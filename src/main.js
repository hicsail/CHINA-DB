// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import L from 'leaflet';
delete L.Icon.Default.prototype._getIconUrl;
import Vue from 'vue';
import App from './App';
import router from './router';
import BootstrapVue from 'bootstrap-vue';
import { library } from '@fortawesome/fontawesome-svg-core';
import { faBars, faBuilding, faChevronDown, faChevronUp, faChurch, faFilter, faMale, faMapMarker, faRedo, faTimes, faUniversity } from '@fortawesome/free-solid-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import './assets/leaflet.awesome-markers.css';
import './assets/leaflet.awesome-markers.js';


library.add(faBars, faBuilding, faChevronDown, faChevronUp, faChurch, faFilter, faMale, faMapMarker, faRedo, faTimes, faUniversity);

window.EventBus = new Vue();

Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.use(BootstrapVue);

Vue.config.productionTip = false;

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
  data: {
    onHomePage: true
  }
});
