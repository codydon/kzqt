<template>
  <div class="bg-white rounded-lg shadow overflow-x-auto">
    <table class="min-w-full divide-y divide-gray-200">
      <thead class="bg-gray-50">
        <tr>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Employee ID
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Start Date
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            End Date
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Description
          </th>
          <th scope="col" class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">
            Status
          </th>
        </tr>
      </thead>
      <tbody class="bg-white divide-y divide-gray-200">
        <tr v-for="(row, index) in leaveRequests" :key="index">
          <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">
            {{ row.EmployeeId }}
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
            <button v-if="row.Status === 'Pending'" @click="approveLeave(index)" class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
              Approve
            </button>
            <span v-else-if="row.Status === 'Approved'" class="text-green-500 font-bold">{{ row.Status }}</span>
            <span v-else class="text-red-500 font-bold">{{ row.Status }}</span>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
export default {
  data() {
    return {
      leaveRequests: [],
    }
  },
  mounted() {
    this.fetchLeaveRequests();
  },
  methods: {
    fetchLeaveRequests() {
      fetch('/api/leave_requests')
        .then(response => response.json())
        .then(data => this.leaveRequests = data)
        .catch(error => console.error(error));
    },
    approveLeave(index) {
      // Update the status of the leave request at the specified index
      this.leaveRequests[index].Status = 'Approved';
    }
  },
};
</script>

<style>
  /* Optional additional styling can be added here */
</style>
