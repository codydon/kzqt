<template>
  <div v-if="!isLoggedin">
    <Login />
  </div>
  <div v-if="isLoggedin" class="flex h-screen overflow-hidden">
    <!-- Sidebar -->
    <div v-show="isOpen" class="bg-gray-800">
      <div class="text-white flex-none flex flex-col">
        <div class="flex p-5">
          <span class="text-xl font-semibold">KaziQuest</span>
        </div>
        <ul class="flex-1 overflow-y-auto">
          <li
            @click="
              (isHome = false),
                (showAddemp = true),
                (showUpdaterole = false),
                (showInventory = false),
                (showLeavedetails = false)
            "
            class="px-4 py-2 hover:bg-gray-700 cursor-pointer"
          >
            Add Employee
          </li>
          <li
            @click="
              (isHome = false),
                (showAddemp = false),
                (showUpdaterole = true),
                (showInventory = false),
                (showLeavedetails = false)
            "
            class="px-4 py-2 hover:bg-gray-700 cursor-pointer"
          >
            Employee Roles
          </li>
          <li
            @click="
              (isHome = false),
                (showAddemp = false),
                (showUpdaterole = false),
                (showInventory = true),
                (showLeavedetails = false)
            "
            class="px-4 py-2 hover:bg-gray-700 cursor-pointer"
          >
            Inventory
          </li>
          <li
            @click="
              (isHome = false),
                (showAddemp = false),
                (showUpdaterole = false),
                (showInventory = false),
                (showLeavedetails = true)
            "
            class="px-4 py-2 hover:bg-gray-700 cursor-pointer"
          >
            Leave Details
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
            <div class="relative" @click="showUserDropdown = !showUserDropdown">
              <span
                class="bg-red-500 text-white rounded-full text-xs absolute top-0 right-0 px-2 py-1"
                >{{ badge }}</span
              >
              <button
                class="bg-gray-500 hover:bg-gray-700 text-white font-bold py-2 px-4 rounded-full"
              >
                logs
              </button>
            </div>

            <div class="relative" v-show="showUserDropdown">
              <div
                class="absolute right-0 mt-12 p-4 w-72 bg-slate-200 rounded-lg shadow-xl z-10 overflow-y-scroll max-h-96"
              >
              <div class="text-right px-4 pb-2 text-red-600 font-extrabold cursor-pointer" @click="showUserDropdown = !showUserDropdown">
                X
              </div>
                <div
                  class="text-center cursor-pointer mb-4 rounded-full p-2 text-sm text-blue-500 bg-gray-300"
                  @click="update_read"
                >
                  mark as read
                </div>
                <div
                  v-for="message in messages"
                  :key="message"
                  class="text-center hover:bg-slate-300 mb-4 p-2 rounded"
                >
                  {{ message }}
                </div>
              </div>
            </div>
          </div>

          <div class="flex">
            <div class="text-gray-500 text-sm my-auto px-2">
              {{ employee.EmployeeId }}
            </div>
            <div
              class="avatar bg-gray-100 text-center rounded-full py-2 px-4"
              @click="showLogout = !showLogout"
            >
              {{ employee.Name[0] }}
            </div>
            <div class="relative" v-show="showLogout">
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
      </header>
      <main class="px-6 py-4">
        <div v-if="isHome" class="">admin dashboard</div>
        <div v-else class="flex flex-col">
          <AddEmployee v-if="showAddemp" />
          <UpdateRole v-if="showUpdaterole" />
          <Inventory v-if="showInventory" />
          <LeaveDetails v-if="showLeavedetails" />
        </div>
      </main>
    </div>
  </div>
</template>

<script>
import Pusher from "pusher-js";
import AddEmployee from "./AddEmployee.vue";
import UpdateRole from "./UpdateRole.vue";
import Inventory from "./Inventory.vue";
import LeaveDetails from "./LeaveDetails.vue";
import Login from "./Login.vue";
import Swal from "sweetalert2";

export default {
  data() {
    return {
      isLoggedin: false,
      isOpen: true,
      showLogs: false,
      showAddemp: false,
      showUpdaterole: false,
      showInventory: false,
      showLeavedetails: false,
      showUserDropdown: false,
      showLogout: false,
      isHome: true,
      username: "John Doe",
      messages: [],
      badge: 0,
      employee: {},
    };
  },
  created() {
    this.getauth();

    Pusher.logToConsole = true;
    const pusher = new Pusher(`${import.meta.env.VITE_PUSHER_APP_KEY}`, {
      cluster: "ap2",
    });
    const channel = pusher.subscribe("notify");
    // Bind a callback function to the pusher:subscription_succeeded event
    channel.bind("pusher:subscription_succeeded", () => {
      console.log("Pusher subscription succeeded.");
    });
    // Bind a callback function to the notification event
    channel.bind("notification", (data) => {
      console.log("Pusher notification received:", data);
      if (data) {
        this.messages.unshift(data.message);
        this.badge += 1;
      }
    });
  },
  components: { Login, AddEmployee, UpdateRole, Inventory, LeaveDetails },
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
          if (response.success === true && response.user.Role === "admin") {
            this.isLoggedin = true;
            this.employee = response.user;
            this.get_notifications();
          } else {
            this.isLoggedin = false;
          }
        });
    },
    get_notifications() {
      fetch(`${import.meta.env.VITE_SERVER_URL}/get_notifications`)
        .then((response) => response.json())
        .then((response) => {
          // console.log(response);
          if (response.success === true) {
            for (let n of response.notifications) {
              this.messages.push(n);
              this.badge += 1;
            }
          }
        });
    },
    update_read(){
      this.badge = 0;
      fetch(`${import.meta.env.VITE_SERVER_URL}/update_read`, {
        headers: { "content-type": "application/json" },
        method: "PUT",
      })
      .then((response) => response.json())
      .then((response) => {
          // console.log(response);
          if (response.success === true) {
            this.get_notifications();
          }
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
            this.showUserDropdown = false;
            this.isLoggedin = false;
            localStorage.clear();
            // window.location.replace(`${import.meta.env.VITE_CLIENT_URL}/login`);
            fetch(`${import.meta.env.VITE_SERVER_URL}/notify`, {
              method: "POST",
              headers: {
                "Content-Type": "application/json",
              },
              body: JSON.stringify({
                EmpId: this.employee.EmployeeId,
                message:
                  "At " +
                  new Date().toLocaleString() +
                  ", " +
                  this.employee.EmployeeId +
                  " logged out",
              }),
            });
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
