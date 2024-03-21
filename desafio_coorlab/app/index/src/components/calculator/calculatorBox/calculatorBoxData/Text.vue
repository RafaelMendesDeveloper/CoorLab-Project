<template>
  <div id='calculatorText'>
    <img src='@/assets/value.png'>
    <p>Calcule o Valor da Viagem</p>
  </div>
</template>

<script>
export default {
  name: 'CalculatorBoxDataText',
}
</script>

<style scoped>
    #calculatorText{
        display: flex;
        height: fit;
        width: fit;
        gap: 0.6rem;
        margin-left: 2rem;
        margin-right: 2rem;
        align-items: center;
    }

    img{
        width: 2rem;
        height: 2rem;
    }

    @media (max-width: 768px) {
      p{
        font-size: 10px;
      }
  }
</style>