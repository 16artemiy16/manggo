<script setup lang="ts">

import DbsListItem from '@/components/DbsListItem.vue';
import { ref } from 'vue';
const items = ref([
  {
    name: 'users',
    collections: ['blocked', 'whitelist', 'peer']
  },
  {
    name: 'jira',
    collections: ['boards', 'tasks', 'users']
  },
])
</script>

<template>
  <div class="dbs">
    <b>-- Databases</b>
    <DbsListItem v-for="item in items" :key="item.name" :item="item" />
  </div>
</template>
