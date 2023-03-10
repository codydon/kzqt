<template>
  <div>
    <!-- Only render adminDashboard component if verifyEmail link has not been clicked -->
    <AdminDash v-if="verifyEmailClicked === 0 && $route.path !== '/employee'" />
    <!-- Only render verifyEmail component if verifyEmail link has been clicked -->
    <router-view v-if="verifyEmailClicked === 1" />
    <!-- Only render employeeDashboard component if the current route is '/employee' -->
    <EmployeeDash v-if="$route.path === '/employee'" />
  </div>
</template>
<script>
import { ref } from 'vue';
import AdminDash from './components/AdminDash.vue';
import EmployeeDash from './components/employee/EmployeeDash.vue';

export default {
  components: {
    AdminDash,
    EmployeeDash,
  },
  setup() {
    const verifyEmailClicked = ref(0);

    // check if the route '/verify_email/:token' is being accessed
    if (window.location.pathname.includes('/verify_email')) {
      verifyEmailClicked.value = 1;
    }

    return {
      verifyEmailClicked,
    };
  },
};
</script>