<template lang="html">
	<div class="container">
		<h3>Eliminando partido...</h3>
	</div>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return {
			partidoID: this.$route.params.partidoID,
        }
    },
	methods: {
		deletePartido(){
			const path = 'http://localhost:8000/api/partidos/numero/'.replace('numero', this.partidoID)
			
			axios.delete(path).then(() => {
				location.href = '#/partidos/'
			}).catch((error) => {
				console.log(error)
			});
		},
	},
	created() {
		this.deletePartido()
	}
}
</script>

<style lang="css" scoped>
</style>
