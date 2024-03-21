<template>
  <div id="calculatorData">
    <CalculatorBoxDataText />
    <CityForm v-if="showCityForm" ref="cityForm" />
    <DateForm v-if="showDateForm" ref="dateForm" />
    <SearchButton @click="submitForm" />

    <!-- Modal customizado -->
    <div v-if="showModal" class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <img src="@/assets/error.png" alt="error" id="error">
          </div>
          <div class="modal-body">
            <p>Insira os valores para realizar a cotação.</p>
          </div>
          <div class="modal-footer">
            <button class="modal-default-button" @click="showModal = false">OK</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CalculatorBoxDataText from "./calculatorBoxData/Text";
import CityForm from "./calculatorBoxData/CityForm";
import DateForm from "./calculatorBoxData/DateForm";
import SearchButton from "./calculatorBoxData/SearchButton";

export default {
  name: "CalculatorBoxData",

  components: {
    CalculatorBoxDataText,
    CityForm,
    DateForm,
    SearchButton,
  },

  data() {
    return {
      showCityForm: true,
      showDateForm: true,
      showModal: false,
    };
  },

  methods: {
    submitForm() {
      if (!this.$refs.cityForm.selectedCity || !this.$refs.dateForm.selectedDate) {
        this.showModal = true;
      } else {
        // Se os formulários estiverem preenchidos, prosseguir com o envio dos dados
        console.log("Cidade selecionada:", this.$refs.cityForm.selectedCity);
        console.log("Data selecionada:", this.$refs.dateForm.selectedDate);
      }
    },
  },
};
</script>

<style scoped>
#calculatorData {
  width: 50%;
  height: 75%;
  background-color: #f8f4f4;
  margin-left: 2rem;
  margin-bottom: 2rem;
  border-radius: 10px;
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-wrapper {
  width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}

.modal-container {
  width: 300px;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 5px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
}

.modal-header{
  display: flex;
  justify-content: center;
}

.modal-header img{
    height: 2rem;
    width: 2rem;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  width: 100%;
  padding: 10px;
  background-color: #04a8b3;
  border: none;
  border-radius: 5px;
  color: #fff;
  cursor: pointer;
}

.modal-default-button:hover {
  background-color: #03848c;
}
</style>
