<template>
    <div class="page-product">
        <div class="columns is-multiline">
            <div class="column is-9">
                <figure class="image mb-6">
                    <!-- <img :src="device.image"> -->
                </figure>

                <h1 class="title">{{ device.name }}</h1>

                <p>{{ device.location?.name }}</p>
            </div>

            <div class="column is-3">
                <h2 class="subtitle">Actions</h2>

                <div class="field has-addons mt-6">
                    <div class="control">
                        <a class="button is-dark" @click="removeDevice()">Remove device</a>
                    </div>
                    <div class="control">
                        <a class="button is-dark" @click="editDevice()">Edit device</a>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
    name: 'DeviceView',
    data() {
        return {
            device: [ ],
        }
    },
    mounted() {
        this.getDevice() 
    },
    methods: {
        getDevice() {
            const slug = this.$route.params.slug
            axios.get(`/api/devices/${slug}`)
            .then(response => {
                this.device = response.data
                document.title = this.device.name
            })
            .catch(error => {
                console.log(error)
            })
        },
        removeDevice() {
            const item = {
                device: this.device 
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        },
        editDevice() {
            if (isNaN(this.quantity) || this.quantity < 1) {
                this.quantity = 1
            }

            const item = {
                product: this.product,
                quantity: this.quantity
            }

            this.$store.commit('addToCart', item)

            toast({
                message: 'The product was added to the cart',
                type: 'is-success',
                dismissible: true,
                pauseOnHover: true,
                duration: 2000,
                position: 'bottom-right',
            })
        }
    }
}
</script>