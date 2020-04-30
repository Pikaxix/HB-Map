import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../components/Home.vue'
import HBmap from '../components/HBmap.vue'
import SVG from '../components/SVG.vue'
import Broswer from '../components/broswer/broswer.vue'

Vue.use(VueRouter)

const routes = [
  { path: '/', component: Home },
  { path: '/HBmap', component: HBmap },
  { path: '/SVG', component: SVG },
  { path: '/broswer', component: Broswer }
]

const router = new VueRouter({
  routes
})

export default router
