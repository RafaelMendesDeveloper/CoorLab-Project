<template>
  <div class="modal-wrapper">
    <div class="modal-container">
      <div class="modal-header">
        <img src="@/assets/error.png" alt="error" id="error">
      </div>
      <div class="modal-body">
        <p>Insira os valores para realizar a cotação.</p>
      </div>
      <div class="modal-footer">
        <button class="modal-default-button" @click="closeModal">OK</button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ModalScreen",
  methods: {
    closeModal() {
      this.$emit('close-modal');
    }
  }
};
</script>

<style scoped>
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
