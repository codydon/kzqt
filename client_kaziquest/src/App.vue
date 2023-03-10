<template>
  <div>
    <!-- Only render adminDashboard component if verifyEmail link has not been clicked -->
    <AdminDash v-if="!verifyEmailClicked" />
    <!-- Only render verifyEmail component if verifyEmail link has been clicked -->
    <router-view v-if="verifyEmailClicked" />
  </div>
</template>

<script>
import { ref } from 'vue';
import AdminDash from './components/AdminDash.vue';

export default {
  components: {
    AdminDash,
  },
  setup() {
    const verifyEmailClicked = ref(false);

    // check if the route '/verify_email/:token' is being accessed
    if (window.location.pathname.includes('/verify_email')) {
      verifyEmailClicked.value = true;
    }

    return {
      verifyEmailClicked,
    };
  },
};
</script>
