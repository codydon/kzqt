<template>
  <form class="bg-gray-200 p-6 rounded-lg">
    <h2 class="text-2xl font-bold mb-6">Employer Sign Up</h2>

    <div class="mb-4">
      <label for="name" class="block font-medium text-gray-700">Name:</label>
      <input
        type="text"
        id="name"
        name="name"
        required
        class="border border-gray-400 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
      />
    </div>

    <div class="mb-4">
      <label for="role" class="block font-medium text-gray-700">Role:</label>
      <input
        type="text"
        id="role"
        name="role"
        required
        class="border border-gray-400 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
      />
    </div>

    <div class="mb-4">
      <label for="company" class="block font-medium text-gray-700"
        >Company:</label
      >
      <input
        type="text"
        id="company"
        name="company"
        required
        class="border border-gray-400 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
      />
    </div>

    <div class="mb-4">
      <label for="email" class="block font-medium text-gray-700">Email:</label>
      <input
        type="email"
        id="email"
        name="email"
        required
        class="border border-gray-400 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
      />
    </div>

    <div class="mb-4">
      <label for="phonenumber" class="block font-medium text-gray-700"
        >Phone Number:</label
      >
      <input
        type="tel"
        id="phonenumber"
        name="phonenumber"
        required
        class="border border-gray-400 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
      />
    </div>

    <div class="mb-4">
      <label for="numemployees" class="block font-medium text-gray-700"
        >Number of Employees:</label
      >
      <input
        type="number"
        id="numemployees"
        name="numemployees"
        min="0"
        required
        class="border border-gray-400 rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:border-blue-500"
      />
    </div>

    <div class="flex justify-end">
      <input
        type="submit"
        value="Submit"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      />
    </div>
  </form>
</template>

<script lang="js">
export default {

}
</script>

<style>
</style>