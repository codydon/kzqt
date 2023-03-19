<template>
  <div class="bg-slate-100 flex items-center justify-center min-h-screen">
    <div class="flex flex-col items-center justify-centerbg-gray-100">
      <div class="bg-white rounded-lg shadow-md p-8">
        <h3
          v-show="loginstatus"
          class="text-red-500 bg-slate-200 p-2 text-center rounded"
        >
          Wrong creddentials, try again
        </h3>
        <h2 class="text-xl font-medium mb-4">KaziQuest Login</h2>
        <form @submit.prevent="empLogin()">
          <div class="mb-4">
            <label
              class="block text-gray-700 font-medium mb-2"
              for="employee-id"
              >Employee ID</label
            >
            <input
              v-model="employeeID"
              class="border border-gray-400 p-2 w-full rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              type="text"
              id="employee-id"
              name="employee-id"
            />
          </div>
          <div class="mb-4">
            <label class="block text-gray-700 font-medium mb-2" for="password"
              >Password</label
            >
            <input
              v-model="pw"
              class="border border-gray-400 p-2 w-full rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-600"
              type="password"
              id="password"
              name="password"
            />
          </div>
          <button
            class="bg-blue-600 text-white py-2 px-4 rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-600"
            type="submit"
          >
            Login
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import Swal from "sweetalert2";

export default {
  data() {
    return {
      loginstatus: false,
      employeeID: "",
      pw: ""
    };
  },
  created() {
  },
  methods: {
    empLogin() {
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
        body: JSON.stringify({
          pw: this.pw,
          emp_id: this.employeeID,
        }),
      };

      fetch(`${import.meta.env.VITE_SERVER_URL}/emplogin`, requestOptions)
        .then((response) => response.json())
        .then((response) => {
          console.log(response);
          if (response.success === true) {
            this.isLogin = true;
            this.pnotify();
            localStorage.setItem("tkn", response.jwt);
            if(response.role === "admin") {
                window.location.href = "/admin";
            } else {
                window.location.href = "/employee";
            }
          } else {
            this.loginstatus = true;
          }
        })
        .catch((error) => {
          Swal.fire({
            icon: "error",
            title: "Error",
            text: error.message,
          });
        });
    },
    pnotify() {
      fetch(`${import.meta.env.VITE_SERVER_URL}/notify`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          EmpId: this.employeeID,
          message: "At " + new Date().toLocaleString() + ", " + this.employeeID + " logged in"
        }),
      });
    },
  },
};
</script>
