<template>
  <div class="flex h-screen overflow-hidden">
    <!-- Sidebar -->
    <div v-show="isOpen" class="bg-gray-800">
      <div class="text-white flex-none flex flex-col">
        <div class="flex p-5">
          <span class="text-xl font-semibold">Employee Dashboard</span>
        </div>
        <ul class="flex-1 overflow-y-auto">
          <li @click="isShow = 1" class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
            <p>Assets</p>
          </li>
          <li @click="isShow = 2" class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
            <p>Update Profile</p>
          </li>
          <li @click="isShow = 3" class="px-4 py-2 hover:bg-gray-700 cursor-pointer">
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

export default {
  data() {
    return {
      isOpen: true,
      isShow: 1,
      isAdmin: false,
    };
  },

  components: {
    UpdateProfile,
    RequestLeave,
    Assets,
  },
};
</script>
