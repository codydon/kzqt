<template>
  <Register v-if="$route.path === '/register'" />
  <Login v-if="$route.path === '/login'" />
  <AdminDash v-if="$route.path === '/admin'" />
  <EmployeeDash v-if="$route.path === '/employee'" />
  <VerifyEmail v-if="showVerifyEmail && $route.path !== '/login'" />
</template>

<script>
import { ref } from "vue";
import { computed } from "vue";
import AdminDash from "./components/AdminDash.vue";
import Register from "./components/Register.vue";
import Login from "./components/Login.vue";
import EmployeeDash from "./components/employee/EmployeeDash.vue";
import VerifyEmail from "./components/VerifyEmail.vue";

export default {
  components: {
    AdminDash,
    EmployeeDash,
    Register,
    VerifyEmail,
    Login,
  },
  setup() {
    const showVerifyEmail = computed(() => {
      return window.location.pathname.includes("/verify_email");
    });


    const isLoggedIn = ref(false);

    if (localStorage.getItem("auth")) {
      isLoggedIn.value = true;
    }
   
    
    return {
      showVerifyEmail,
      isLoggedIn,
    };
  },
};
</script>
