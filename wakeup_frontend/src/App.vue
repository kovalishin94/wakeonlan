<template>
  <RouterView />
  <WakeupToast />
</template>

<script>
import axios from 'axios'

import { useUserStore } from '@/stores/user'

import WakeupToast from '@/components/WakeupToast.vue'

export default {
  setup() {
    const userStore = useUserStore()


    return {
      userStore
    }
  },

  components: { WakeupToast },

  beforeCreate() {
    this.userStore.initUser()
    axios.defaults.headers.common['Authorization'] = 'Bearer ' + this.userStore.user.accessToken
  },
}
</script>