import apiClient from '@/axios';
import { defineStore } from 'pinia';


export const useAppStore = defineStore('appStore', {
  state: () => ({
    classrooms: false
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
    }

  },

  getters: {
    getClassrooms: (state) => state.classrooms
  },

});