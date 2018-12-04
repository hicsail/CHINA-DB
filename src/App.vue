<template>
    <div>
        <div class="row title padding-sides">
            <div class="col-md-9 my-auto grey-text" >
                <h1>China Christian Database</h1>
            </div>

            <div class="col-md-0.5"></div>
            <div class="col-md-1 my-auto center-grey-text">
                <nav>
                    <div role='navigation' aria-label='main navigation' >
                        <router-link to="/geo" class="routerlink" v-on:click="this.$parent.onHomePage = true">
                            <h6 v-if="this.$parent.onHomePage" class="underline-light-text" >Home</h6>
                            <h6 v-if="!this.$parent.onHomePage">Home</h6>
                        </router-link>
                    </div>
                </nav>
            </div>
            <div class="col-md-1 my-auto center-grey-text">
                <nav>
                    <div role='navigation' aria-label='main navigation' >
                        <router-link to="/about" class="routerlink" v-on:click="this.$parent.onHomePage = false">
                            <h6 v-if="this.$parent.onHomePage" >About</h6>
                            <h6 v-if="!this.$parent.onHomePage" class="underline-light-text">About</h6>
                        </router-link>
                    </div>

                </nav>
            </div>
            <div class="col-md-0.5"></div>
        </div>

        <router-view></router-view>

    </div>


</template>

<script>
export default {
  name: 'App',
  methods: {
    setHomePage(status){
      this.$parent.onHomePage = status;
    }
  }
}

</script>



<style>

    .title {
        padding-top: 20px;
        padding-bottom: 20px;
        border-bottom: 1px solid #808080;
    }

    .padding-sides {
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

<!--<div role='navigation' aria-label='main navigation' >-->
<!--<router-link v-if="this.$parent.onHomePage" to="/about" class="routerlink" v-on:click.native="toggleOnHomePage">-->
<!--<h6>About</h6>-->
<!--</router-link>-->
<!--<router-link v-if="!this.$parent.onHomePage" to="/geo" class="routerlink" v-on:click.native="toggleOnHomePage">-->
<!--<h6>Home</h6>-->
<!--</router-link>-->
<!--</div>-->
