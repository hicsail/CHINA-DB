import Vue from 'vue'
import Router from 'vue-router'
import home from '@/components/Home'
import about from '@/components/About'
import notfound from '@/components/NotFound'
import geo from '@/components/Geo'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: home
    },
    {
      path: '/about',
      name: 'About',
      component: about
    },
		{
			path: '*',
			name: 'NotFound',
			component: notfound
		},
		{
			path: '/geo',
			name: 'Geo',
			component: geo
		}
  ],
  mode: 'history',
  linkActiveClass: 'is-active'
})
