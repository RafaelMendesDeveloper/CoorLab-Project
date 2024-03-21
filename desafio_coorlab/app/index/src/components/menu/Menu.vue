<template>
  <div class="menu">
    <ul>
      <Logo />
      <MenuItem />
    </ul>
  </div>
</template>

<script>
import Logo from './Logo.vue';
import MenuItem from './MenuItem.vue';

export default {
  name: 'MenuComponent',
  components: {
    Logo,
    MenuItem
  }
}
</script>

<style scoped>
.menu {
  position: fixed;
  left: 0;
  height: 100%;
  width: 12rem;
  background-color: #2a3041;
  transition: width 0.3s ease;
}

ul {
  list-style-type: none;
  padding-left: 0;
}

@media (max-width: 768px) {
  .menu {
    position: relative;
    width: 100%;
    padding-bottom: 1rem;
    display: flex;
    flex-direction: column;
    align-items: center;
  }

  p{
    color: white;
  }

  #calculator-menu {
    margin-left: -0.5rem;
  }
}
</style>
