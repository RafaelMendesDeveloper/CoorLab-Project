<template>
  <div id='calculatorShow'>
    <p v-if="selectedCity">Estas ão as melhores alternativas de viagem para a data selecionada</p>
    <p v-if="companyName">Nome da Empresa: {{ companyName }}</p>
    <p v-if="bed">Leito: {{ bed }}</p>  
    <p v-if="duration">Duração: {{ duration }}</p>
    <p v-if="price_confort">Preço Leito: {{ price_confort }}</p>
    <p v-if="seat">Assento: {{ seat }}</p>
    <p v-if="price_econ">Preço Semi-Leito: {{ price_econ }}</p>
    <p v-else>Nenhum dado selecionado.</p>
  </div>
</template>

<script>
export default {
  name: 'CalculatorBoxShow',
  props: {
    selectedCity: String,
    economyPrice: String,
    infos: String
},
  data() {
    return {
      infosObject: null,
      companyName: '',
      bed : '',
      duration : '',
      price_confort : '',
      seat: '',
      price_econ: ''
    };
  },
  watch: {
    infos : {
    handler(newInfos) {
      this.infosObject = newInfos ? JSON.parse(newInfos) : null;
      this.companyName = this.infosObject ? this.infosObject.name : '';
      this.bed = this.infosObject ? this.infosObject.bed : '';
      this.duration = this.infosObject ? this.infosObject.duration : '';
      this.price_confort = this.infosObject ? this.infosObject.price_confort : '';
      this.seat = this.infosObject ? this.infosObject.seat : '';
      this.price_econ = this.infosObject ? this.infosObject.price_econ : '';
    },
    immediate : true
  }
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
