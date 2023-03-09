<template>
  <div>
    <div v-if="loading">
      <p>Loading...</p>
    </div>
    <div v-else>
      <div v-if="exists">
        <form @submit.prevent="submitForm">
          <label for="password">Password:</label>
          <input type="password" id="password" v-model="password" />
          <label for="confirm-password">Confirm Password:</label>
          <input
            type="password"
            id="confirm-password"
            v-model="confirmPassword"
          />
          <button type="submit">Submit</button>
        </form>
      </div>
      <div v-else>
        <p>Link does not exist. Contact the administrator</p>
      </div>
    </div>
  </div>
</template>
  
  <script>
export default {
  name: "VerifyEmail",
  data() {
    return {
      id: null,
      exists: false,
      loading: true,
      password: null,
      confirmPassword: null,
    };
  },
//   created() {
//     // Get the ID parameter from the route
//     this.id = this.$route.params.id;

//     // Check if the ID exists in the backend
//     this.checkIdExists();
//   },
  methods: {
    checkIdExists() {
      // Make API call to check if the ID exists
      // Replace the API endpoint and request body with your own backend API call
      fetch("/api/verify_email/" + this.$route.params.token)
        .then((response) => {
          if (response.ok) {
            return response.json();
          } else {
            throw new Error("Network response was not ok");
          }
        })
        .then((data) => {
          if (data.exists) {
            this.exists = true;
          } else {
            this.exists = false;
          }
          this.loading = false;
        })
        .catch((error) => {
          console.error("Error:", error);
          this.loading = false;
        });
    },
    submitForm() {
      if (this.password === this.confirmPassword) {
        // Handle form submission
        // You can access the password input value with this.password
        // and the confirm password input value with this.confirmPassword
      } else {
        alert("Passwords do not match");
      }
    },
  },
};
</script>
  