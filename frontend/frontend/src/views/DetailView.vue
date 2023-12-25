<template>
  <div class="container">
    <div class="row">
      <div class="col-12 col-md-8 mx-auto">
        <div class="jumbotron card p-3 my-3">
          <h1 class="display-4">{{ task.title }}</h1>
          <p class="lead">
            {{ task.created }}
          </p>
          <span>
            <button
              type="button"
              data-bs-toggle="modal"
              data-bs-target="#exampleModal"
              class="btn btn-sm my-2 btn-warning btn-lg text-white"
            >
              <i class="bi bi-pencil-square"></i> &nbsp;Update Task
            </button>
            <!-- Modal -->
            <div
              class="modal fade"
              id="exampleModal"
              tabindex="-1"
              aria-labelledby="exampleModalLabel"
              aria-hidden="true"
            >
              <div class="modal-dialog">
                <div class="modal-content">
                  <div class="modal-header">
                    <h1 class="modal-title fs-5" id="exampleModalLabel">
                      Update Task
                    </h1>
                    <button
                      type="button"
                      class="btn-close"
                      data-bs-dismiss="modal"
                      aria-label="Close"
                    ></button>
                  </div>
                  <div class="modal-body">
                    <form action="">
                      <div class="form-group">
                        <label for="">Title</label>
                        <input
                          v-model="task.title"
                          type="text"
                          class="form-control"
                        />
                      </div>
                      <div class="form-group">
                        <label for="">Priority</label>
                        <select class="form-select" v-model="task.priority">
                          <option value="{{ task.priority }}" selected>
                            {{ task.priority }}
                          </option>
                          <option value="HIGH">HIGH</option>
                          <option value="MEDIUM">MEDIUM</option>
                          <option value="LOW">HIGH</option>
                        </select>
                      </div>
                      <!-- <div class="form-group">
                        <label for="">Update Image</label>
                        <input
                          type="file"
                          @change="updateImage"
                          ref="image"
                          multiple
                          class="form-control"
                        />
                      </div> -->
                      <div class="form-group">
                        <label for="">Description</label>
                        <textarea
                          v-model="task.desc"
                          cols="30"
                          rows="5"
                          class="form-control"
                        >
                        </textarea>
                      </div>
                    </form>
                  </div>
                  <div class="modal-footer">
                    <button
                      type="button"
                      class="btn btn-secondary"
                      data-bs-dismiss="modal"
                    >
                      Close
                    </button>
                    <button
                      @click="saveChanges"
                      type="button"
                      class="btn btn-primary"
                    >
                      Save changes
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </span>

          <hr class="my-4" />
          <p>
            {{ task.desc }}
          </p>
          <div class="row">
            <div class="col col-md-4 my-2" v-for="img in task.image" :key="img">
              <img :src="img.image" class="img-fluid img-thumbnail" alt="" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DetailView",
  data() {
    return {
      task: {},
      update: {
        title: "",
        priority: "",
        desc: "",

        // update image
      },
      // images: [],
    };
  },
  mounted() {
    this.getData();
  },
  methods: {
    getData() {
      const id = this.$route.params["id"];
      console.log(id);
      axios
        .get(`api/tasks/${id}`)
        .then((res) => {
          //console.log('Tasks: ', res.data);
          this.task = res.data;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    async saveChanges() {
      let data = new FormData();
      data.append("title", this.task.title);
      data.append("desc", this.task.desc);
      data.append("priority", this.task.priority);

      // Check if images have been selected
      //  if (this.images.length > 0) {
      //     console.log("got image", this.images);

      //     // Loop through all selected images and append each to form data
      //     for (let i = 0; i < this.images.length; i++) {
      //       data.append("image", this.images[i]);
      //     }
      //  }

      const id = this.$route.params["id"];
      await axios
        .put(`api/tasks/${id}/`, data, {
          headers: {
            Authorization: `token ${localStorage.getItem("token")}`,
            // "Content-Type": "multipart/form-data",
          },
        })
        .then((res) => {
          console.log(res.data);
          this.getData();
        })
        .catch((error) => {
          console.log(error);
        });
    },
    // updateImage() {
    //   this.images = this.$refs.image.files;
    //   console.log(this.images);
    // },
  },
};
</script>
