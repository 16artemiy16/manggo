<script setup lang="ts">
import useState from '@/store';

const { toggleLeftSidebar } = useState();
</script>

<template>
  <header>
    <div>
      <button @click="toggleLeftSidebar" class="sidebar-toggler">&lt;--></button>
      <div class="spacer"></div>
    </div>
  </header>
</template>

<style scoped lang="scss">
header {
  width: 100%;
  border-bottom: 1px black solid;
  height: 100px;
}
</style>
