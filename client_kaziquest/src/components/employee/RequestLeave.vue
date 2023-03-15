<template>
  <div class="p-8">
    <h1 class="text-2xl font-bold mb-4">Leave Request</h1>
    <form @submit.prevent="submitForm">
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="start-date">
          Start Date
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="start-date"
          type="date"
          v-model="startDate"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="end-date">
          End Date
        </label>
        <input
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="end-date"
          type="date"
          v-model="endDate"
          required
        />
      </div>
      <div class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" for="description">
          Description
        </label>
        <textarea
          class="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          id="description"
          rows="3"
          v-model="description"
          required
        ></textarea>
      </div>
      <div class="flex items-center justify-between">
        <button
          class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
          type="submit"
        >
          Request Leave
        </button>
      </div>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      startDate: "",
      endDate: "",
      description: "",
    };
  },
  methods: {
    submitForm() {
      // Submit form data to the server and handle response
      // You can use Axios or Fetch to make API requests
      // For example:
      axios
        .post("/api/leave-request", {
          start_date: this.startDate,
          end_date: this.endDate,
          description: this.description,
        })
        .then((response) => {
          console.log(response.data);
          // Handle successful response, for example by displaying a success message
        })
        .catch((error) => {
          console.error(error);
          // Handle error response, for example by displaying an error message
        });
    },
  },
};
</script>

