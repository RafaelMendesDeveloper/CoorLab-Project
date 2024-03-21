<template>
    <div id='calculatorDate'>
        <form>
            <label for="date">Data</label>
            <input ref="dateForm" v-model="selectedDate" type="date" required>
        </form>
    </div>
</template>

<script>
export default {
    name: 'DateForm',
    data() {
        return {
            selectedDate: ''
        }
    }
}
</script>


<style scoped>
    #calculatorDate{
        margin-top: 1rem;
        height: 3rem;
        width: 80%;
        gap: 0.6rem;
        margin-left: 2rem;
        margin-right: 2rem;
    }

    input{
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
        input{
        width: 90%;
        font-size: 10px;
      }
    }

</style>