<template>
  <!-- <div v-if="!isLoggedin" class="bg-slate-100 flex items-center justify-center min-h-screen">
    <Login />
  </div> -->
  <div class="flex h-screen overflow-hidden">
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
                class="absolute right-0 mt-2 p-4 w-72 bg-slate-200 rounded-lg shadow-xl z-10 overflow-y-scroll"
              >
                <div
                  class="text-center cursor-pointer mb-4 rounded-full p-2 text-sm text-red-400 bg-gray-300"
                  @click="
                    ($event) => {
                      (showUserDropdown = !showUserDropdown), (badge = 0);
                    }
                  "
                >
                  close
                </div>
                <div
                  v-for="message in messages"
                  :key="message"
                  class="text-center hover:bg-slate-300"
                >
                  {{ message }}
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
      isHome: true,
      username: "John Doe",
      messages: [],
      badge: 0,
    };
  },
  created() {
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
      this.messages.push(`(time) Employee ${data.username} logged in.`);
      this.badge += 1;
    });
  },
  components: { Login, AddEmployee, UpdateRole, Inventory, LeaveDetails },
};
</script>



