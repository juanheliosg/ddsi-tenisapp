<template lang="html">
	<div class="container">
		<h3>Eliminando compra...</h3>
	</div>
</template>

<script>
import axios from 'axios';

export default{
    data(){
        return {
			compraID: this.$route.params.compraID,
        }
    },
	methods: {
		deleteCompra(){
			const path = 'http://localhost:8000/api/compras/numero/'.replace('numero', this.compraID)
			
			axios.delete(path).then(() => {
				location.href = '#/compras/'
			}).catch((error) => {
				console.log(error)
			});
		},
	},
	created() {
		this.deleteCompra()
	}
}
</script>

<style lang="css" scoped>
</style>
