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
          <td class="border px-4 py-2">{{ employee.employee_id }}</td>
          <td class="border px-4 py-2">{{ employee.employee_name }}</td>
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
      v-if="showChangeRole"
      class="fixed inset-0 bg-gray-500 bg-opacity-75 flex items-center justify-center"
    >
      <div class="bg-white p-6 rounded-lg">
        <div
          class="text-red-500 text-right pb-4 cursor-pointer font-bold"
          @click="showChangeRole = false"
        >
          X
        </div>
        <h2 class="text-lg font-bold mb-4">
          Select a new role for {{ selectedEmployee.employee_name }}
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
import Swal from 'sweetalert2'

export default {
  data() {
    return {
      employees: [

      ],
      roles: ["Manager", "Developer", "Designer", "QA"],
      selectedEmployee: null,
      showChangeRole:false,
      selectedEid:"",
      selectedRole:""
    };
  },
  created() {
    this.getEmployees()
  },
  methods: {
    getEmployees() {
      fetch(`${import.meta.env.VITE_SERVER_URL}/get_employees/`)
        .then((response) => response.json())
        .then((response) => {
          if (response.success === true) {
            this.employees = response.employees;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    openRolePopup(index) {
      this.selectedEmployee = this.employees[index];
      this.showChangeRole = true;

    },
    changeRole(newRole) {
  const selectedEmployee = this.selectedEmployee;
  const selectedEid = selectedEmployee.employee_id;
  
  // Show a confirmation dialog before updating the role
  Swal.fire({
    title: 'Are you sure?',
    text: `Do you want to change ${selectedEmployee.name}'s role to ${newRole}?`,
    icon: 'warning',
    showCancelButton: true,
    confirmButtonColor: '#3085d6',
    cancelButtonColor: '#d33',
    confirmButtonText: 'Yes, change role',
  }).then((result) => {
    if (result.isConfirmed) {
      const url = `${import.meta.env.VITE_SERVER_URL}/change_employee_role/${selectedEid}/`;
      const options = {
        method: "PUT",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ role: newRole }),
      };
      fetch(url, options)
        .then((response) => response.json())
        .then((response) => {
          if (response.success === true) {
            this.showChangeRole = false;
            this.getEmployees();
            Swal.fire({
              title: "Success",
              text: "Role has been updated!",
              icon: "success",
              timer: 1500,
            });
          }
        })
        .catch((error) => {
          console.error("PUT ERROR", error);
        });
      this.selectedEmployee = null;
    }
  });
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
