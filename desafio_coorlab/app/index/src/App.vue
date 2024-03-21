<template>
    <Menu/>
    <CalculatorDiv/>
</template>


<script>
import Menu from './components/menu/Menu.vue'
import CalculatorDiv from './components/calculator/CalculatorDiv.vue'

export default {
  name: 'App',
  components: {
    Menu,
    CalculatorDiv
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
