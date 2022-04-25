<script setup lang="ts">
import ConnectionSidebar from '@/components/ConnectionSidebar.vue';
import ConnectionHeader from '@/components/ConnectionHeader.vue';
import ConnectionMain from '@/components/ConnectionMain.vue';

</script>

<template>
  <div class="connection-page">
    <ConnectionSidebar />
    <div class="content">
      <ConnectionHeader />
      <ConnectionMain />
    </div>
  </div>
</template>


<style scoped lang="scss">
.connection-page {
  display: flex;
  flex: 1;
}
.content {
  flex: 1;
}
</style>
