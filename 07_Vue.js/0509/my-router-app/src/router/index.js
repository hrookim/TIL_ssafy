import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AboutView from '../views/AboutView.vue'
import LottoView from '../views/LottoView.vue'
import UserProfile from '../views/UserProfile.vue'


Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: AboutView,
  },
  {
    path: '/lotto',
    name: 'lotto',
    component: LottoView,
  },
  {
    path: '/:userId/article/:articleId',
    name: 'profile',
    component: UserProfile
  }

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
