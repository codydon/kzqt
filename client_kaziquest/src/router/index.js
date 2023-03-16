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
  // { path: "/addemployee", name: "AddEmployee", component: AddEmployee },
  // { path: "/updaterole", name: "UpdateRole", component: UpdateRole },
  // { path: "/inventory", name: "Inventory", component: Inventory },
  // { path: "/leavedetails", name: "LeaveDetails", component: LeaveDetails },
  { path: "/register", name: "register", component: Register },
  { path: "/login", name: "Login", component: Login },
  // { path: "/admin", name: "AdminDash", component: AdminDash },
  //
  // { path: "/employee", name: "AdminDash", component: EmployeeDash },
  // { path: "/assets", name: "Assets", component: Assets },
  // { path: "/request_leave", name: "RequestLeave", component: RequestLeave },
  // { path: "/Update_profile", name: "UpdateProfile", component: UpdateProfile },
  {
    path: "/verify_email/:tkn",
    name: "VerifyEmail",
    component: VerifyEmail,
  },
  //
  // { path: "/dummy", name: "Dummy", component: Dummy },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
