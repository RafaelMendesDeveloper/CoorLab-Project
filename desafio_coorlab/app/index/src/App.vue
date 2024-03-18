<template>
  <Menu msg="Hello, World!"/>
</template>


<script>
import Menu from './components/menu/Menu.vue'

export default {
  name: 'App',
  components: {
    Menu
  }
}
</script>

<style>
*{
  margin: 0;
  padding: 0;
}

#app{
  width: 100%;
  height: 100%;
  font-family: 'Roboto', sans-serif;
}


</style>
