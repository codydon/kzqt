<template>
  <div class="flex flex-col items-center justify-center bg-gray-200">
    <h1 class="text-3xl font-bold mb-4">Assign Asset</h1>
    <div class="w-full max-w-md bg-white rounded-lg shadow-lg overflow-hidden p-10">
      <div class="px-6 py-4">
        <div class="mb-4">
          <label class="block text-gray-700 font-bold mb-2" for="employee">
            Employee
          </label>
          <div class="relative">
            <select
              class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-2 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              v-model="selectedEmployee"
              @change="updateSelectedAsset()"
            >
              <option value="" disabled>Select an employee</option>
              <option
                v-for="(employee, index) in employees"
                :key="index"
                :value="employee.EmployeeId"
              >
                {{ employee.Name }}
              </option>
            </select>
            <div
              class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
            >
              <svg
                class="fill-current h-4 w-4"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 20 20"
              >
                <path d="M10 12a2 2 0 100-4 2 2 0 000 4z" />
                <path
                  fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-10 3a3 3 0 016 0h-2a1 1 0 00-2 0h-2zM9 6a1 1 0 012 0v2.17a1 1 0 00.53.88l1.74 1a1 1 0 01.27 1.4l-1.42 2a1 1 0 01-1.64 0l-1.42-2a1 1 0 01.27-1.4l1.74-1a1 1 0 00.53-.88V6z"
                  clip-rule="evenodd"
                />
              </svg>
            </div>
          </div>
        </div>
        <div class="mb-4">
          <table class="w-full border-collapse table-auto">
            <thead>
              <tr>
                <th class="border py-2 px-3">Asset ID</th>
                <th class="border py-2 px-3">Asset Name</th>
                <th class="border py-2 px-3">Assign</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(asset, index) in assets" :key="index">
                <td class="border py-2 px-3">{{ asset.id }}</td>
                <td class="border py-2 px-3">{{ asset.name }}</td>
                <td class="border py-2 px-3">
<input
type="checkbox"
:id="'asset-'+index"
:value="asset.id"
v-model="selectedAssets"
@change="updateSelectedAsset()"
/>
<label :for="'asset-'+index" class="ml-2">{{ asset.name }}</label>
</td>
</tr>
</tbody>
</table>
</div>
<div class="flex justify-end">
<button
class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
:disabled="!selectedAssets.length"
@click="assignAsset()"
>
Assign Asset
</button>
</div>
</div>
</div>

  </div>
</template>
<script>
export default {
  data() {
    return {
      employees: [],
      assets: [],
      selectedEmployee: "",
      selectedAssets: [],
    };
  },
  methods: {
    fetchEmployees() {
      // fetch the list of employees from the server and set the data to the employees array
      // use axios library to make a GET request to the server API endpoint '/employees'
      // then set the response data to the employees array
      axios
        .get("/employees")
        .then((response) => {
          this.employees = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    fetchAssets() {
      // fetch the list of assets from the server and set the data to the assets array
      // use axios library to make a GET request to the server API endpoint '/assets'
      // then set the response data to the assets array
      axios
        .get("/assets")
        .then((response) => {
          this.assets = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    updateSelectedAsset() {
      // filter the selected assets based on the selected employee
      // use axios library to make a GET request to the server API endpoint '/assets?employee_id=<selectedEmployee>'
      // then set the response data to the assets array
      axios
        .get(`/assets?employee_id=${this.selectedEmployee}`)
        .then((response) => {
          this.assets = response.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    assignAsset() {
      // make a POST request to the server API endpoint '/assets/assign' with selectedEmployee and selectedAssets data
      axios
        .post("/assets/assign", {
          employee_id: this.selectedEmployee,
          asset_ids: this.selectedAssets,
        })
        .then((response) => {
          console.log(response.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
  mounted() {
    // fetch the employees and assets data when the component is mounted
    this.fetchEmployees();
    this.fetchAssets();
  },
};
</script>