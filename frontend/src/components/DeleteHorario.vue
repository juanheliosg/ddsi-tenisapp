<template lang="html">
	<div class="container">
		<h3>Eliminando horario...</h3>
	</div>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return {
			horarioID: this.$route.params.horarioID,
        }
    },
	methods: {
		deleteHorario(){
			const path = 'http://localhost:8000/api/horarios/numero/'.replace('numero', this.horarioID)
			
			axios.delete(path).then(() => {
				location.href = '#/horarios/'
			}).catch((error) => {
				console.log(error)
			});
		},
	},
	created() {
		this.deleteHorario()
	}
}
</script>

<style lang="css" scoped>
</style>
