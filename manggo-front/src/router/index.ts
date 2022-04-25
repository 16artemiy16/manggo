import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router'
import Connection from '@/views/Connection.vue';

const routes: Array<RouteRecordRaw> = [
  {
    path: '/',
    name: 'Connection',
    component: Connection
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
