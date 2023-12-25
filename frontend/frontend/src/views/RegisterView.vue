<template>
    <div class="container">
        <div class="row register-div">
            <div v-if="errors" class=" alert alert-danger mx-auto mb-0 ">
                <p  class="text-center">{{ errors }}</p>

            </div>
            <div class="col-12 col-md-5 mx-auto card  p-3">
                <h3 class="text-center">Register a new Account</h3>
                <hr>
                <form @submit.prevent="submitForm" >
                    <div class="form-group">
                        <label for="">Username</label>
                        <input type="text" class="form-control" v-model="username" required>
                    </div>
                    <div class="form-group">
                        <label for="">Email</label>
                        <input type="email" class="form-control" v-model="email" required>
                    </div>
                    <div class="form-group">
                        <label for="">Password</label>
                        <input type="password" class="form-control" v-model="password" required>
                    </div>
                    <div class="form-group">
                        <label for="">Confirm Password</label>
                        <input type="password" class="form-control" v-model="password2" required>
                    </div>
                    <button class="btn btn-secondary w-100 mt-2 " type="submit">Register</button>
                </form>
                <br>
                <p>Already have an account? <router-link to="/login">Login now</router-link> </p>
            </div>
        </div>
    </div>

</template>


<script>
import axios from 'axios' 

export default {
    
    name: 'RegisterView',
    data(){
        return {
            username: '',
            password: '',
            password2: '',
            email:'',

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
            formData.append("email", this.email)

            axios.defaults.headers.common['Authorization'] = ''
            localStorage.removeItem('token')
            axios.post('auth/users/', formData)
                .then(response => {
                
                this.$router.push('/')
                })
                .catch(error => {
                    console.log('error',error)
                this.errors = error.response.data
            })
        }
    }
}
</script>

<style scoped> 
.register-div{
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

</style>