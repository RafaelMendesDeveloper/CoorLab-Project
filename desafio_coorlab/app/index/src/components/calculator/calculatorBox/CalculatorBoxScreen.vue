<template>
  <div id='boxCalculator'>
    <CalculatorBoxData :transportData="transportData" @submitForm="submitForm" @submitDate="submitDate"/>
    <CalculatorBoxShow :selectedCity="selectedCity" :economyPrice="economyPrice"/>
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
  },
  data() {
    return {
      selectedCity: '',
      economyPrice: '',
      transportData: [],
    }
  },
  methods: {
    submitForm(city, economyPrice) {
      this.selectedCity = city;
      this.economyPrice = economyPrice;
    },
    submitDate(city, economyPrice) {
      this.selectedCity = city;
      this.economyPrice = economyPrice;
    }
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