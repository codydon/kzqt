<template>
  <div class="bg-gray-200 min-h-screen p-8 h-64 overflow-y-auto">
    <h1 class="text-3xl font-bold mb-8 text-center">Inventory</h1>
    <div class="flex mb-4">
      <!-- <input
        type="text"
        placeholder="Search"
        class="w-2/3 p-2 border border-gray-300 rounded-l-lg focus:outline-none focus:ring focus:border-blue-300"
      /> -->
      <!-- <button
        class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-r-lg"
        @click="resetSearch"
      >
        X
      </button> -->
    </div>
    <button
      class="px-4 py-2 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded-lg"
      @click="showAddAssetModal = true"
    >
      Add Asset
    </button>
    <div class="flex justify-center gap-4 mb-4"></div>
    <!-- <template> -->
    <div class="overflow-x-auto overflow-scroll">
      <table class="table-auto w-full border-collapse border border-gray-300">
        <thead>
          <tr
            class="bg-gray-200 text-gray-600 uppercase text-sm leading-normal"
          >
            <th
              class="py-3 px-6 text-left cursor-pointer border"
              @click="sortBy('id')"
            >
              Asset ID
            </th>
            <th
              class="py-3 px-6 text-left cursor-pointer border"
              @click="sortBy('name')"
            >
              Asset Name
            </th>
            <th
              class="py-3 px-6 text-left cursor-pointer border"
              @click="sortBy('assignedTo')"
            >
              Assigned To
            </th>
            <th
              class="py-3 px-6 text-left cursor-pointer border"
              @click="sortBy('description')"
            >
              Description
            </th>
            <th
              class="py-3 px-6 text-left cursor-pointer border"
              @click="sortBy('assigned')"
            >
              Assigned
            </th>
            <th class="py-3 px-6 text-center border">Actions</th>
          </tr>
        </thead>
        <tbody class="text-gray-600 text-sm font-light">
          <tr
            v-for="asset in assets"
            :key="asset.id"
            class="border-b border-gray-200 hover:bg-gray-100"
          >
            <td class="py-3 px-6 text-left border">{{ asset.asset_id }}</td>
            <td class="py-3 px-6 text-left border">{{ asset.asset_name }}</td>
            <td class="py-3 px-6 text-left border">{{ asset.employeeId }}</td>
            <td class="py-3 px-6 text-left border">{{ asset.description }}</td>
            <td class="py-3 px-6 text-left border">
              {{ asset.assigned_status }}
            </td>
            <td class="py-3 px-6 text-center border">
              <div class="flex justify-center items-center space-x-2">
                <button
                  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  @click="showAssign(asset)"
                >
                  Assign
                </button>
                <button
                  class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  @click="showEditAssetModal(asset)"
                >
                  Edit
                </button>
                <button
                  class="bg-red-500 hover:bg-red-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                  @click="deleteAsset(asset)"
                >
                  Delete
                </button>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <div
      v-if="showAssignModal"
      class="fixed inset-0 bg-gray-500 bg-opacity-75 flex justify-center items-center"
    >
      <div class="bg-white p-8 rounded-lg">
        <h2 class="text-xl font-bold mb-4">Assign Asset</h2>
        <form @submit.prevent="assignAsset()">
          <div class="pb-5">
            <select
              class="block appearance-none w-full bg-gray-200 border border-gray-200 text-gray-700 py-2 px-4 pr-8 rounded leading-tight focus:outline-none focus:bg-white focus:border-gray-500"
              v-model="selectedEmployee"
              required
            >
              <option value="" disabled>Select an employee</option>
              <option
                v-for="employee in employees"
                :key="employee.employee_id"
                :value="employee.employee_id"
              >
                {{ employee.employee_name }} - {{ employee.employee_id }}
              </option>
            </select>
            <div
              class="pointer-events-none absolute inset-y-0 right-0 flex items-center px-2 text-gray-700"
            ></div>
          </div>
          <div class="flex justify-end">
            <button
              type="button"
              class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-lg mr-2"
              @click="showAssignModal = false"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="px-4 py-2 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded-lg"
            >
              Assign
            </button>
          </div>
        </form>
      </div>
    </div>

    <div
      v-if="showAddAssetModal"
      class="fixed inset-0 bg-gray-500 bg-opacity-75 flex justify-center items-center"
    >
      <div class="bg-white p-8 rounded-lg">
        <h2 class="text-xl font-bold mb-4">Add Asset</h2>
        <form @submit.prevent="addAsset">
          <!-- <input type="hidden" name="csrfmiddlewaretoken" :value="csrfToken" /> -->
          <div class="mb-4">
            <label for="asset-name" class="block font-bold mb-2"
              >Asset Name</label
            >
            <input
              type="text"
              id="asset-name"
              v-model="newAsset.name"
              required
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:border-blue-300"
            />
          </div>
          <div class="mb-4">
            <label for="asset-name" class="block font-bold mb-2"
              >Asset ID</label
            >
            <input
              type="text"
              id="asset-id"
              v-model="newAsset.id"
              required
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:border-blue-300"
            />
          </div>

          <div class="mb-4">
            <label for="asset-description" class="block font-bold mb-2"
              >Description</label
            >
            <textarea
              id="asset-description"
              v-model="newAsset.description"
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:border-blue-300"
            ></textarea>
          </div>

          <div class="flex justify-end">
            <button
              type="button"
              class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-lg mr-2"
              @click="showAddAssetModal = false"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="px-4 py-2 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded-lg"
            >
              Add Asset
            </button>
          </div>
        </form>
      </div>
    </div>

    <div
      v-if="showEditModal"
      class="fixed inset-0 bg-gray-500 bg-opacity-75 flex justify-center items-center"
    >
      <div class="bg-white p-8 rounded-lg">
        <h2 class="text-xl font-bold mb-4">Edit Asset</h2>
        <form @submit.prevent="updateAsset()">
          <div class="mb-4">
            <label for="asset-name" class="block font-bold mb-2">Name</label>
            <input
              type="text"
              id="asset-name"
              v-model="selectedAsset.asset_name"
              required
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:border-blue-300"
            />
          </div>
          <div class="mb-4">
            <label for="asset-description" class="block font-bold mb-2"
              >Description</label
            >
            <textarea
              id="asset-description"
              v-model="selectedAsset.description"
              class="w-full p-2 border border-gray-300 rounded-lg focus:outline-none focus:ring focus:border-blue-300"
            ></textarea>
          </div>
          <div class="flex justify-end">
            <button
              type="button"
              class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-lg mr-2"
              @click="showEditModal = false"
            >
              Cancel
            </button>
            <button
              type="submit"
              class="px-4 py-2 bg-blue-500 hover:bg-blue-700 text-white font-bold rounded-lg"
            >
              Update Asset
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>
<script>
// import axios from "axios";
import Swal from "sweetalert2";

export default {
  name: "AssetManager",
  data() {
    return {
      assets: [],
      filteredAssets: [],
      employees: [],
      sortColumn: "id",
      sortDirection: "asc",
      emp: {},
      searchTerm: "",
      showAddAssetModal: false,
      showEditModal: false,
      showAssignModal: false,
      newAsset: {
        name: "",
        id: "",
        description: "",
        assigned_status: "",
        eId: "",
      },
      selectedEmployee: "",
      selectedAsset: {},
    };
  },
  created() {
    this.getauth();
    this.getAssets();
  },

  computed: {
    sortedAssets() {
      return this.filteredAssets.sort((a, b) => {
        const sortColumn = this.sortColumn;
        const sortDirection = this.sortDirection === "asc" ? 1 : -1;
        const aVal = a[sortColumn];
        const bVal = b[sortColumn];
        if (aVal < bVal) {
          return -1 * sortDirection;
        } else if (aVal > bVal) {
          return 1 * sortDirection;
        } else {
          return 0;
        }
      });
    },
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
            this.emp = response.user;
          } else {
            this.$router.push({ name: "Login" });
          }
        });
    },
    getAssets() {
      fetch(`${import.meta.env.VITE_SERVER_URL}/get_assets/`)
        .then((response) => response.json())
        .then((response) => {
          if (response.success === true) {
            this.assets = response.assets;
          }
        })
        .catch((error) => {
          console.log(error);
        });
    },
    toggleSort(column) {
      if (this.sortColumn === column) {
        this.sortDirection = this.sortDirection === "asc" ? "desc" : "asc";
      } else {
        this.sortColumn = column;
        this.sortDirection = "asc";
      }
    },
    assignAsset() {
      console.log(this.selectedEmployee);
      this.selectedAsset.employee_id = this.selectedEmployee;
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.selectedAsset),
      };

      fetch(`${import.meta.env.VITE_SERVER_URL}/assign_asset/`, requestOptions)
        .then((response) => response.json())
        .then((response) => {
          console.log(response);
          if (response.success === true) {
            this.getAssets();
            this.selectedAsset = {};
            this.showAssignModal = false;
            Swal.fire({
              icon: "success",
              title: "Success",
              text: "Assigned successfully",
            });
          } else {
            Swal.fire({
              icon: "error",
              title: "Error",
              text: "Network error",
            });
          }
        })
        .catch((error) => {
          Swal.fire({
            icon: "error",
            title: "Error",
            text: error.message,
          });
        });
    },
    search() {
      this.filteredAssets = this.assets.filter((asset) =>
        asset.name.toLowerCase().includes(this.searchTerm.toLowerCase())
      );
    },
    resetSearch() {
      this.searchTerm = "";
      this.filteredAssets = this.assets;
    },
    showAddAssetModalFn() {
      this.showAddAssetModal = true;
      this.newAsset = {
        name: "",
        description: "",
        assignedTo: "",
      };
    },
    showEditAssetModal(asset) {
      this.selectedAsset = asset;
      this.showEditModal = true;
    },

    showAssign(asset) {
      this.selectedAsset = asset;
      this.getEmployees();
      this.showAssignModal = true;
    },
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
    toggleSort(column) {
      if (this.sortColumn === column) {
        this.sortDirection = this.sortDirection === "asc" ? "desc" : "asc";
      } else {
        this.sortColumn = column;
        this.sortDirection = "asc";
      }
    },
    addAsset() {
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.newAsset, this.employee),
      };

      fetch(`${import.meta.env.VITE_SERVER_URL}/add_asset/`, requestOptions)
        .then((response) => response.json())
        .then((response) => {
          console.log(response);
          if (response.success === true) {
            this.getAssets();
            this.newAsset = {};
            this.showAddAssetModal = false;
            Swal.fire({
              icon: "success",
              title: "Success",
              text: "Asset added successfully",
            });
          } else {
            Swal.fire({
              icon: "error",
              title: "Error",
              text: "Network error",
            });
          }
        })
        .catch((error) => {
          Swal.fire({
            icon: "error",
            title: "Error",
            text: error.message,
          });
        });
    },
    updateAsset() {
      const requestOptions = {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(this.selectedAsset),
      };

      fetch(`${import.meta.env.VITE_SERVER_URL}/update_asset/`, requestOptions)
        .then((response) => response.json())
        .then((response) => {
          if (response.success === true) {
            console.log(response.resp);
            this.getAssets();
            this.selectedAsset = {};
            this.showEditModal = false;
            this.getAssets();
            Swal.fire({
              icon: "success",
              title: "Success",
              text: "Asset updated successfully",
            });
          } else {
            this.selectedAsset = {};
            this.showEditModal = false;
            Swal.fire({
              icon: "error",
              title: "Error",
              text: "Network error",
            });
          }
        })
        .catch((error) => {
          Swal.fire({
            icon: "error",
            title: "Error",
            text: error.message,
          });
        });
    },
    deleteAsset(asset) {
      this.selectedAsset = asset;

      Swal.fire({
        title: "Are you sure you want to delete this asset?",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Yes, delete it!",
      }).then((result) => {
        if (result.isConfirmed) {
          const requestOptions = {
            method: "DELETE",
          };
          fetch(
            `${import.meta.env.VITE_SERVER_URL}/delete_asset/${this.selectedAsset.asset_id}/`,
            requestOptions
          )
            .then((response) => response.json())
            .then((response) => {
              console.log(response.resp);
              if (response.success === true) {
                this.getAssets();
                this.selectedAsset = {};
                this.showEditModal = false;
                this.getAssets();
                Swal.fire({
                  icon: "success",
                  title: "Success",
                  text: "Asset deleted successfully",
                });
              } else {
                this.selectedAsset = {};
                this.showEditModal = false;
                this.getAssets();
                Swal.fire({
                  icon: "error",
                  title: "Error",
                  text: "Network error",
                });
              }
            })
            .catch((error) => {
              this.getAssets();
              Swal.fire({
                icon: "error",
                title: "Error",
                text: error.message,
              });
            });
        }
      });
    },
  },
};
</script>
