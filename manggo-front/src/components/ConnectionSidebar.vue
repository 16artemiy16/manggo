<script setup lang="ts">
import { toRefs } from 'vue';
import useState from '@/store';
import ConnectionSidebarOpened from '@/components/ConnectionSidebarOpened.vue';
import ConnectionSidebarClosed from '@/components/ConnectionSidebarClosed.vue';

const { isLeftSidebarOpened } = toRefs(useState());

</script>

<template>
  <aside class="aside">
    <div class="aside-content">
      <ConnectionSidebarOpened v-if="isLeftSidebarOpened" />
      <ConnectionSidebarClosed v-else />
    </div>
  </aside>
</template>

<style scoped lang="scss">
.spacer {
  flex: 1;
}

.aside {
  display: flex;
  &-content {
    border: 1px black solid;
    width: fit-content;
  }
}
</style>
