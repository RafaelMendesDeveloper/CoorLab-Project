<template>
    <div id='calculatorCity'>
        <form>
            <label for="select">Destino</label>
            <select ref="cityForm" v-model="selectedCity" required @change="getTransport">
                <option value="" disabled selected hidden>Selecione o destino</option>
                <option v-for="city in cities" :key="city" :value="city">{{city}}</option>
            </select>
        </form>
    </div>
</template>

<script>
export default {
    name: 'CityForm',
    data() {
        return {
            selectedCity: '',
            cities: []
        }
    },
    async mounted(){
        await this.fetchCities();
    },
    methods: {
        async fetchCities() {
        const response = await fetch('http://localhost:5000/api/cities');
        console.log(response);
        this.cities = await response.json();
        },

        async getTransport() {
         console.log('Obtendo transporte para a cidade:', this.selectedCity);
         try {
             const response = await fetch(`http://localhost:5000/api/transport?city=${this.selectedCity}`);
             if (!response.ok) {
                 throw new Error('Erro ao obter dados de transporte: ' + response.statusText);
             }
             const transport = await response.json();
             console.log('Dados de transporte obtidos com sucesso:', transport);
         } catch (error) {
             console.error('Erro ao obter dados de transporte:', error);
         }
}

    }
}
</script>

<style scoped>
    #calculatorCity{
        margin-top: 1rem;
        height: 3rem;
        width: 80%;
        gap: 0.6rem;
        margin-left: 2rem;
        margin-right: 2rem;
    }

    select{
        height: 2rem;
        width: 100%;
        background-color: white;
        color: #bdbbbb;
        border: 1px solid;
        border-radius: 5px;
        cursor: pointer;
    }

    label{
        font-size: 10px;
        font-weight: bold;
    }

    @media (max-width: 768px) {
        select{
        width: 90%;
        font-size: 10px;
      }
    }
</style>