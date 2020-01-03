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
						<form @submit="onSubmit">
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Partido</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.id">
								</div>
							</div>

							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Pista</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.idpista">
								</div>
							</div>
							
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Árbitro</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.idarbitro">
								</div>
							</div>
							
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">Resultado</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.resultado">
								</div>
							</div>
							
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">Fecha</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="2050-01-01" name="title" class="form-control" v-model.trim="form.fecha">
								</div>
							</div>
						
							<div class = "rows">
								<div class = "col text-left">
									<b-button type="submit" variant="primary">Editar</b-button>
									<b-button type="submit" class="btn-large-space" :to="{name: 'Partidos'}">Cancelar</b-button>
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
			partidoID: this.$route.params.partidoID,
            form: {
				id: '',
				idpista: '',
				idarbitro: '',
				resultado: '',
				fecha: ''
			}
        }
    },
	methods: {
		onSubmit(event){
			event.preventDefault()
			const path = 'http://localhost:8000/api/partidos/numero/'.replace('numero', this.partidoID)
			
			axios.put(path, this.form).then((response) => {
				this.form.id = response.data.id
				this.form.idpista = response.data.idpista
				this.form.idarbitro = response.data.idarbitro
				this.form.resultado = response.data.resultado
				this.form.fecha = response.data.fecha
				
				alert("Partido actualizado con exito")
				location.href = '#/partidos/'
			}).catch((error) => {
				console.log(error)
			});
		},
		
		getPartido(){
			const path = 'http://localhost:8000/api/partidos/numero/'.replace('numero', this.partidoID)
			
			axios.get(path).then((response) => {
				this.form.id = response.data.id
				this.form.idpista = response.data.idpista
				this.form.idarbitro = response.data.idarbitro
				this.form.resultado = response.data.resultado
				this.form.fecha = response.data.fecha
			}).catch((error) => {
				console.log(error)
			});
		},
	},
	created() {
		this.getPartido()
	}
}
</script>

<style lang='css' scoped></style>
