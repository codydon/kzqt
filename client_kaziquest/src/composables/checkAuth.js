import { reactive, ref } from "vue";

// const globalState = reactive({
//   someString: "Initial value",
//   someBoolean: false
// });

// export const useStatefulComposable = () => {
//   const localState = reactive({
//     someString: "Initial value",
//     someBoolean: false
//   });

//   const updateValues = (sValue, bValue) => {
//     // Set the global state values
//     globalState.someString = sValue;
//     globalState.someBoolean = bValue;

//     // Set the local state values
//     localState.someString = sValue;
//     localState.someBoolean = bValue;
//   };

//   return {
//     globalState,
//     localState,
//     updateValues
//   };
// };

const authUser = reactive({
    empId: "",
    empName: "",
    empEmail: "",
    empRole: "",
});

const isLoggedIn = ref(false);

export const checkauth = () => {

    // get tkn from local storage
    const token = localStorage.getItem("token");
    //send a POST request to the server
    fetch(`${import.meta.env.VITE_SERVER_URL}/getauth`, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            // "Authorization": `Bearer ${token}`
        },
        body:JSON.stringify({
            tkn: token
        })
    })
    .then((res) => res.json())
    .then((res) => {
        if (res.success === true) {
            isLoggedIn.value = true;
            authUser.empId = res.user.EmployeeId;
            authUser.empName = res.user.Name;
            authUser.empEmail = res.user.email;
            authUser.empRole = res.user.Role
    }
    else {
        isLoggedIn.value = false;
        authUser.empId = "";
        authUser.empName = "";
        authUser.empEmail = "";
        authUser.empRole = "";
    }
});

    
    

    return authUser, isLoggedIn, checkauth;
};
    