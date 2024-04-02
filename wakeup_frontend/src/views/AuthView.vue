<template>
    <div class="flex h-dvh flex-col justify-center px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm">
            <div class="text-center text-3xl mb-8">
                WakeOnLan
            </div>
            <div v-show="authErrors.length">
                <div v-for="error in authErrors" class="p-3 bg-red-400 text-center rounded-lg mb-3 text-sm">
                    {{ error }}
                </div>
            </div>
            <form @submit.prevent="submitAuthForm" class="space-y-6">
                <div>
                    <wakeup-input id="username" v-model="authFormData.username">Доменное имя пользователя</wakeup-input>
                </div>

                <div>
                    <wakeup-input id="password" v-model="authFormData.password" type="password">Пароль</wakeup-input>
                </div>

                <div class="flex justify-center">
                    <button type="submit"
                        class="flex justify-center rounded-md bg-gray-600 px-12 py-1.5 text-sm font-semibold leading-6 text-white shadow-sm hover:bg-gray-500 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600">
                        Войти
                    </button>
                </div>
            </form>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import WakeupInput from '@/components/WakeupInput.vue'

export default {
    setup() {
        const userStore = useUserStore()

        return {
            userStore
        }
    },
    data() {
        return {
            authFormData: {
                username: "",
                password: ""
            },
            authErrors: []
        }
    },
    components: { WakeupInput },
    methods: {
        submitAuthForm() {
            this.authErrors = []
            axios
                .post('/api/token/', this.authFormData)
                .then(response => {
                    this.userStore.user.isAuthenticated = true
                    axios.defaults.headers.common['Authorization'] = 'Bearer ' + response.data.access
                    this.userStore.setTokens(response.data)
                    this.$router.push({ name: 'wakeup' })
                })
                .catch(error => {
                    if (error.response.status === 401) {
                        this.authErrors.push('Неверные учетные данные')
                    }
                    this.authFormData.username = ''
                    this.authFormData.password = ''
                })
        }
    }
}
</script>
