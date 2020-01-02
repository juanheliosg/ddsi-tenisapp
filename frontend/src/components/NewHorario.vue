<template lang="html">
    <div class = "container">
        <div class = "row">
            <div class = "col text-left">
                <h2>Nuevo Horario</h2>
            </div>
        </div>
        <div class = "row">
            <div class = "col">
				<div class = "card">
					<div class = "card-body">
						<form @submit="onSubmit">
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Trabajador</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.idtrabajador">
								</div>
							</div>
							
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Edición</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.idedicion">
								</div>
							</div>
							
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Pista</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.idpista">
								</div>
							</div>
							
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">Fecha de Inicio</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="2016-1-1" name="title" class="form-control" v-model.trim="form.fechaini">
								</div>
							</div>
							
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">Fecha de Finalización</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="2016-1-1" name="title" class="form-control" v-model.trim="form.fechafin">
								</div>
							</div>
						
							<div class = "rows">
								<div class = "col text-left">
									<b-button type="submit" variant="primary">Crear</b-button>
									<b-button type="submit" class="btn-large-space" :to="{name: 'HorariosAsignados'}">Cancelar</b-button>
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
            form: {
				idtrabajador: '',
				idedicion: '',
				idpista: '',
				fechaini: '',
				fechafin: ''
			},
			horario: '',
        }
    },
	methods: {
		onSubmit(event){
			event.preventDefault()
			const path = 'http://localhost:8000/api/horarios/'
			
			axios.post(path, this.form).then((response) => {
				this.form.idtrabajador = response.data.idtrabajador
				this.form.idedicion = response.data.idedicion
				this.form.idpista = response.data.idpista
				this.form.fechaini = response.data.fechaini
				this.form.fechafin = response.data.fechafin
				
				alert("Horario creado con exito")
			}).catch((error) => {
				console.log(error)
			});
		},
	},
	created() {
	}
}
</script>

<style lang='css' scoped></style>
