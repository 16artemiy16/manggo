import { defineStore } from 'pinia';

export default defineStore('main', {
  state: () => ({
    isLeftSidebarOpened: true,
    isConnectionDetailsOpened: true,
  }),
  actions: {
    toggleLeftSidebar() {
      this.isLeftSidebarOpened = !this.isLeftSidebarOpened;
    },
    toggleConnectionDetails() {
      this.isConnectionDetailsOpened = !this.isConnectionDetailsOpened;
    }
  }
});
