import Vue from 'vue';
import Vuex from 'vuex';
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex);

export default new Vuex.Store({

  state: {
    individualData: {},
    institutionData: {}
  },
  mutations: {
    setIndividualData(state, newIndivData){
      state.individualData = newIndivData;
    },
    setInstitutionData(state, newInstData){
      state.institutionData = newInstData;
    }
  },
  getters: {
    individualData: state => state.individualData,
    institutionData: state => state.institutionData
  },
  plugins: [createPersistedState()]

})
