<script setup lang="ts">
import useStore from  '@/store/index.ts';

const store = useStore();

</script>

<template>
  {{ store.counter }}
  <button @click="store.counter++">+</button>
  <button @click="store.counter--">-</button>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">

</style>
