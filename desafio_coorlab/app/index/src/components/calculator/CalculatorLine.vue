<template>
  <div id='stripe'>
    
  </div>
</template>

<script>
export default {
  name: 'CalculatorLine',
}
</script>

<style scoped>
#stripe {
  box-shadow: 0px 2px 2px rgba(0, 0, 0, 0.3);
  width: 100%;
  height: 3rem;
}

@media (max-width: 768px) {
#stripe{
    display: none;
}
}
</style>
