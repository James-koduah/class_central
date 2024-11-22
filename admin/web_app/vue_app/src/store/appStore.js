import apiClient from '@/axios';
import { defineStore } from 'pinia';


export const useAppStore = defineStore('appStore', {
  state: () => ({
    classrooms: false,
    teachers: false,
    students: false
  }),

  actions: {
    async fetchClassrooms(){
      const response = await apiClient.get('/classrooms')
      if (response.data.status){
        this.classrooms = response.data.data
      }else{
        console.log(response.data)
        this.classrooms = false
      }
      return this.classrooms
    },
    findClassroom(id){
      return this.classrooms.find(classroom => classroom.id === id)
    },
    classroomSearch(query = '') {
      if (query === '' || !this.classrooms) return []
      query = query.toLowerCase()
      let res = this.classrooms.filter(item => item.name.toLowerCase().includes(query))
      .map(item => {
          const searchDisplayText = item.name.replace(
              new RegExp(`(${query})`, 'gi'),
              '<mark>$1</mark>'
          );
          return {
              ...item,
              searchDisplayText,
              searchValue: item.id
          };
      });
      return res
    },

    async fetchTeachers(){
      const response = await apiClient.get('/teachers')
      if (response.data.status){
        this.teachers = response.data.data
      }else{
        console.log(response.data)
        this.teachers = false
      }
      return this.teachers
    },
    findTeacher(id){
      return this.teachers.find(teacher => teacher.id === id)
    },
    teachersSearch(query = '') {
      if (query === '' || !this.teachers) return []
      query = query.toLowerCase()
      let res = this.teachers.filter(item => item.name.toLowerCase().includes(query))
      .map(item => {
          const searchDisplayText = item.name.replace(
              new RegExp(`(${query})`, 'gi'),
              '<mark>$1</mark>'
          );
          return {
              ...item,
              searchDisplayText,
              searchValue: item.id
          };
      });
      return res
    },

    async fetchStudents(){
      const response = await apiClient.get('/students')
      if (response.data.status){
        this.students = response.data.data
      }else{
        console.log(response.data)
        this.students = false
      }
      return this.students
    },
    findStudent(id){
      return this.students.find(student => student.id === id)
    },
    studentsSearch(query = '') {
      if (query === '' || !this.students) return []
      query = query.toLowerCase()
      let res = this.students.filter(item => item.name.toLowerCase().includes(query))
      .map(item => {
          const searchDisplayText = item.name.replace(
              new RegExp(`(${query})`, 'gi'),
              '<mark>$1</mark>'
          );
          return {
              ...item,
              searchDisplayText,
              searchValue: item.id
          };
      });
      return res
    },

  },

  getters: {
    getClassrooms: (state) => state.classrooms,
    getTeachers: (state) => state.teachers,
    getStudents: (state) => state.students,
  },

});