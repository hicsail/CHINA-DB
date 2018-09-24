<template>
  <div id="app">
      <h1>CHINA-DB</h1>
      <nav id="navbar">
          <div id="navbar-items" role='navigation' aria-label='main navigation'>
              <div id="navbar-itemWrapper">
                  <router-link class="navbar-item" to="/">
                      Home
                  </router-link>
                  <router-link class="navbar-item" to="/about">
                      About
                  </router-link>
                  <router-link class="navbar-item" to="/geo">
                      Geo
                  </router-link>
              </div>
          </div>
      </nav>
      <router-view></router-view>
  </div>

</template>

<script>
export default {
  name: 'App'
}
</script>

<style>

#app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    overflow-y: scroll;
    margin-top: 40px;
}

#navbar {
    background-color: #fceeff;
    padding-left: 20px;
    padding-right: 10px;
    border: 3px solid green;
}

#navbar-items{
    display:flex;
    justify-content:center;
    margin-right: auto;
}

#navbar-itemWrapper{
    flex-grow: 1;
    display: flex;
}

.navbar-item{
    padding-left: 10px;
    padding-right: 10px;
}

</style>
