<template>
    <div id='boxCalculator'>
        <CalculatorBoxData/>
        <CalculatorBoxShow/>
    </div>
</template>

<script>
import CalculatorBoxData from './CalculatorBoxData'
import CalculatorBoxShow from './CalculatorBoxShow'

export default {
  name: 'CalculatorBoxScreen',
  components: {
    CalculatorBoxData,
    CalculatorBoxShow
  }
}
</script>

<style scoped>
#boxCalculator {
    height: 100%;
    width: 100%;
    display: flex;
    align-items: center;
    gap: 2rem;
}
</style>
