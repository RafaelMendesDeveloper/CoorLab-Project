<template>
  <div id='calculatorButton'>
    <button type="submit">Buscar</button>
  </div>
</template>

<script>
export default {
  name: 'SearchButton',
}
</script>

<style scoped>
    #calculatorButton{
        display: flex;
        justify-content: center;
        height: fit;
        width: fit;
        gap: 0.6rem;
        margin-left: 2rem;
        margin-right: 2rem;
    }

    button{
        margin-top: 2rem;
        width: 80%;
        height: 2rem;
        background-color: #04a8b3;
        border:none;
        border-radius: 5px;
        cursor: pointer;
    }
</style>