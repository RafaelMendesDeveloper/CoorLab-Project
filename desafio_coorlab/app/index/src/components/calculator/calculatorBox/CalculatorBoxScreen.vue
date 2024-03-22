<template>
  <div id='boxCalculator'>
    <CalculatorBoxData :transportData="transportData" @form-submitted="updateData"/>
    <CalculatorBoxShow :selectedCity="selectedCity" :economyPrice="economyPrice" :infos="infos"/>
  </div>
</template>

<script>
import CalculatorBoxData from './CalculatorBoxData'
import CalculatorBoxShow from './CalculatorBoxShow'
import axios from 'axios';

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
      infos: '',
      transportData: [], 
    }
  },
  methods: {
    updateData(city, economyPrice, infos) {
      this.selectedCity = city;
      this.economyPrice = economyPrice;
      this.infos = infos;
    },
    async fetchTransportData() {
      try {
        const response = await axios.get('http://localhost:5000/api/cities'); 
        const cities = response.data;
        for (const city of cities) {
          const transportResponse = await axios.get(`http://localhost:5000/api/transport?city=${city}`);
          this.transportData.push(...transportResponse.data);
        }
      } catch (error) {
        console.error('Erro ao obter dados do servidor:', error);
      }
    }
  },
  async mounted() {
    await this.fetchTransportData();
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
