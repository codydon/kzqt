import { reactive } from 'vue';


const authState = reactive({
    isLoggedIn: false,
    user: null
});


function checkauth() {
    fetch(`${import.meta.env.VITE_SERVER_URL}/getauth/`, {
        headers: { "content-type": "application/json" },
        // credentials: "include",
    })
        .then((response) => response.json())
        .then((response) => {
            if (response.success === true) {
                authState.isLoggedIn = true;
                authState.user = response.user;
            }
            else {
                authState.isLoggedIn = false;
                authState.user = 'yyyyyyyyyyyy';
            }
        });
}

function logout() {
   //send post request to server

    fetch(`${import.meta.env.VITE_SERVER_URL}/logout/`, {
        headers: { "content-type": "application/json" },
        // credentials: "include",
    })
      .then((response) => response.json())
      .then((response) => {
            if (response.success === true) {
                authState.isLoggedIn = false;
                authState.user = null;
            }
        });
}

export function useAuth() {
    return {
        authState,
        checkauth,
        logout
    }
}