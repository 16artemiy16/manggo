<script setup lang="ts">
import useState from '@/store';
import DbsList from '@/components/DbsList.vue';

const state = useState();

</script>

<template>
  <div class="sidebar-opened">
    <div class="conn-addr">
      localhost:27017
    </div>
    <div class="conn-stats">
      <button class="conn-stats__toggler" @click="state.toggleConnectionDetails">
        <img v-if="state.isConnectionDetailsOpened" src="@/assets/icons/angle-down.svg" />
        <img v-else src="@/assets/icons/angle-up.svg" />
      </button>
      <div>
        59 DBS 1478 COLLECTIONS
      </div>
    </div>
    <div class="conn-details" v-if="state.isConnectionDetailsOpened">
      <div class="conn-details-row">
        HOST <br>
        localhost:27017
      </div>
      <div class="conn-details-row">
        CLUSTER <br>
        Unknown
      </div>
      <div class="conn-details-row">
        EDITION <br>
        MongoDB 4.2.1 Community
      </div>
    </div>
    <DbsList />
  </div>
</template>

<style scoped lang="scss">
.sidebar-opened {
  width: 300px;
  display: flex;
  flex-direction: column;
}

.conn-addr {
  display: flex;
  flex-direction: column;
  background: lightgray;
  padding: 0.5rem 1rem;
}

.conn-stats {
  display: flex;
  align-items: center;
  padding: .5rem;
  &__toggler {
    margin-right: .5rem;
  }
}

.conn-details {
  padding: 1rem 2rem;
}

.conn-details-row {
  margin-top: .5rem;
}
</style>
