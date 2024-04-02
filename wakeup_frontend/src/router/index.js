import { createRouter, createWebHistory } from 'vue-router'
import { useUserStore } from '@/stores/user'
import AuthView from '@/views/AuthView.vue'
import NotFoundView from '@/views/NotFoundView.vue'
import WakeupView from '@/views/WakeupView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'auth',
      component: AuthView
    },
    {
      path: '/wakeup',
      name: 'wakeup',
      component: WakeupView,
      meta: {
        requiresAuth: true
      }
    },
    {
      path: '/:pathMatch(.*)*',
      name: 'notfound',
      component: NotFoundView,
      meta: {
        requiresAuth: true
      }
    },
  ]
})

router.beforeEach((to, from, next) => {
  const userStore = useUserStore()
  if (to.matched.some(record => record.meta.requiresAuth) && !userStore.user.isAuthenticated) {
    next({ name: 'auth' })
  } else if (to.name === 'auth' && userStore.user.isAuthenticated) {
    next({ name: 'wakeup' })
  } else {
    next()
  }

  if (userStore.user.isAuthenticated) {
    userStore.getMe()
  }
})

export default router
