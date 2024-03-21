<template>
    <div id='box'>
        <CalculatorBoxStripe/>
        <CalculatorBoxScreen/>    
    </div>
</template>
x 
<script>
import CalculatorBoxStripe from './calculatorBox/CalculatorBoxStripe'
import CalculatorBoxScreen from './calculatorBox/CalculatorBoxScreen'

export default {
  name: 'CalculatorBox',
  components: {
    CalculatorBoxStripe,
    CalculatorBoxScreen
  }
}
</script>

<style scoped>
#box {
  margin-top: 2rem;
  height: 65%;
  width: 94%;
  background-color: white;
  box-shadow: 0 0 10px rgba(0,0,0,0.2);
  border-radius: 5px;
}
</style>
