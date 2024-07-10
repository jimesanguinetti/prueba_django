<template>
    <section class="section">
    <div class="container">
        <h1 class="title">Create a New Location</h1>
        <form id="create-location-form">
            <div class="field">
                <label class="label" for="location-name">Location Name</label>
                <div class="control has-icons-left">
                    <input class="input" type="text" id="location-name" name="name" placeholder="Enter location name" required>
                    <span class="icon is-small is-left">
                        <i class="fas fa-map-marker-alt"></i>
                    </span>
                </div>
            </div>

            <div class="field">
                <div class="control">
                    <a class="button is-dark" @click="createLocation()">Submit</a>
                </div>
            </div>
        </form>
    </div>
</section>
</template>


<script>
// import axios from 'axios'
// import { toast } from 'bulma-toast'

// export default {
//     name: 'AddDeviceView', 
//     data () {
//         return {
//             locations: [  ]
//         }
//     },
//     components: {
//     },
//     mounted () {
//         this.getLocations()
//     },
//     methods: {
//         getLocations() {
//             axios.get('/api/locations/')
//             .then(response => {
//                 this.locations = response.data  
//             })
//             .catch(error => {
//                 console.log(error)
//             })
//         }
//     }
// }
</script>