import { defineStore } from 'pinia'
import axios from 'axios'


export const useUserStore = defineStore('user', {
    state: () => ({
        user: {
            isAuthenticated: false,
            id: null,
            username: null,
            accessToken: null,
            refreshToken: null,
        }
    }),
    actions: {
        async refreshToken() {
            try {
                const response = await axios.post('/api/token/refresh/', { refresh: this.user.refreshToken })
                this.user.accessToken = response.data.access
                localStorage.setItem('user.accessToken', response.data.access)

            } catch (error) {
                console.log(error)
                this.removeUserData()
            }
        },
        initUser() {
            if (localStorage.getItem('user.accessToken')) {
                this.user.isAuthenticated = true
                this.user.id = localStorage.getItem('user.id')
                this.user.username = localStorage.getItem('user.username')
                this.user.accessToken = localStorage.getItem('user.accessToken')
                this.user.refreshToken = localStorage.getItem('user.refreshToken')
            }
        },
        removeUserData() {
            this.user.isAuthenticated = false
            this.user.id = null
            this.user.username = null
            this.user.accessToken = null
            this.user.refreshToken = null

            localStorage.setItem('user.id', '')
            localStorage.setItem('user.username', '')
            localStorage.setItem('user.accessToken', '')
            localStorage.setItem('user.refreshToken', '')

            axios.defaults.headers.common['Authorization'] = ''

        },
        async getMe() {
            try {
                const response = await axios.get('/api/core/me/')
                localStorage.setItem('user.id', response.data.id)
                localStorage.setItem('user.username', response.data.username)
                this.user.id = response.data.id
                this.user.username = response.data.username
            } catch (error) {
                console.log(error)
                this.removeUserData()
            }
        },
        setTokens(data) {
            localStorage.setItem('user.accessToken', data.access)
            localStorage.setItem('user.refreshToken', data.refresh)
            this.user.accessToken = data.access
            this.user.refreshToken = data.refresh

            this.getMe()
        },


    }
})