import { createRouter, createWebHistory } from "vue-router";
import AddEmployee from "../components/AddEmployee.vue";
import UpdateRole from "../components/UpdateRole.vue";
import Inventory from "../components/Inventory.vue";
import LeaveDetails from "../components/LeaveDetails.vue";
import AdminDash from "../components/AdminDash.vue";
import VerifyEmail from "../components/VerifyEmail.vue";
import EmployeeDash from "../components/employee/EmployeeDash.vue";
import Assets from "../components/employee/Assets.vue";
import RequestLeave from "../components/employee/RequestLeave.vue";
import UpdateProfile from "../components/employee/UpdateProfile.vue";
import Register from "../components/Register.vue";
import Login from "../components/Login.vue";
import Dummy from "../components/Dummy.vue";

const routes = [
  { path: "/", redirect: "/login" },
  { path: "/register", name: "Register", component: Register },
  { path: "/login", name: "Login", component: Login },
  {
    path: "/verify_email/:tkn",
    name: "VerifyEmail",
    component: VerifyEmail,
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
