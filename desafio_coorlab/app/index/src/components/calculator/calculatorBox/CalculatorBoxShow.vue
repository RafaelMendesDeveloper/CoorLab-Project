<template>
  <div id='calculatorShow'>
    <div v-if="companyName !== ''">
      <p class="text">Estas ão as melhores alternativas de viagem para a data selecionada</p>
      <div class="companies">
        <div class="confort">
          <div class="infosBox">
            <div class="iconBox">
              <img src="../../../assets/clock.png" alt="time image">
            </div>  
            <div class="infos">
              <span>{{ companyName }}</span>
              <p>Leito: {{ bed }}</p>
              <p>Tempo estimado: {{ duration }}</p>
            </div>
            <div class="priceBox">
              <span>Preço</span>
              <p>{{ price_confort }}</p>
            </div>
          </div>
        </div>
        <div class="econ">
          <div class="infosBox">
            <div class="iconBox">
              <img src="../../../assets/money.png" alt="economy image">
            </div>
            <div class="infos">
              <span>{{ companyName }}</span>
              <p>Assento: {{ seat }}</p>
              <p>Tempo estimado: {{ duration }}</p>
            </div>
            <div class="priceBox">
              <span>Preço</span>
              <p>{{ price_econ }}</p>
            </div>
          </div>
        </div>
      </div>
      <div>
        <button @click="cleanScreen" class="cleanButton">Limpar</button>
      </div>
    </div>
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
  },
  methods:{
    cleanScreen(){
      this.companyName ='';
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

.companies {
  display: flex;
  flex-direction: column;
  gap: .7rem;
  width: 100%;
}

.confort{
  display: flex;
  /* flex-direction: row; */
  align-items: center;
  justify-content: space-between;
  width: 30rem;
}

.econ{
  display: flex;
  flex-direction: row;
  align-items: center;
}

img {
  width: 2rem;
}

.iconBox {
  background-color: #00a8ba;
  width: 4rem;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 5px 0px 0px 5px;
  gap: .7rem;
}
 
.infosBox {
  display: flex;
  justify-content: flex-start;
}

.infos {
  background-color: #e2e2e2;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  border-radius: 0px 5px 5px 0px;
  padding: 1rem;
  width:20rem;

}

.priceBox {
  background-color: #e2e2e2;
  display: flex;
  width: 8rem;
  flex-direction: column;
  justify-content: center;
  align-items: flex-start;
  border-radius: 5px 5px 5px 5px;
  margin-left: .5rem;
  padding: 1rem;
}

h1 {
  font-size: 1.3rem;
  margin-bottom: 1rem;
}

span {
  font-size: 1rem;
  font-weight: bolder;
}

p {
  font-size: .85rem;
}

button{
        margin-top: 2rem;
        width: 100%;
        height: 2rem;
        background-color: #d2b409;
        border:none;
        border-radius: 5px;
        cursor: pointer;
    }

  .text{
    margin-bottom: 1rem;
  }
</style>
