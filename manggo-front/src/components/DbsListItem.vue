<script setup lang="ts">
//eslint-disable-next-line no-undef
const props = defineProps({
  item: Object,
});
</script>

<template>
  <div class="dbs__item">
    <div>- {{ props.item.name }}</div>
    <div v-for="collection in props.item.collections" :key="collection">
      -- {{ collection }}
    </div>
  </div>
</template>
