<template lang="html">
    <div class = "container">
        <div class = "row">
            <div class = "col text-left">
                <h2>Nueva Compra</h2>
            </div>
        </div>
        <div class = "row">
            <div class = "col">
				<div class = "card">
					<div class = "card-body">
						<form @submit="onSubmit">
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Compra</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.idcompra">
								</div>
							</div>

							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Edicion</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.idedicion">
								</div>
							</div>
							
							<div class = "form-group row">
								<label for = "title" class = "col-sm-3 col-form-label">ID_Usuario</label>
								<div class = "col-sm-6">
									<input type="text" placeholder="1" name="title" class="form-control" v-model.trim="form.idusuario">
								</div>
							</div>
						
							<div class = "rows">
								<div class = "col text-left">
									<b-button type="submit" variant="primary">Crear</b-button>
									<b-button type="submit" class="btn-large-space" :to="{name: 'Compras'}">Cancelar</b-button>
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
				idcompra: '',
				idedicion: '',
				fecha_inicio: '2000-01-01',
				idusuario: '',
			}
        }
    },
	methods: {
		onSubmit(event){
			event.preventDefault()
			const path = 'http://localhost:8000/api/compras/'
			
			axios.post(path, this.form).then((response) => {
				this.form.idcompra = response.data.idcompra
				this.form.idedicion = response.data.idedicion
				this.form.fecha_inicio = response.data.fecha_inicio
				this.form.idusuario = response.data.idusuario
				
				alert("Compra creada con exito")
				location.href = '#/compras/'
			}).catch((error) => {
                console.log(error)
                alert(error)
			});
		},
	},
	created() {
	}
}
</script>

<style lang='css' scoped></style>
