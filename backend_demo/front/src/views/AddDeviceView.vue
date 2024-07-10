<template>
    <section class="section">
        <div class="container">
            <h1 class="title">Create a New Device</h1>
            <form id="create-device-form">
                <div class="field">
                    <label class="label" for="device-name">Device Name</label>
                    <div class="control has-icons-left">
                        <input class="input" type="text" id="device-name" v-model="deviceName" name="name" placeholder="Enter device name" required>
                        <span class="icon is-small is-left">
                            <i class="fas fa-tag"></i>
                        </span>
                    </div>
                </div>

                <div class="field">
                    <label class="label" for="device-location">Location</label>
                    <div class="control has-icons-left">
                        <div class="select">
                            <select id="device-location" v-model="deviceLocation" name="location" required>
                                <option value="" disabled selected>Select location</option>
                                <option 
                                v-for="location in locations" 
                                :key="location.id" 
                                :value="location.id">{{ location.name }}</option>
                            </select>
                        </div>
                        <span class="icon is-small is-left">
                            <i class="fas fa-map-marker-alt"></i>
                        </span>
                    </div>
                </div>

                <div class="field">
                    <label class="label" for="device-image">Device Image</label>
                    <div class="control has-icons-left">
                        <input class="input" type="file" id="device-image" name="image" @change="handleFileChange($event, 'image')" accept="image/*" required>
                        <span class="icon is-small is-left">
                            <i class="fas fa-image"></i>
                        </span>
                    </div>
                </div>

                <div class="field">
                    <label class="label" for="device-thumbnail">Device Thumbnail</label>
                    <div class="control has-icons-left">
                        <input class="input" type="file" id="device-thumbnail" name="thumbnail" @change="handleFileChange($event, 'thumbnail')" accept="image/*" required>
                        <span class="icon is-small is-left">
                            <i class="fas fa-th"></i>
                        </span>
                    </div>
                </div>

                <div class="field is-grouped">
                    <div class="control">
                        <a class="button is-dark" @click="createDevice()">Submit</a>
                    </div>
                </div>
            </form>
        </div>
    </section>
</template>


<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'AddDeviceView', 
    data () {
        return {
            locations: [  ],
            formData: {}
        }
    },
    components: {
    },
    mounted () {
        this.getLocations()
    },
    methods: {
        getLocations() {
            axios.get('/api/locations/')
            .then(response => {
                this.locations = response.data  
            })
            .catch(error => {
                console.log(error)
            })
        },
        handleFileChange(event, type) {
            const file = event.target.files[0];
            this.formData[type] = file;
        },
        createDevice(){
            this.formData["name"] = this.deviceName;
            this.formData["location_id"] = this.deviceLocation;
            console.log('Device creado:', this.formData);

            axios.post('/api/devices/', this.formData)
            .then(response => {
                console.log('Device creado:', response.data);
            })
            .catch(error => {
                console.error('Error al crear el device:', error);
            });
        }
    }
}
</script>