<template>
  <li id="calculator-menu">
    <a href="#">
      <img src="@/assets/calculator.png" alt="calculator" id="calculatorImage">
      <p>Calculadora de Viagem</p>
    </a>
  </li>
</template>

<style scoped>
#calculator-menu {
  margin-top: 2rem;
}

li {
  margin: 1rem 0 0 0.8rem;
}

a {
  text-decoration: none;
  display: flex;
  flex-direction: row;
  cursor: pointer;
}

li:hover p {
  font-size: 0.88em;
  margin-left: 0.2rem;
  transition: margin-left 0.5s ease, font-size 0.5s ease;
}

p {
  margin-left: 0.4rem;
  color: white;
  font-size: 0.8rem;
}
  
img{
    max-height: 1rem;
    max-width: 1rem;
}

</style>
