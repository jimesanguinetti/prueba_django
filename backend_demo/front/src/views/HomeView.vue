<template>
  <div class="home">
    <section class="hero is-medium is-dark mb-6">
        <div class="hero-body has-text-centered">
            <p class="title mb-6">
                Welcome to Devices
            </p>
            <p class="subtitle">
                The best devices store online
            </p>
        </div>
    </section>  

    <div class="columns is-multiline">
      <div class="column is-12">
          <h2 class="is-size-2 has-text-centered">Latest devices</h2>
      </div>

      <div class="column is-3"
        v-for="device in devices" 
        v-bind:key="device.id">
        <div class="box">
          <figure class="image mb-4"> 
            <img :src="device.image">
          </figure>
          <h3 class="is-size-4">{{ device.name }}</h3>
          <p class="is-size-6 has-text-grey">{{ device.location.name }}</p>

          <router-link v-bind:to="device.slug" class="button is-dark mt-4">View details</router-link>
        </div>
      </div>
    </div>

  </div>
</template>

<script>
import axios from 'axios'
 
export default {
  name: 'HomeView', 
  data () {
      return {
        devices: [  ]
      }
  },
  components: {
  },
  mounted () {
    this.getDevices()
  },
  methods: {
    getDevices() {
      axios.get('/api/devices/')
      .then(response => {
          this.devices = response.data  
      })
      .catch(error => {
        console.log(error)
      })
    }
  }
} 
</script>

<style scoped>
  .image {
    margin-top: -1.25rem;
    margin-left: -1.25rem;
    margin-right: -1.25rem;
  }
</style>
