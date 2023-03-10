<template>
  <div>
    <div class="flex justify-center items-center h-screen">
      <div v-if="loading" class="animate-pulse">
        <p>Loading...</p>
      </div>
      <div v-else>
        <div v-if="exists">
          <form @submit.prevent="submitForm" class="flex flex-col items-center">
            <input
              type="hidden"
              name="csrfmiddlewaretoken"
              :value="csrfToken"
            />
            <h3 class="font-bold text-gray-800 text-base">
              Enter a password to create your Kaziquest account
            </h3>
            <label for="password" class="mt-4">Password:</label>
            <input
              type="password"
              id="password"
              v-model="password"
              class="p-2 border border-gray-300 rounded-lg mt-2 w-full"
            />
            <label for="confirm-password" class="mt-4">Confirm Password:</label>
            <input
              type="password"
              id="confirm-password"
              v-model="confirmPassword"
              class="p-2 border border-gray-300 rounded-lg mt-2 w-full"
            />

            <button
              type="submit"
              class="bg-blue-500 text-white px-4 py-2 mt-4 rounded hover:bg-blue-600"
            >
              Submit
            </button>
          </form>
        </div>
        <div v-else>
          <div v-if="error">
            <p>Network error. Contact the administrator</p>
          </div>
          <div v-else>
            <p>Link expired or is already used.Kindly contact the administrator</p>
          </div>
        </div>
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
      error: false,
      loading: true,
      password: null,
      confirmPassword: null,
    };
  },
  created() {
    // Get the token parameter from the route
    this.id = this.$route.params.token;
    // Check if the ID exists in the backend
    setTimeout(() => {
      this.checkIdExists();
    }, 2000);
  },
  methods: {
    checkIdExists() {
      try {
        fetch(`${import.meta.env.VITE_SERVER_URL}/verify_email/${this.id}/`)
          .then((response) => response.json())
          .then((response) => {
            if (response.resp === 1) {
              this.exists = true;
              this.loading = false;
              console.log("TOKEN FOUND");
            } else {
              this.exists = false;
              this.loading = false;
              console.log("NO SUCH TOKEN", response.resp);
            }
          })
          .catch((error) => {
            console.error("FETCH ERROR", error);
            this.error = true;
            this.loading = false;
          });
      } catch (error) {
        console.error("CATCH ERROR", error);
        this.error = true;
        this.loading = false;
      }
    },
    submitForm() {
  if (this.password === this.confirmPassword) {
    // Get the CSRF token from the HTML template
    const csrfToken = document.querySelector(
      'input[name="csrfmiddlewaretoken"]'
    ).value;
    const url = `${import.meta.env.VITE_SERVER_URL}/user_pass/`;
    const data = {
      pw: this.confirmPassword,
      token: this.id,
    };
    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": csrfToken,
      },
      body: JSON.stringify(data),
    };
    // Make an HTTP request to the server to submit the form data
    fetch(url, options)
      .then((response) => response.json())
      .then((response) => {
        // Handle the server response
        if (response.resp === 1) {
          console.log("account created");
          this.$router.push('/employee')
        } else {
          console.log("a/c creation failed", response);
        }
      })
      .catch((error, response) => {
        // Handle any errors that occur during the HTTP request
        console.error("FETCH ERROR", response);
      });
  } else {
    alert("Passwords do not match");
  }
},

  },
};
</script>

<style>
.animate-pulse {
  animation: pulse 1s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0% {
    transform: scale(1);
    opacity: 1;
  }
  50% {
    transform: scale(0.95);
    opacity: 0.5;
  }
  100% {
    transform: scale(1);
    opacity: 1;
  }
}
</style> 