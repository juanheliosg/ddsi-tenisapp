import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import tenis from '@/components/tenis'

import Horarios from '@/components/Horarios.vue'
import EditHorario from '@/components/EditHorario.vue'
import NewHorario from '@/components/NewHorario.vue'
import DeleteHorario from '@/components/DeleteHorario.vue'

import Partidos from '@/components/Partidos.vue'
import NewPartido from '@/components/NewPartido.vue'
import EditPartido from '@/components/EditPartido.vue'
import DeletePartido from '@/components/DeletePartido.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/tenistasno',
    name: 'tenistasno',
    component: tenis
  },
  {
    path: '/horarios',
    name: 'HorariosAsignados',
    component: Horarios
  },
  {
    path: '/horarios/new',
    name: 'NewHorario',
    component: NewHorario
  },
  {
    path: '/horarios/:horarioID/edit',
    name: 'EditHorario',
    component: EditHorario
  },
  {
    path: '/horarios/:horarioID/delete',
    name: 'DeleteHorario',
    component: DeleteHorario
  },
  {
    path: '/partidos',
    name: 'Partidos',
    component: Partidos
  },
  {
    path: '/partidos/new',
    name: 'NewPartido',
    component: NewPartido
  },
  {
    path: '/partidos/:partidoID/edit',
    name: 'EditPartido',
    component: EditPartido
  },
  {
    path: '/partidos/:partidoID/delete',
    name: 'DeletePartido',
    component: DeletePartido
  },
]

const router = new VueRouter({
  routes
})

export default router
