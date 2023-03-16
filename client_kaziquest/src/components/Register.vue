<template>
  <div class="rounded-md shadow-lg p-8 container mx-auto mt-8">
    <h2 class="text-2xl font-bold mb-4">Employer Sign Up</h2>
    <form @submit.prevent="submitForm">
      <div class="mb-4">
        <label for="name" class="block font-semibold mb-1">Name:</label>
        <input
          id="name"
          v-model="name"
          type="text"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 transition duration-500 ease-in-out"
          required
        />
      </div>
      <div class="mb-4">
        <label for="role" class="block font-semibold mb-1"
          >Role/Position:</label
        >
        <input
          id="role"
          v-model="role"
          type="text"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 transition duration-500 ease-in-out"
          required
        />
      </div>
      <div class="mb-4">
        <label for="company" class="block font-semibold mb-1">Company:</label>
        <input
          id="company"
          v-model="company"
          type="text"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 transition duration-500 ease-in-out"
          required
        />
      </div>
      <div class="mb-4">
        <label for="email" class="block font-semibold mb-1">Email:</label>
        <input
          id="email"
          v-model="email"
          type="email"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 transition duration-500 ease-in-out"
          required
        />
      </div>
      <div class="mb-4">
        <label for="phone" class="block font-semibold mb-1"
          >Phone Number:</label
        >
        <input
          id="phone"
          v-model="phone"
          type="tel"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 transition duration-500 ease-in-out"
          required
        />
      </div>
      <div class="mb-4">
        <label for="numEmployees" class="block font-semibold mb-1"
          >Number of employees:</label
        >
        <select
          id="numEmployees"
          v-model="numEmployees"
          class="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:border-blue-500 transition duration-500 ease-in-out"
          required
        >
          <option value="">Please select</option>
          <option v-for="n in employeeOptions" :key="n" :value="n">
            {{ n }}
          </option>
        </select>
      </div>
      <button
        type="submit"
        class="block bg-blue-500 hover:bg-blue-600 text-white font-semibold rounded-md py-2 px-4 transition duration-500 ease-in-out transform hover:-translate-y-1 hover:scale-110"
      >
        Register
      </button>
    </form>
  </div>
</template>
  
  <script>
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      name: "",
      role: "",
      company: "",
      email: "",
      phone: "",
      numEmployees: "",
      employeeOptions: ["1-10", "11-50", "51-100", "101-500", "500+"],
    };
  },
  methods: {
    submitForm() {
      // Your form submission logic here
      const formdata = {
        name: this.name,
        role: this.role,
        company: this.company,
        email: this.email,
        phone: this.phone,
        // numEmployees: this.numEmployees,
      }

      console.log(formdata);
      fetch(`${import.meta.env.VITE_SERVER_URL}/reg_admin/`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formdata),
      })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        if (data.success === true) {
          // window.location.href = "/admin";
          this.name = "";
          this.role = "";
          this.company = "";
          this.email = "";
          this.phone = "";
          this.numEmployees = "";

          Swal.fire({
            icon:'success',
            title: 'Success!',
            text: "check your email for account activation link",
          });
        } else {
          alert("network error! cant add administartor");
        }
      });
    },
  },
};
</script>
  
