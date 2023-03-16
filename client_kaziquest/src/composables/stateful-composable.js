import { reactive } from "vue";

const globalState = reactive({
  someString: "Initial value",
  someBoolean: false
});

export const useStatefulComposable = () => {
  const localState = reactive({
    someString: "Initial value",
    someBoolean: false
  });

  const updateValues = (sValue, bValue) => {
    // Set the global state values
    globalState.someString = sValue;
    globalState.someBoolean = bValue;

    // Set the local state values
    localState.someString = sValue;
    localState.someBoolean = bValue;
  };

  return {
    globalState,
    localState,
    updateValues
  };
};