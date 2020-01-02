<template lang="html">
    <div class = "container">
        <div class = "row">
            <div class = "col text-left">
                <h2>Editar Horario</h2>
            </div>
        </div>
        <div class = "row">
            <div class = "col">
				<div class = "card">
					<div class = "card-body">
						<form @onSubmit="onSubmit">
							<div class = "form-group row">
								<label for = "title" class = "col-sm-2 col-form-label">Título</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="Título" name="title" class="form-control">
								</div>
							</div>
						</form>
					</div>
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
            { key: 'idpista', label: 'ID_Pista'},
            { key: 'idtrabajador', label: 'ID_Trabajador'}, 
            { key: 'idedicion', label: 'ID_Edición'},
            { key: 'fechaini', label: 'Fecha de Inicio'},
            { key: 'fechafin', label: 'Fecha de Finalización'},
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
