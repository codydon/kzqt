<template>
  <div class="flex flex-col items-center">
    <h1 class="text-3xl font-bold mb-6">My Assets</h1>
    <table class="border-collapse border border-gray-400">
      <thead>
        <tr>
          <th class="border border-gray-400 px-4 py-2">Asset</th>
          <th class="border border-gray-400 px-4 py-2">AssetID</th>
          <th class="border border-gray-400 px-4 py-2">Description</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(asset, index) in assets" :key="index">
          <td
            class="border border-gray-400 px-4 py-2 cursor-pointer hover:bg-gray-100"
          >
            {{ asset.AssetName }}
          </td>
          <td
            class="border border-gray-400 px-4 py-2 cursor-pointer hover:bg-gray-100"
          >
            {{ asset.AssetId }}
          </td>
          <td
            class="border border-gray-400 px-4 py-2 cursor-pointer hover:bg-gray-100"
          >
            {{ asset.Description }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>

export default {
  data() {
    return {
      assets: {},
      employee: {},
    };
  },
  created() {
    this.getauth();
  },
  mounted() {
  },
  methods: {
    getauth() {
      const authToken = localStorage.getItem("tkn");

      fetch(`${import.meta.env.VITE_SERVER_URL}/getauth`, {
        headers: { "content-type": "application/json" },
        method: "POST",
        body: JSON.stringify({
          tkn: authToken,
        }),
      })
        .then((response) => response.json())
        .then((response) => {
          if (response.success === true) {
            this.isLogin = true;
            this.employee = response.user;
            this.fetchAssets()
          } else {
            this.$router.push({ name: "Login" });
          }
        });
    },
    async fetchAssets() {
      console.log(this.employee);
      const response = await fetch(
        `${import.meta.env.VITE_SERVER_URL}/fetch_assets/${
          this.employee.EmployeeId
        }/`
      );
      const data = await response.json();
      if (data.success === true) {
        this.assets = data.assets;
        console.log("tdvfvekd", this.assets);
      }
    },
  },
 
};
</script>
