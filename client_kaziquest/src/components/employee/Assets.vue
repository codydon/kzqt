<template>
  <div class="flex flex-col items-center">
    <h1 class="text-3xl font-bold mb-6">My Assets</h1>
    <table class="border-collapse border border-gray-400">
      <thead>
        <tr>
          <th class="border border-gray-400 px-4 py-2">Asset</th>
          <th class="border border-gray-400 px-4 py-2">AssetID</th>
          <th class="border border-gray-400 px-4 py-2">Date Issued</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(asset, index) in assets" :key="index" @click="handleAssetClick(asset)">
          <td class="border border-gray-400 px-4 py-2 cursor-pointer hover:bg-gray-100">{{ asset.name }}</td>
          <td class="border border-gray-400 px-4 py-2 cursor-pointer hover:bg-gray-100">{{ asset.id }}</td>
          <td class="border border-gray-400 px-4 py-2 cursor-pointer hover:bg-gray-100">{{ asset.date_issued }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      assets: [],
    };
  },
  methods: {
    async fetchAssets() {
      const response = await axios.get('/api/assets/');
      this.assets = response.data;
    },
    handleAssetClick(asset) {
      // handle click event on an asset row
      console.log('Clicked asset:', asset);
    },
  },
  mounted() {
    this.fetchAssets();
  },
};
</script>

