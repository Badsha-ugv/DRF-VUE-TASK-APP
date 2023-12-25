<template>
  <div class="container">
    <div class="row my-3">
      <div class="col-12 col-md-5 ">
        <div class="alert alert-success">
          <h3 class="text-center">CREATE A NEW TASK</h3>
          <div class="card card-body p-3 my-2">
            <form @submit.prevent="submitForm">
              <div class="form-group">
                <label for="">Title</label>
                <input type="text" class="form-control" v-model="title" />
              </div>
              <div class="form-group">
                <label for="">Priority</label>
                <select name="" v-model="priority" id="" class="form-select">
                  <option>Select Priority</option>
                  <option value="HIGH">HIGH</option>
                  <option value="MEDIUM">MEDIUM</option>
                  <option value="LOW">LOW</option>
                </select>
              </div>
              <div class="form-group">
                <label for="">Task Image(Optional)</label> 
                <input ref="file" type="file" @change="imageUp" accept=".png, .jpg, .jpeg" multiple/>
              </div>
              <div class="form-group">
                <label for="">Description(Optional)</label>
                <textarea
                  v-model="desc"
                  cols="30"
                  rows="5"
                  class="form-control"
                ></textarea>
              </div>
              <button class="btn btn-success mt-2">Create Task</button>
            </form>
          </div>
        </div>
      </div>

      <div class="col-12 col-md-7 ">
        <div class="alert alert-success">
          <h3 class="text-center">TASK LIST</h3>
          <button class="btn btn-sm btn-danger logoutBtn" @click="logout">Logout</button>
          <div class="task-list card card-body p-3 my-2">
            <input type="text" v-model="search" class="form-control my-2" placeholder="Search tasks...">

            <table class="table table-striped table-bordered text-center">
              <thead>
                <tr>
                  <th>Sl.</th>
                  <th>Title</th>
                  <th>Action</th>
                </tr>
              </thead>
              <tbody>
                <tr v-for="(item,index) in searchTask" :key="item.id">
                  <td>{{ index+1 }}</td>
                  <td>{{ item.title }}
                    <sup>

                      <span class="badge bg-secondary">{{ item.priority }}</span>
                    </sup>
                  
                  </td>
                  <td class="d-flex justify-content-center gap-2">
                    <router-link :to="{name:'detail',params:{'id':item.id}}" class="btn btn-sm btn-warning">
                      <i class="bi bi-eye-fill "></i>
                    </router-link>
                    <button @click="taskComplete(item.id)" class="btn btn-sm btn-outline-success">

                      <i class="bi bi-check-circle"></i>
                    </button>
                    <button class="btn btn-sm btn-outline-danger" @click="deleteTask(item.id)">

                      <i class="bi bi-trash"></i>
                    </button>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "HomeView",
  data() {
    return {
      title: "",
      desc: "",
      priority: "",
      images: [],

      // search 
      search:'',
      // badge color
      
        
    
      
      // task view 
      tasks:[],

      // global
      token: "",
    };
  },
  beforeCreate() {
    if (!this.$store.state.isAuthenticated) {
      this.$router.push("/login");
    }
  },
  mounted() {
    this.token = localStorage.getItem("token");
    this.getData()
  },
  computed: {
    searchTask() {
      if (!this.search) {
        return this.tasks
      }
      return this.tasks.filter(task => task.title.toLowerCase().includes(this.search.toLowerCase()))
    }
  },
  methods: {
    async submitForm() {
      let formData = new FormData()
        
      formData.append('title',this.title)
      formData.append('desc',this.desc)
      formData.append('priority', this.priority)

      if (this.images.length) {
        for (let i = 0; i < this.images.length; i++){
          formData.append('image',this.images[i])
        }
      }
      await axios
        .post("api/tasks/", formData, {
          headers: {
            'Authorization': `token ${this.token}`,
            'Content-Type': 'multipart/form-data'
          },
        })
        .then((res) => {
          console.log(res);
          this.getData()
        })
        .catch((error) => {
          console.log(error);
        });
      this.title = ''
      this.desc = ''
      // this.priority = ''
      this.images = []
      
    },
    getData() {
      axios.get('api/tasks/', {
        headers: {
          'Authorization': `Token ${this.token}`
        }
      })
        .then(res => {
          this.tasks = res.data;
        console.log(this.tasks)
        })
        .catch(error => {
        console.log(error)
        })
      
    },

    deleteTask(id) {
      axios.delete(`api/tasks/${id}/`, {
        headers: {
          "Authorization": `Token ${this.token}`
        }
      })
        .then(res => {
          console.log(res)
          this.getData();
        
        })
        .catch(error => {
        console.log(error.data)
      })
    },
    taskComplete(id) {
      axios.get(`api/complete/${id}/`, null,{
        headers: {
          'Authorization':`token ${this.token}`
        }
      })  
        .then(res => {
          console.log(res)
        this.getData()
        })
        .catch(error => {
        console.log(error)
      })
    },
    imageUp() {
      this.images = this.$refs.file.files
      console.log(this.images)
    },
    logout() {
      axios.post('auth/token/logout/',null, {
        headers: {
          'Authorization':`token ${this.token}`
        }
      })
        .then(res => {
          localStorage.removeItem("token");
          this.$store.commit('removeToken')
          axios.defaults.headers.common['Authorization'] = '' 
          this.$router.push('/login')
        })
        .catch(error => {
        console.log(error)
      })
    }


    // methods end here
  },
};
</script>


<style scoped>
.task-list{
  height: 410px;
    overflow-y: auto;
}
.logoutBtn{
  position: absolute;
  right:9px;
  top: 9px;
}
</style>