<template>
  <div class="bg-gray-100 min-h-screen flex flex-col items-center">
    <h3 class="font-bold p-4">Add Employee</h3>
    <form
      class="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4 w-full max-w-md"
    >
      <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken" />
      <div class="mb-4">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="name">
          Name
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="name"
          type="text"
          v-model="name"
          @focus="isNameFocused = true"
          @blur="isNameFocused = false"
        />
        <div
          v-show="isNameFocused"
          class="h-1 w-full mt-1 bg-blue-500 rounded-full"
        ></div>
      </div>
      <div class="mb-6">
        <label class="block text-gray-700 text-sm font-bold mb-2" for="email">
          Email
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="email"
          type="email"
          v-model="email"
          @focus="isEmailFocused = true"
          @blur="isEmailFocused = false"
        />
        <div
          v-show="isEmailFocused"
          class="h-1 w-full mt-1 bg-blue-500 rounded-full"
        ></div>
      </div>
      <div class="flex items-center justify-between">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="button"
          @click="saveEmployee"
        >
          Save
        </button>
      </div>
    </form>
  </div>
</template>
<script>
import Swal from "sweetalert2";

export default {
  data() {
    return {
      name: "",
      email: "",
      employee_id: "",
      verification_token: "",
      isNameFocused: false,
      isEmailFocused: false,
      csrfToken: null,
      showUserDropdown: false,
    };
  },
  methods: {
    saveEmployee() {
      const employee = {
        name: this.name,
        email: this.email,
      };
      console.log("Save employee", employee);

      const csrfToken = document.querySelector(
        'input[name="csrfmiddlewaretoken"]'
      ).value;

      const url = `${import.meta.env.VITE_SERVER_URL}/create_employee/`;
      const options = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-CSRFToken": csrfToken,
        },
        body: JSON.stringify(employee),
      };

      fetch(url, options)
        .then((response) => response.json())
        .then((response) => {
          if (response.success === true) {
            // console.log("RESPONSE", data);
            // Clear the form
            this.name = "";
            this.email = "";

            // Show success message
            Swal.fire({
              title: "Success!",
              text: "Employee created successfully.",
              icon: "success",
              timer: 1500, // 1.5 seconds
              timerProgressBar: true,
              showConfirmButton: false,
            });
          }
        })
        .catch((error) => {
          console.error("POST ERROR", error);
          this.name = "";
          this.email = "";
          Swal.fire({
            title: "Oops...",
            text: "Email already exists",
            icon: "error",
            timer: 1500, // 1.5 seconds
            timerProgressBar: true,
            showConfirmButton: false,
          });
        });
    },
  },
};
</script>
