<template lang="html">
    <div class = "container">
        <div class = "ro">
            <div class = "col text-left"> 
                <h4> Listado de tenistas no inscritos en la edicion {{ edicion }}</h4>
                <div class="select_edition">
                    <input v-model="newedicion" type="text" placeholder="Pon la edición" v-on:keyup.enter="getTenistas()"> 
                </div>

                <div class="col-md-16">
                    <b-table striped hover :items='tenistas' :fields='fields'>
                    </b-table>
            </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return { 
            fields: [
            { key: 'nombre', label: 'Nombre'}, 
            { key: 'apellido', label: 'Apellido'},
            { key: 'telefono', label: 'Telefono'},
            { key: 'mail', label: 'Correo'},
            ],
            tenistas: [],
            newedicion: '',
            edicion: ''
        }
    },
    methods: {
        getTenistas(){
            const path = 'http://127.0.0.1:8000/tenistas_no_inscritos/edicion/'.replace('edicion', this.newedicion)
            axios.get(path).then((response) => {
                this.tenistas = response.data
            }).catch((error) => {
                console.log(error)
            });
            this.edicion = this.newedicion;
            
        },
    },
    created(){
        this.getTenistas()
    }
}
</script>

<style lang='css' scoped></style>
