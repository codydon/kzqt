<template>
  <div v-if="employee" class="max-w-md mx-auto">
    <h1 class="text-3xl font-bold mb-6">Update Employee Info</h1>
    <form @submit.prevent="handleSubmit">
      <label class="block text-gray-700 font-bold mb-2" for="name">Name</label>
      <input
        v-model="employee.Name"
        class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 leading-tight focus:outline-none focus:bg-white focus:border-blue-500"
        id="name"
        type="text"
      />
      <label class="block text-gray-700 font-bold mb-2" for="name"
        >ID number</label
      >
      <input
        v-model="employee.IDnumber"
        class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 leading-tight focus:outline-none focus:bg-white focus:border-blue-500"
        id="id"
        type="number"
      />
      <label class="block text-gray-700 font-bold mb-2" for="name"
        >KRA PIN</label
      >
      <input
        v-model="employee.KRAPIN"
        class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 leading-tight focus:outline-none focus:bg-white focus:border-blue-500"
        id="kra"
        type="integer"
      />
      <label class="block text-gray-700 font-bold mb-2" for="email"
        >email</label
      >
      <input
        v-model="employee.email"
        class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 leading-tight focus:outline-none focus:bg-white focus:border-blue-500"
        id="email"
        type="email"
      />
      <label class="block text-gray-700 font-bold mb-2" for="phoneNumber"
        >Phonenumber</label
      >
      <input
        v-model="employee.PhoneNumber"
        class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 leading-tight focus:outline-none focus:bg-white focus:border-blue-500"
        id="phoneNumber"
        type="tel"
      />
      <label class="block text-gray-700 font-bold mb-2" for="dob">DOB</label>
      <input
        v-model="employee.DOB"
        class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 leading-tight focus:outline-none focus:bg-white focus:border-blue-500"
        id="dob"
        type="date"
      />
      <button
        type="submit"
        class="bg-blue-500 mt-4 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Update
      </button>
    </form>
  </div>
  <div v-else>Loading...</div>
</template>

<script>
import Swal from "sweetalert2";

export default {
  props: {
    employee: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {};
  },
  created() {
    this.getauth();
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
          // console.log(response);
          if (response.success === true) {
            this.isLogin = true;
            this.employee = response.user;
          } else {
            this.$router.push({ name: "Login" });
          }
        });
    },
    async handleSubmit() {
      try {
        console.log(this.employee);
        const response = await fetch(
          `${import.meta.env.VITE_SERVER_URL}/update_profile/`,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
            },
            body: JSON.stringify(this.employee),
          }
        );
        const data = await response.json();
        console.log(data);
        if (data.success === true) {
          this.getauth;
          Swal.fire({
            icon: "success",
            title: "Updated successfully",
            showConfirmButton: true,
            timer: 1500,
          });
        }
      } catch (error) {
        Swal.fire({
          icon: "Failed, network error",
          title: error,
          showConfirmButton: true,
          timer: 1500,
        });
      }
    },
  },
};
</script>
