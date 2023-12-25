<template>
    <div class="container">
        <div class="row login-div">
            <div v-if="errors" class=" alert alert-danger mx-auto mb-0 ">
                <p  class="text-center">{{ errors }}</p>

            </div>
            <div class="col-12 col-md-5 mx-auto card  p-3">
                <h3 class="text-center">Login to your Account</h3>
                <hr>
                <form @submit.prevent="submitForm" >
                    <div class="form-group">
                        <label for="">Username</label>
                        <input type="text" class="form-control" v-model="username">
                    </div>
                    <div class="form-group">
                        <label for="">Password</label>
                        <input type="password" class="form-control" v-model="password">
                    </div>
                    <button class="btn btn-secondary w-100 mt-2 " type="submit">Login</button>
                </form>
                <br>
                <p>Dont have an account? <router-link to="/register">Register now</router-link> </p>
            </div>
        </div>
    </div>

</template>


<script>
import axios from 'axios' 

export default {
    
    name: 'LoginView',
    data(){
        return {
            username: '',
            password: '',

            // global 
            errors: '',
            
        

        }
    },
    mounted() {
        if (localStorage.getItem('token')) {
            
            this.$router.push('/')
        }
    },
    methods: {
        submitForm() {
            let formData = new FormData() 
            formData.append("username" , this.username)
            formData.append("password", this.password)

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            axios.post('auth/token/login/', formData)
                .then(response => {
                    let token = response.data.auth_token
                    this.$store.commit('setToken', token)
                localStorage.setItem('token',token)
                this.$router.push('/')
                })
                .catch(error => {
                    console.log(error) 
                    console.log('error',error.response.data['non_field_errors'].join(''))
                this.errors = error.response.data['non_field_errors'].join('')
            })
        }
    }
}
</script>

<style scoped> 
.login-div{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

</style>