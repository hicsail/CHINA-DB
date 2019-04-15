import Vue from 'vue'
import Router from 'vue-router'
import about from '../components/About'
import geo from '../components/Geo'
import individual from '../components/IndividualDetail'
import institution from '../components/InstitutionDetail'

Vue.use(Router);


export default new Router({
	routes: [
		{
			path: '/',
			name: 'Geo',
			component: geo
		},
		{
			path: '/individual',
			name: 'Individual',
			component: individual
		},
		{
			path: '/institution',
			name: 'Institution',
			component: institution
		},
		{
			path: '/about',
			name: 'About',
			component: about
		},
		{
			path: '/geo',
			name: 'Geo',
			component: geo
		}
	],
	mode: 'history',
	linkActiveClass: 'is-active',
	base: '/'
})


