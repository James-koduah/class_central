import axios from 'axios';
let base_url = process.env.VUE_APP_API_URL
const apiClient = axios.create({
  baseURL: base_url,
  headers: {
    "Content-Type": 'application/json'
  }
});
export default apiClient;