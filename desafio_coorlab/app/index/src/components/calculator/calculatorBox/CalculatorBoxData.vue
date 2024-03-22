<template>
  <div id="calculatorData">
    <CalculatorBoxDataText />
    <CityForm v-if="showCityForm" ref="cityForm" />
    <DateForm v-if="showDateForm" ref="dateForm" />
    <SearchButton @click="submitForm" />
    <div v-if="showModal" class="modal-mask">
        <ModalScreen @close-modal="closeModal"/>
    </div>
  </div>
</template>

<script>
import CalculatorBoxDataText from "./calculatorBoxData/Text";
import CityForm from "./calculatorBoxData/CityForm";
import DateForm from "./calculatorBoxData/DateForm";
import SearchButton from "./calculatorBoxData/SearchButton";
import ModalScreen from "./calculatorBoxData/ModalScreen";

export default {
  name: "CalculatorBoxData",

  components: {
    CalculatorBoxDataText,
    CityForm,
    DateForm,
    SearchButton,
    ModalScreen,
  },

  props: {
    transportData: {
      type: Array,
      required: true
    }
  },

  data() {
    return {
      showCityForm: true,
      showDateForm: true,
      showModal: false,
      selectedCity: '',
      economyPrice: ''
    };
  },

  methods: {
    submitForm() {
      if (!this.$refs.cityForm.selectedCity || !this.$refs.dateForm.selectedDate) {
        this.showModal = true;
      } else {
        this.selectedCity = this.$refs.cityForm.selectedCity;
        this.economyPrice = this.getEconomyPrice(this.selectedCity);
      }
    },
    closeModal() {
      this.showModal = false;
    },
    getEconomyPrice(city) {
      const transport = this.transportData.find(t => t.city === city);
      return transport ? transport.price_econ : "Não disponível";
    }
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
</style>
