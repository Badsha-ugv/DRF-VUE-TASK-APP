<template>
  
  <router-view/>
</template>


<script>
import axios from 'axios'

export default {
  name: 'App',
  beforeCreate() {
    this.$store.commit('initToken')
    let token = this.$store.state.token 
    if (token) {
      axios.defaults.headers.common['Authorization'] = 'token '+ token
    }
    
  }
}
</script>