<template>
  <div class='calculator'>
    <CalculatorLine/>
    <CalculatorBox/>
  </div>
</template>

<script>
import CalculatorLine from './CalculatorLine';
import CalculatorBox from './CalculatorBox'

export default {
  name: 'CalculatorDiv',
  components: {
    CalculatorLine,
    CalculatorBox
  }
}
</script>

<style scoped>
  .calculator{
    height: 100vh;
    width: calc(100% - 12rem);
    position: fixed;
    right: 0;
    background-color: #f8f4f4;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    gap: 5%;
    align-items: center;
  }

  @media (max-width: 768px) {
  .calculator{
    width: 100vw;
  }
}
</style>