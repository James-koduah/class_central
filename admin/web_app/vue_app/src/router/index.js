import { createRouter, createWebHistory } from 'vue-router';
import DashboardPage from '@/components/pages/dashboard/DashboardPage.vue';
import ClassroomMain from '@/components/pages/classrooms/ClassroomMain.vue';
import TeachersMain from '@/components/pages/teachers/teachersMain.vue';
import StudentsMain from '@/components/pages/students/StudentsMain.vue';


const router = createRouter({
    history: createWebHistory(process.env.BASE_URL || '/'),
    routes: [
        {
            path: '/',
            name: 'Dashboard',
            component: DashboardPage
        },
        {
            path: '/classrooms',
            name: "ClassroomMain",
            component: ClassroomMain
        },
        {
            path: '/teachers',
            name: "TeachersMain",
            component: TeachersMain
        },
        {
            path: '/students',
            name: "StudentsMain",
            component: StudentsMain
        }
    ]
})

export default router