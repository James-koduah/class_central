import { createRouter, createWebHistory } from 'vue-router';
import DashboardPage from '@/components/pages/dashboard/DashboardPage.vue';
import CoursesPage from '@/components/pages/courses/CoursesPage.vue';


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL || '/'),
    routes: [
        {
            path: '/',
            name: 'Dashboard',
            component: DashboardPage
        },
        {
            path: '/courses',
            name: 'Courses',
            component: CoursesPage
        }
    ]
})

export default router