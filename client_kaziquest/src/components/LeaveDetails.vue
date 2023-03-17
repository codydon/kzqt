<template>
  <div class="bg-white rounded-lg shadow overflow-x-auto">
    <p class="p-4 font-bold underline">Leave Requests</p>
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
          >
            Employee ID
          </th>
          <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
          >
            Start Date
          </th>
          <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
          >
            End Date
          </th>
          <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
          >
            Description
          </th>
          <th
            scope="col"
            class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider"
          >
            APPROVED
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="(row, index) in leaveRequests" :key="index">
          <td
            class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900"
          >
            {{ row.EmpId }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            {{ row.StartDate }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            {{ row.EndDate }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            {{ row.Description }}
          </td>
          <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">
            <button
              v-if="row.Status === 'pending'"
              @click="approveLeave(index)"
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
            >
              Approve
            </button>
            <span
              v-else-if="row.Status === 'Approved'"
              class="text-green-500 font-bold"
              >{{ row.Status }}</span
            >
            <span v-else class="text-red-500 font-bold">{{ row.Status }}</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import Swal from 'sweetalert2';

export default {
  data() {
    return {
      leaveRequests: [],
    };
  },
  created() {
    this.fetchLeaveRequests();
  },
  methods: {
    fetchLeaveRequests() {
      fetch(`${import.meta.env.VITE_SERVER_URL}/getRequests/`)
        .then((response) => response.json())
        .then((response) => {
          if (response.success === true) {
            this.leaveRequests = response.requests;
          }
        })
        .catch((error) => console.error(error));
    },
    approveLeave(index) {
  const leaveRequest = this.leaveRequests[index];
  
  // Show confirmation message before sending the request
  Swal.fire({
    title: 'Are you sure?',
    text: 'You are about to approve this leave request',
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, approve it!'
  }).then((result) => {
    if (result.isConfirmed) {
      // Send the request if the user confirms
      fetch(`${import.meta.env.VITE_SERVER_URL}/approveRequest/`, {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          id: leaveRequest.id, // assuming that each leave request has a unique id
          status: "Approved",
        }),
      })
      .then((response) => response.json())
      .then((response) => {
        if (response.success === true) {
          this.leaveRequests[index].Status = "Approved";
          this.fetchLeaveRequests();
        }
      })
      .catch((error) => console.error(error));
    }
  })
}
  },
};
</script>
