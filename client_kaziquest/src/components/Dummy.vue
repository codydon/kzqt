<template>
 logged in:
{{ authState.isLoggedIn }}
user:
{{ authState.user }}
</template>

<script>
import { useAuth } from "@/composables/useAuth";

export default {
    data() {
      return {
          authState:{},
          checkauth:false,
          logout:false
      };
    },
  created() {
    const { authState, checkauth, logout } = useAuth();
    checkauth()
  },
  mounted() {
    console.log(this.authState);
  },
};
</script>

<style>
</style>