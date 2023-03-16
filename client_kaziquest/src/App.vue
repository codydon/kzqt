<template>
    <AdminDash v-if="$route.path === '/admin'" />
    <VerifyEmail v-if="verifyEmailClicked === 1" />
    <EmployeeDash v-if="$route.path === '/employee'" />
    <Register v-if="$route.path === '/register'" />
    <router-view></router-view>
</template>

<script>
import { ref } from 'vue';
import AdminDash from './components/AdminDash.vue';
import Register from './components/Register.vue';
import EmployeeDash from './components/employee/EmployeeDash.vue';
import VerifyEmail from './components/VerifyEmail.vue';
import { useRouter } from 'vue-router';

export default {
  components: {
    AdminDash,
    EmployeeDash,
    Register,
    VerifyEmail,
  },
  setup() {
    const verifyEmailClicked = ref(0);

    const router = useRouter();
    const isLoggedIn = ref(false);

    // check if the 'auth' item is present in local storage
    if (localStorage.getItem('auth')) {
      isLoggedIn.value = true;
      // router.push('/admin');
    }
    
    // check if the route '/verify_email/:token' is being accessed
    if (window.location.pathname.includes('/verify_email')) {
      verifyEmailClicked.value = 1;
    }

    return {
      verifyEmailClicked,
      isLoggedIn
    };
  },
};
</script>

