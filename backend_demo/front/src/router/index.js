import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import DeviceView from '../views/DeviceView.vue'
import AddDeviceView from '../views/AddDeviceView.vue'
import AddLocationView from '../views/AddLocationView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: () => import('../views/AboutView.vue')
  }, 
  {
    path: '/:slug/',
    name: 'device',
    component: DeviceView
  },
  {
    path: '/devices/',
    name: 'device',
    component: AddDeviceView
  },
  {
    path: '/locations/',
    name: 'location',
    component: AddLocationView
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
