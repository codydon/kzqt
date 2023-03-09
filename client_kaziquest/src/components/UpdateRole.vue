<template>
  <div class="p-4">
    <table class="table-auto border w-full">
      <thead>
        <tr>
          <th class="px-4 py-2">EmployeeID</th>
          <th class="px-4 py-2">Name</th>
          <th class="px-4 py-2">Role</th>
          <th class="px-4 py-2">Change Role</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(employee, index) in employees" :key="employee.id">
          <td class="border px-4 py-2">{{ employee.id }}</td>
          <td class="border px-4 py-2">{{ employee.name }}</td>
          <td class="border px-4 py-2">{{ employee.role }}</td>
          <td class="border px-4 py-2">
            <button
              class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
              @click="openRolePopup(index)"
            >
              Change Role
            </button>
          </td>
        </tr>
      </tbody>
    </table>

    <!-- Role popup -->
    <div
      v-if="selectedEmployee !== null"
      class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center"
    >
      <div class="bg-white p-6 rounded-lg">
        <div class="text-red-500 text-right pb-4 cursor-pointer font-bold" @click="selectedEmployee = null">
          X
        </div>
        <h2 class="text-lg font-bold mb-4">
          Select a new role for {{ selectedEmployee.name }}
        </h2>
        <ul>
          <li
            v-for="(role, index) in roles"
            :key="index"
            class="cursor-pointer py-2 hover:bg-gray-200"
            @click="changeRole(role)"
          >
            {{ role }}
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      employees: [
        { id: 1, name: "John Doe", role: "Manager" },
        { id: 2, name: "Jane Doe", role: "Developer" },
        { id: 3, name: "Bob Smith", role: "Designer" },
      ],
      roles: ["Manager", "Developer", "Designer", "QA"],
      selectedEmployee: null,
    };
  },
  methods: {
    openRolePopup(index) {
      this.selectedEmployee = this.employees[index];
    },
    changeRole(newRole) {
      this.selectedEmployee.role = newRole;
      this.selectedEmployee = null;
    },
  },
};
</script>

<style>
/* Ant Design styles for role popup */
li:hover {
  background-color: #e6f7ff;
}

li:active {
  background-color: #bae7ff;
}
</style>
