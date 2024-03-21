<template>
  <div id='stripe'>
    <img src="@/assets/bus.png" alt="bus" id="bus">
    <p>Calculadora de Viagem</p>
  </div>
</template>

<script>
export default {
  name: 'CalculatorDivLine',
}
</script>

<style scoped>
#stripe {
  border-top-left-radius: 5px;
  border-top-right-radius: 5px;
  background-color: #2a3041;
  width: 100%;
  height: 3rem;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 0.8rem;
}

p{
    color: white;
    font-weight: bold;
}

img{
    max-height: 2rem;
    max-width: 2rem;
    margin-left: 2rem;
}
</style>