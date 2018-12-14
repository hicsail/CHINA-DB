import Vue from 'vue'
import Router from 'vue-router'
import about from '@/components/About'
import geo from '@/components/Geo'

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/about',
      name: 'About',
      component: about
    },
		{
			path: '*',
			redirect: '/geo'
		},
		{
			path: '/geo',
			name: 'Geo',
			component: geo
		}
  ],
  mode: 'history',
  linkActiveClass: 'is-active',
	base: window.location.pathname
})
