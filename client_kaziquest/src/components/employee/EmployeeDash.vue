<template>
  <div v-if="!isLogin" class="">
    <Login />
  </div>
  <div v-if="isLogin" class="flex h-screen overflow-hidden">
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
            <div class="relative flex">
              <div class="text-gray-500 text-sm my-auto px-2">
                {{ employee.EmployeeId }}
              </div>
              <div
                class="avatar bg-gray-100 text-center rounded-full py-2 px-4"
                @click="showUserDropdown = !showUserDropdown"
              >
                {{ employee.Name[0] }}
              </div>
              <div class="relative" v-show="showUserDropdown">
                <div
                  class="absolute right-0 mt-12 bg-slate-200 rounded-lg shadow-xl z-10"
                >
                  <!-- <div
                    class="text-right cursor-pointer mb-4 rounded-full text-sm text-red-400 hover:bg-gray-300"
                    @click="showUserDropdown = !showUserDropdown       
                    "
                  >
                    X
                  </div> -->
                  <div class="text-center hover:bg-slate-200">
                    <!-- <p class="hover:bg-slate-300 px-3 mb-2 rounded-full cursor-pointer">profile</p> -->
                    <p
                      class="hover:bg-slate-300 px-10 py-2 cursor-pointer rounded"
                      @click="logout"
                    >
                      logout
                    </p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </header>
      <!--  -->
      <div class="p-6">
        <Assets v-if="isShow == 1" />
        <UpdateProfile v-if="isShow == 2" :employee="employee" />
        <RequestLeave v-if="isShow == 3" :f="f" />
      </div>
    </div>
  </div>
</template>

<script>
import UpdateProfile from "./UpdateProfile.vue";
import RequestLeave from "./RequestLeave.vue";
import Assets from "./Assets.vue";
import Login from "../Login.vue";
import Swal from "sweetalert2";

export default {
  name: "EmployeeDash",
  data() {
    return {
      isOpen: true,
      isShow: 1,
      isLogin: false,
      showUserDropdown: false,
      employee: {},
      f: 1,
    };
  },

  components: {
    UpdateProfile,
    RequestLeave,
    Assets,
    Login,
  },
  mounted() {},
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
          if (response.success === true) {
            this.isLogin = true;
            this.employee = response.user;
          } else {
            this.isLogin = false;
          }
        });
    },
    pnotify() {
      fetch(`${import.meta.env.VITE_SERVER_URL}/notify`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          EmpId: this.employee.EmployeeId,
          message: "At " + new Date().toLocaleString() + ", " + this.employee.EmployeeId + " logged out",
        }),
      });
    },
    logout() {
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        credentials: "include",
      };
      fetch(`${import.meta.env.VITE_SERVER_URL}/logout/`, requestOptions)
        .then((response) => response.json())
        .then((response) => {
          console.log(response);
          if (response.success === true) {
            this.pnotify();
            this.showUserDropdown = false;
            this.isLogin = false;
            localStorage.clear();
            // this.$router.push({ name: "Login" });
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
  },
};
</script>
