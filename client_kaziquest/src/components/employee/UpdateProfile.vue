<template>
  <div v-if="employee" class="max-w-md mx-auto">
    <h1 class="text-3xl font-bold mb-6">Update Employee Info</h1>
    <form @submit.prevent="handleSubmit">
      <div v-for="(input, label) in inputs" :key="label" class="mb-4">
        <label class="block text-gray-700 font-bold mb-2" :for="label">{{ label }}</label>
        <input
          v-model="employee[input]"
          class="bg-gray-200 appearance-none border-2 border-gray-200 rounded w-full py-2 px-4 leading-tight focus:outline-none focus:bg-white focus:border-blue-500"
          :id="label"
          :type="inputType[input]"
          :required="isRequired(input)"
          :readonly="isReadonly(input)"
        />
      </div>
      <button
        type="submit"
        class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
      >
        Update
      </button>
    </form>
  </div>
  <div v-else>
    Loading...
  </div>
</template>
<script>
export default {
  props: {
    employee: {
      type: Object,
      required: true,
    },
  },
  data() {
    return {
      inputs: {
        Name: "Name",
        Email: "Email",
        PhoneNumber: "Phone Number",
        dob: "Date of Birth",
        

      },
      inputType: {
        Email: "email",
        PhoneNumber: "tel",
        EmployeeId: "text",
      },
    };
  },
  methods: {
    handleSubmit() {
      // TODO: Implement submission logic
    },
    isRequired(input) {
      return input !== "EmployeeId";
    },
    isReadonly(input) {
      return input === "EmployeeId";
    },
  },
};
</script>
