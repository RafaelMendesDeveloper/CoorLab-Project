<template>
  <div id='calculatorShow'>
    <h1 v-if="selectedCity">{{ selectedCity }}</h1>
    <p v-if="selectedCity && economyPrice">Preço da econômica: {{ economyPrice }}</p>
    <p v-else>Nenhum dado selecionado.</p>
  </div>
</template>

<script>
export default {
  name: 'CalculatorBoxShow',
  props: {
    selectedCity: String,
    economyPrice: String
  }
}
</script>

<style scoped>
#calculatorShow {
  width: 100%;
  height: 80%;
  margin-bottom: 4rem;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

h1 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

p {
  font-size: 1.2rem;
}
</style>
