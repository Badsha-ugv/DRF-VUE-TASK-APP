import { createStore } from 'vuex'

export default createStore({
  state: {
    token: '',
    isAuthenticated:''
  },
  getters: {
  },
  mutations: {
    initToken(state) {
      let token = localStorage.getItem('token')
      if (token) {
        state.isAuthenticated = true;
        state.token = token 
      } else {
        state.isAuthenticated = false
        state.token = '' 
        localStorage.removeItem('token') 
      }
    },
    setToken(state, token) {
      state.token = token 
      localStorage.setItem("token", token);
      state.isAuthenticated = true 
    },
    removeToken(state) {
      localStorage.removeItem("token");
      state.token = '';
      state.isAuthenticated = false;
      
    }
  },
  actions: {
  },
  modules: {
  }
})
