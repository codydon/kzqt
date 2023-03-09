<template>
  <div>
    <header>
      <!-- Header content -->
    </header>
    <main>
      <!-- Dashboard content -->
      <div class="">
        <!-- <AdminDash /> -->
      </div>
      <router-view></router-view>
    </main>
    <footer>
      <!-- Footer content -->
    </footer>
  </div>
</template>

<script>
import AdminDash from './components/AdminDash.vue';

export default {
  name: "App",
  components:{AdminDash}
};
</script>

<style>
/* CSS styles for the layout */
</style>
