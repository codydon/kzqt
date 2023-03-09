import { createRouter, createWebHistory } from 'vue-router'
// import HomeView from '../views/HomeView.vue'
import AddEmployee from '../components/AddEmployee.vue'
import UpdateRole from '../components/UpdateRole.vue'
import Inventory from "../components/Inventory.vue";
import LeaveDetails from "../components/LeaveDetails.vue";
import AssignAsset from "../components/AssignAsset.vue";
import AdminDashboard from "../components/AdminDash.vue";
import VerifyEmail from "../components/VerifyEmail.vue";
// import VerifyEmailLayout from "../layouts/VerifyEmailLayout.vue";


const routes = [
    { path: '/', redirect: '/AdminDashboard' },
    { path: '/addemployee',  name:'AddEmployee', component: AddEmployee  },
    { path: '/assign_asset', name:'AssignAsset', component: AssignAsset },
    { path: '/updaterole', name:'UpdateRole', component: UpdateRole },
    { path: '/inventory', name:'Inventory', component: Inventory },
    { path: '/leavedetails', name:'LeaveDetails', component: LeaveDetails },
    { path: '/admin', name:'AdminDashboard', component: AdminDashboard },
    { 
      path: '/verify_email/:token', 
      name:'VerifyEmail', 
      component: VerifyEmail,
      // meta: { layout: VerifyEmailLayout }
    },
  ]


const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
