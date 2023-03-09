<template>
  <div class="bg-gray-200 min-h-screen p-8">
    <h1 class="text-3xl font-bold mb-8">Assets</h1>
    <div class="flex mb-4">
      <input type="text" v-model="searchQuery" placeholder="Search" class="w-2/3 p-2 border border-gray-300 rounded-l-lg focus:outline-none focus:ring focus:border-blue-300">
      <button class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-r-lg" @click="searchQuery=''">Clear</button>
    </div>
    <div class="flex justify-between mb-4">
      <button class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-lg" :class="{'bg-gray-700 text-white': filter === 'all'}" @click="filter='all'">All</button>
      <button class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-lg" :class="{'bg-gray-700 text-white': filter === 'assigned'}" @click="filter='assigned'">Assigned</button>
      <button class="px-4 py-2 bg-gray-300 text-gray-700 font-semibold rounded-lg" :class="{'bg-gray-700 text-white': filter === 'unassigned'}" @click="filter='unassigned'">Unassigned</button>
    </div>
    <table class="w-full border-collapse table-auto">
      <thead>
        <tr>
          <th class="border p-3 cursor-pointer" @click="sortBy('id')">Asset ID</th>
          <th class="border p-3 cursor-pointer" @click="sortBy('name')">Asset Name</th>
          <th class="border p-3 cursor-pointer" @click="sortBy('assignedTo')">Assigned To</th>
          <th class="border p-3 cursor-pointer" @click="sortBy('description')">Description</th>
          <th class="border p-3 cursor-pointer" @click="sortBy('assigned')">Assigned</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(asset, index) in filteredAssets" :key="index">
          <td class="border p-3">{{ asset.id }}</td>
          <td class="border p-3">{{ asset.name }}</td>
          <td class="border p-3">{{ asset.assignedTo }}</td>
          <td class="border p-3">{{ asset.description }}</td>
          <td class="border p-3 rounded-lg font-bold" :class="{ 'text-red-600 bg-gray-300': asset.assigned, 'text-green-600 bg-gray-100': !asset.assigned }">
            {{ asset.assigned ? 'Yes' : 'No' }}
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
      assets: [
        {
          id: 1,
          name: 'Laptop',
          assignedTo: 'John Doe',
          description: 'MacBook Pro',
          assigned: true,
        },
        {
          id: 2,
          name: 'Monitor',
          assignedTo: null,
          description: 'Dell Ultrasharp',
          assigned: false,
        },
        {
          id: 3,
          name: 'Desk',
          assignedTo: 'don',
          description: 'Adjustable height',
          assigned: true,
        },
      ],
    };
  },
};
</script>
