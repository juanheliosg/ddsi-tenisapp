<template>
  <div id="app">
    <div id="nav">
      <router-link to="/">Home</router-link> |
      <router-link to="/tenistasno">Consultar tenistas no inscritos</router-link> |
      <router-link :to="{ name:'HorariosAsignados'}">Asignar horarios</router-link> |
      <router-link :to="{ name:'Partidos'}">Editar partidos</router-link> |
      <router-link :to="{ name:'Compras'}">Iniciar compras</router-link>
    </div>

    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
