<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left"> 
				<div class="">
					<h4>Horarios asignados a trabajadores</h4>

					<b-button size="sm" variant="primary" :to="{ name:'NewHorario'}">
						Nuevo Horario
					</b-button>
				</div>
				<br>
                
                <div class="col-md-15">
                    <b-table striped hover :items='horarios' :fields='fields'>
						<template v-slot:cell(action)="data">
							<b-button size="sm" variant="primary" :to="{ name:'EditHorario', params: {horarioID: data.item.idtrabajador}}">
								Editar
							</b-button>
							<b-button size="sm" variant="danger">
								Eliminar
							</b-button>
						</template>
                    </b-table>
				</div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default{
    data () {
        return { 
            fields: [
            { key: 'idtrabajador', label: 'ID_Trabajador'}, 
            { key: 'idedicion', label: 'ID_Edición'},
			{ key: 'idpista', label: 'ID_Pista'},
            { key: 'fechaini', label: 'Fecha de Inicio'},
            { key: 'fechafin', label: 'Fecha de Finalización'},
            { key: 'action', label: ''}
            ],
            horarios: [],
        }
    },
    methods: {
        getHorarios(){
            const path = 'http://localhost:8000/api/horarios/'
            axios.get(path).then((response) => {
                this.horarios = response.data
            }).catch((error) => {
                console.log(error)
            });
        },
    },
    created(){
        this.getHorarios()
    }
}
</script>

<style lang='css' scoped></style>
