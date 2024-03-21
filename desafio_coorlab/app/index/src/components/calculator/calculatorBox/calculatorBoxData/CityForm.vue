<template>
    <div id='calculatorCity'>
        <form>
            <label for="select">Destino</label>
            <select ref="cityForm" v-model="selectedCity" required>
                <option value="" disabled selected hidden>Selecione o destino</option>
                <option value="Campinas">Campinas</option>
                <option value="São Paulo">São Paulo</option>
                <option value="Santo André">Santo André</option>
            </select>
        </form>
    </div>
</template>

<script>
export default {
    name: 'CityForm',
    data() {
        return {
            selectedCity: ''
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