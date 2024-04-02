<template>
    <div class="flex flex-col justify-center text-2xl text-center mt-4">
        <button @click="logOut"
            class="place-self-end mr-4 rounded-md bg-gray-100 px-3 py-2 text-sm font-semibold text-black shadow-sm hover:bg-gray-300 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-gray-600">Выход</button>
        <p>Добро пожаловать,</p>
        <p class="mb-3">{{ myPcInfo.first_name }} {{ myPcInfo.last_name }}</p>
        <p class="text-sm" v-show="myPcInfo.computername">Имя ПК: {{ myPcInfo.computername }}</p>
        <p class="text-sm" v-show="myPcInfo.ip_address">IP: {{ myPcInfo.ip_address }}</p>
        <p class="text-sm" v-show="myPcInfo.mac">MAC: {{ myPcInfo.mac }}</p>
    </div>
    <svg @click="wakeUpComputer" class="absolute left-0 right-0 top-0 bottom-0 m-auto h-1/4 w-1/4 z-0" version="1.1"
        :class="[myPcInfo.is_running ? 'fill-emerald-400 cursor-not-allowed' : 'fill-red-500 cursor-pointer']"
        xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" viewBox="0 0 496.158 496.158"
        xml:space="preserve">
        <path d="M496.158,248.085c0-137.021-111.07-248.082-248.076-248.082C111.07,0.003,0,111.063,0,248.085
	c0,137.002,111.07,248.07,248.082,248.07C385.088,496.155,496.158,385.087,496.158,248.085z" />
        <g>
            <path style="fill:#ffffff;" d="M373.299,154.891c-19.558-26.212-47.401-46.023-78.401-55.787c-0.759-0.238-1.588-0.103-2.229,0.369
		c-0.643,0.471-1.021,1.22-1.021,2.016l0.16,40.256c0,1.074,0.514,2.06,1.332,2.562c31.732,19.456,66.504,47,66.504,103.237
		c0,61.515-50.047,111.56-111.562,111.56c-61.517,0-111.566-50.045-111.566-111.56c0-58.737,35.199-84.661,67.615-103.917
		c0.836-0.496,1.363-1.492,1.363-2.58l0.154-39.909c0-0.793-0.375-1.539-1.013-2.01c-0.638-0.472-1.46-0.611-2.219-0.381
		c-31.283,9.586-59.41,29.357-79.202,55.672c-20.467,27.215-31.285,59.603-31.285,93.662c0,86.099,70.049,156.146,156.152,156.146
		c86.1,0,156.147-70.047,156.147-156.146C404.228,214.235,393.533,182.01,373.299,154.891z" />
            <path style="fill:#ffffff;" d="M251.851,67.009h-7.549c-11.788,0-21.378,9.59-21.378,21.377v181.189
		c0,11.787,9.59,21.377,21.378,21.377h7.549c11.788,0,21.378-9.59,21.378-21.377V88.386
		C273.229,76.599,263.64,67.009,251.851,67.009z" />
        </g>
    </svg>
    <svg v-if="showSpinner" aria-hidden="true"
        class="absolute left-0 right-0 top-0 bottom-0 m-auto w-1/3 h-1/3 text-gray-200 animate-spin fill-gray-600 z-0"
        viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
        <path
            d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z"
            fill="currentColor" />
        <path
            d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z"
            fill="currentFill" />
    </svg>
</template>

<script>
import axios from 'axios'
import { useUserStore } from '@/stores/user'
import { useToastStore } from '@/stores/toast'

export default {
    setup() {
        const userStore = useUserStore()
        const toastStore = useToastStore()

        return {
            userStore, toastStore
        }
    },
    data() {
        return {
            modalShow: true,
            showSpinner: false,
            myPcInfo: {
                last_name: '',
                first_name: '',
                computername: '',
                ip_address: '',
                mac: '',
                is_running: false
            },
        }
    },
    mounted() {
        this.getMyPcInfo()
    },
    methods: {
        async getMyPcInfo() {
            this.showSpinner = true
            try {
                const response = await axios.get('/api/core/get-my-pc/')
                this.myPcInfo = response.data.info
                if (response.data.message) {
                    if (response.status == 200) {
                        this.toastStore.showToast(5000, response.data.message, 'bg-emerald-400')
                    } else {
                        this.toastStore.showToast(5000, response.data.message, 'bg-red-400')
                    }
                }
            } catch (error) {
                this.logOut()
                console.log(error)
            }
            this.showSpinner = false
        },
        async wakeUpComputer() {
            if (this, this.myPcInfo.is_running) {
                this.toastStore.showToast(5000, 'ПК уже запущен', 'bg-emerald-400')
                return
            }
            if (!this.myPcInfo.ip_address) {
                this.toastStore.showToast(5000, 'Не известен IP адрес', 'bg-red-400')
                return
            }
            this.showSpinner = true
            try {
                const response = await axios.post('/api/core/wake-up/', { ip_address: this.myPcInfo.ip_address, mac: this.myPcInfo.mac })
                this.myPcInfo.is_running = response.data.is_running
                if (this.myPcInfo.is_running) {
                    this.toastStore.showToast(5000, response.data.message, 'bg-emerald-400')
                } else {
                    this.toastStore.showToast(5000, response.data.message, 'bg-red-400')
                }
            } catch (error) {
                if (error.response.data.message) {
                    this.toastStore.showToast(5000, error.response.data.message, 'bg-red-400')
                }
                if (error.response.status == 401) {
                    this.logOut()
                }
            }
            this.showSpinner = false
        },

        logOut() {
            this.userStore.removeUserData()
            this.$router.push({ name: 'auth' })
        }
    }
}
</script>