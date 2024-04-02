<template>
    <div class="relative">
        <input @input="updateInput" :value="modelValue" :type="type" :id="id"
            class="block px-2.5 pb-2.5 pt-4 w-full text-sm text-gray-900 bg-transparent rounded-lg border-1 border-gray-300 appearance-none focus:outline-none focus:ring-0 focus:border-gray-600 peer"
            placeholder=" " />
        <label :for="id"
            class="absolute text-sm text-gray-500 duration-300 transform -translate-y-4 scale-75 top-2 z-10 origin-[0] bg-white  px-2 peer-focus:px-2 peer-focus:text-gray-600 peer-placeholder-shown:scale-100 peer-placeholder-shown:-translate-y-1/2 peer-placeholder-shown:top-1/2 peer-focus:top-2 peer-focus:scale-75 peer-focus:-translate-y-4 rtl:peer-focus:translate-x-1/4 rtl:peer-focus:left-auto start-1">
            <slot>Введите данные</slot>
        </label>
    </div>
    <div v-if="errors.length">
        <p v-for="error in errors" :key="error" class="mt-2 text-xs text-red-600 dark:text-red-400">{{ error instanceof
            Array ? error[0] : error }}</p>
    </div>
</template>

<script>
export default {
    name: 'WakeupInput',
    props: {
        modelValue: {
            type: [String, Number],
            default: ''
        },
        type: {
            type: String,
            default: 'text'
        },
        id: {
            type: [String, Number],
            default: 'floating_outlined'
        },
        errors: {
            type: Array,
            default: []
        }
    },
    methods: {
        updateInput(event) {
            this.$emit('update:modelValue', event.target.value)
        }
    }
}
</script>