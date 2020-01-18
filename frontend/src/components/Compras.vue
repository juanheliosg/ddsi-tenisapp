<template lang="html">
    <div class="container">
        <div class="row">
            <div class="col text-left"> 
				<div class="">
					<h4>Compras</h4>

					<b-button size="sm" variant="primary" :to="{ name:'NewCompra'}">
						Iniciar Compra
					</b-button>
				</div>
				<br>
                
                <div class="col-md-15">
                    <b-table striped hover :items='compras' :fields='fields'>
						<template v-slot:cell(action)="data">
							<b-button size="sm" variant="danger" :to="{ name:'DeleteCompra', params: {compraID: data.item.idcompra}}">
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
            { key: 'idcompra', label: 'ID_Compra'},
            { key: 'idedicion', label: 'ID_Edicion'},
            { key: 'fecha_inicio', label: 'Fecha_inicio'},
            { key: 'idusuario', label: 'ID_Usuario'},
            { key: 'action', label: ''}
            ],
            compras: [],
        }
    },
    methods: {
        getCompras(){
            const path = 'http://localhost:8000/api/compras/'
            axios.get(path).then((response) => {
                this.compras = response.data
            }).catch((error) => {
                console.log(error)
            });
        },
    },
    created(){
        this.getCompras()
    }
}
</script>

<style lang='css' scoped></style>
