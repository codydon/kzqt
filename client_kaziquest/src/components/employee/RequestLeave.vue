<template>
  <div class="p-8">
    <h1 class="text-2xl font-bold mb-4">Leave Request</h1>
    <form @submit.prevent="submitLeaveRequest">
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
          Description/reason
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
import Swal  from 'sweetalert2';


export default {
  name: 'RequestLeave',
  data() {
    return {
      startDate: "",
      endDate: "",
      description: "",
      employee:{},
    };
  },
  created(){
    this.getauth()
  },
  methods: {
    getauth() {
      const authToken = localStorage.getItem("tkn");

      fetch(`${import.meta.env.VITE_SERVER_URL}/getauth`, {
        headers: { "content-type": "application/json" },
        method: "POST",
        body: JSON.stringify({
          tkn: authToken,
        }),
      })
        .then((response) => response.json())
        .then((response) => {
          // console.log(response);
          if (response.success === true) {
            this.isLogin = true;
            this.employee = response.user;
          }
          else{
            this.$router.push({ name: "Login" });
          }
        });
    },

    submitLeaveRequest() {
      console.log("submitting form");
      fetch(`${import.meta.env.VITE_SERVER_URL}/leave_request`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          // 'include-credentials': 'true',
        },
        body: JSON.stringify({
          start_date: this.startDate,
          end_date: this.endDate,
          description: this.description,
          eId: this.employee.EmployeeId
        })
        })
        .then((response) => response.json())
        .then((response) => {
          if(response.success === true){
            this.startDate = "",
            this.endDate = "",
            this.description = "",
            Swal.fire({
              icon:'success',
              title: 'Request sent successfully',
              showConfirmButton: true,
              timer: 1500
            })
          }
          })
        .catch((error) => {
          console.error(error);
          Swal.fire({
              icon:'error',
              title: 'Request failed',
              showConfirmButton: true,
              timer: 1500
            })
        });
    },
  },
};
</script>

