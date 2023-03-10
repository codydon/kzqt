<template>
    <div class="flex h-screen overflow-hidden">
      <!-- Sidebar -->
      <div v-show="isOpen" class="bg-gray-800">
        <div class="text-white flex-none flex flex-col">
          <div class="flex p-5">
            <span class="text-xl font-semibold">KaziQuest</span>
          </div>
          <ul class="flex-1 overflow-y-auto">
            <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
              <router-link to="/addemployee">Add Employee</router-link>
            </li>
            <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
              <router-link to="/assign_asset">Assign Asset</router-link>
            </li>
            <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
              <router-link to="/updaterole">Employee Roles</router-link>
            </li>
            <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
              <router-link to="/inventory">Inventory</router-link>
            </li>
            <li class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
              <router-link to="/leavedetails">Leave Details</router-link>
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
              <div class="text-gray-500 text-sm my-auto px-2">Onserio</div>
              <div class="avatar bg-gray-100 text-center rounded-full py-2 px-4">
                D
              </div>
            </div>
          </div>
        </header>
        <!--  -->
        <main class="p-6">
          <router-view></router-view>
        </main>
      </div>
  
     
     
    </div>
  </template>
  
  <script>
  import AddEmployee from "../components/AddEmployee.vue";
  import UpdateRole from "../components/UpdateRole.vue";
  import Inventory from "../components/Inventory.vue";
  import LeaveDetails from "../components/LeaveDetails.vue";
  import AssignAsset from "../components/AssignAsset.vue";
  
  export default {
    data() {
      return {
        isOpen: true,
        isAdmin: true,
      };
    },
  
    components: {
      AddEmployee,
      UpdateRole,
      Inventory,
      LeaveDetails,
      AssignAsset,
    },
  };
  </script>
  