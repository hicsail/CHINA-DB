<template>
    <div>
        <div class="row title ">
            <div class="col-md-10 my-auto grey-text padding-left" >
                <h1>China Christian Database</h1>
            </div>


            <div class="col-md-2 my-auto center-grey-text" >
                <nav>
                    <div role='navigation' aria-label='main navigation' >
                        <router-link to="/geo" class="routerlink center-item" v-on:click="this.$parent.onHomePage = true">
                            <h6 v-if="this.$parent.onHomePage" class="underline-light-text">Home</h6>
                            <h6 v-if="!this.$parent.onHomePage">Home</h6>
                        </router-link>
                    </div>
                </nav>
                <nav>
                    <div role='navigation' aria-label='main navigation' >
                        <router-link to="/about" class="routerlink center-item" v-on:click="this.$parent.onHomePage = false">
                            <h6 v-if="this.$parent.onHomePage" >About</h6>
                            <h6 v-if="!this.$parent.onHomePage" class="underline-light-text">About</h6>
                        </router-link>
                    </div>
                </nav>
            </div>

        </div>

        <router-view></router-view>

    </div>


</template>

<script>
import Geo from './components/Geo'
import Individual from './components/IndividualDetail'
import Institution from './components/InstitutionDetail'

export default {
  name: 'App',
  methods: {
    setHomePage(status){
      this.$parent.onHomePage = status;
    }
  },
  components: {
    Geo,
    Individual,
    Institution
  }
}

</script>


<style>

    .title {
        padding-top: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #808080;
    }

    .padding-left {
        padding-left: 40px;
    }

    .routerlink {
        color: #101010;
    }

    .grey-text {
        color: #101010;
    }

    .center-grey-text {
        text-align: center;
        color: #101010;
    }

    .underline-light-text {
        text-decoration: underline;
        color: #808080;
    }

</style>

