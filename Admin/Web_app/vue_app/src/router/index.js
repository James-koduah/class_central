import { createRouter, createWebHistory } from 'vue-router';
import DashboardPage from '@/components/pages/dashboard/DashboardPage.vue';


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL || '/'),
    routes: [
        {
            path: '/',
            name: 'Dashboard',
            component: DashboardPage
        },
    ]
})

export default router