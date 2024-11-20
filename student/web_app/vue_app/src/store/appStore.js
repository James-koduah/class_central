import { defineStore } from 'pinia';


export const useAppStore = defineStore('appStore', {
  state: () => ({
    something: []
  }),

  actions: {
    getDate() {
      const date = new Date();

      const days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
      const months = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
      ];

      const dayOfWeek = days[date.getDay()];
      const dayOfMonth = date.getDate();
      const month = months[date.getMonth()];
      const year = date.getFullYear();

      // Function to get the ordinal suffix (e.g., "st", "nd", "rd", "th")
      const getOrdinalSuffix = (day) => {
        if (day > 3 && day < 21) return "th"; // 11th to 19th are exceptions
        switch (day % 10) {
          case 1: return "st";
          case 2: return "nd";
          case 3: return "rd";
          default: return "th";
        }
      };
      const ordinalSuffix = getOrdinalSuffix(dayOfMonth);
      return `${dayOfWeek} ${dayOfMonth}${ordinalSuffix} ${month}, ${year}`;
    }
  },

  getters: {

  },

});