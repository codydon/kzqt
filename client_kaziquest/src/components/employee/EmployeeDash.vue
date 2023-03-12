<template>
  <div class="" v-if="!isLogin">
    <div
      class="flex flex-col items-center justify-center min-h-screen bg-gray-100"
    >
      <div class="bg-white rounded-lg shadow-md p-8">
        <h3 v-show="loginstatus" class="text-red-500 bg-slate-200 p-2 text-center rounded">Wrong creddentials, try again</h3>
        <h2 class="text-xl font-medium mb-4">Employee Login</h2>
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
  <div class="flex h-screen overflow-hidden" v-else>
    <!-- Sidebar -->
    <div v-show="isOpen" class="bg-gray-800">
      <div class="text-white flex-none flex flex-col">
        <div class="flex p-5">
          <span class="text-xl font-semibold">Employee Dashboard</span>
        </div>
        <ul class="flex-1 overflow-y-auto">
          <li
            @click="isShow = 1"
            class="px-4 py-2 hover:bg-gray-700 cursor-pointer"
          >
            <p>Assets</p>
          </li>
          <li
            @click="isShow = 2"
            class="px-4 py-2 hover:bg-gray-700 cursor-pointer"
          >
            <p>Update Profile</p>
          </li>
          <li
            @click="isShow = 3"
            class="px-4 py-2 hover:bg-gray-700 cursor-pointer"
          >
            <p>Request Leave</p>
          </li>
        </ul>
      </div>
    </div>

    <!-- Main Content -->
    <div class="flex-1 bg-gray-100">
      <header class="bg-white shadow">
        <div class="flex items-center justify-between h-16 px-6">
          <button
            class="text-gray-500 hover:text-gray-600"
            @click="isOpen = !isOpen"
          >
            <svg class="h-6 w-6 fill-current" viewBox="0 0 24 24">
              <path
                v-if="isOpen"
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M4 6h16v2H4V6zm0 5h16v2H4v-2zm0 5h16v2H4v-2z"
              />
              <path
                v-else
                fill-rule="evenodd"
                clip-rule="evenodd"
                d="M4 6h16v2H4V6zm0 5h16v2H4v-2zm0 5h16v2H4v-2z"
              />
            </svg>
          </button>
          <div class="flex">
            <div class="text-gray-500 text-sm my-auto px-2">John Doe</div>
            <div class="avatar bg-gray-100 text-center rounded-full py-2 px-4">
              J
            </div>
          </div>
        </div>
      </header>
      <!--  -->
      <main class="p-6">
        <Assets v-if="isShow == 1" />
        <UpdateProfile v-if="isShow == 2" />
        <RequestLeave v-if="isShow == 3" />
      </main>
    </div>
  </div>
</template>

<script>
import UpdateProfile from "./UpdateProfile.vue";
import RequestLeave from "./RequestLeave.vue";
import Assets from "./Assets.vue";
import Swal from "sweetalert2";


export default {
  data() {
    return {
      isOpen: true,
      isShow: 1,
      isAdmin: false,
      isLogin: false,
      employeeID: "",
      pw: "",
      loginstatus:false,
    };
  },

  components: {
    UpdateProfile,
    RequestLeave,
    Assets,
  },
  methods: {
    empLogin() {
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          pw:this.pw,
          emp_id: this.employeeID
        }),
      };

      fetch(`${import.meta.env.VITE_SERVER_URL}/emplogin/`, requestOptions)
      .then((response) => response.json())
        .then((response) => {
          console.log(response);
          if ((response.success === true)) {
            this.isLogin = true
            this.pnotify()
            // Swal.fire({
            //   icon: "success",
            //   title: "Success",
            //   text: "Asset added successfully",
            // });
          } else {
            this.loginstatus = true
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
    pnotify(){
        fetch(`${import.meta.env.VITE_SERVER_URL}/notify/`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            username: this.employeeID
          }),
        })
    },
  },
  
};
</script>
