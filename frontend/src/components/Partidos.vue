<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left"> 
				<div class="">
					<h4>Partidos</h4>

					<b-button size="sm" variant="primary" :to="{ name:'NewPartido'}">
						Nuevo Partido
					</b-button>
				</div>
				<br>
                
                <div class="col-md-15">
                    <b-table striped hover :items='partidos' :fields='fields'>
						<template v-slot:cell(action)="data">
							<b-button size="sm" variant="primary" :to="{ name:'EditPartido', params: {partidoID: data.item.id}}">
								Editar
							</b-button>
							<b-button size="sm" variant="danger" :to="{ name:'DeletePartido', params: {partidoID: data.item.id}}">
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
            { key: 'id', label: 'ID_Partido'},
            { key: 'idpista', label: 'ID_Pista'},
            { key: 'idarbitro', label: 'ID_Edición'},
			{ key: 'resultado', label: 'Resultado'},
            { key: 'fecha', label: 'Fecha'},
            { key: 'action', label: ''}
            ],
            partidos: [],
        }
    },
    methods: {
        getPartidos(){
            const path = 'http://localhost:8000/api/partidos/'
            axios.get(path).then((response) => {
                this.partidos = response.data
            }).catch((error) => {
                console.log(error)
            });
        },
    },
    created(){
        this.getPartidos()
    }
}
</script>

<style lang='css' scoped></style>
