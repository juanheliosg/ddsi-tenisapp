import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'

import tenis from '@/components/tenis'

import HorariosAsignados from '@/components/Horarios.vue'
import EditHorario from '@/components/EditHorario.vue'

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
    component: HorariosAsignados
  },
  {
    path: '/horarios/edit',
    name: 'EditHorario',
    component: EditHorario
  }
]

const router = new VueRouter({
  routes
})

export default router
