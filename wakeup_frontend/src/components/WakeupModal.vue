<template>
    <div class="top-0 left-0 right-0 bottom-0 z-10 flex fixed bg-slate-200 opacity-50" v-if="isShow"
        @click="$emit('update:isShow', false)">
        <div class="dialog" @click.stop>
            <h1 style="text-align: center;">Введите IP</h1>
            <slot></slot>
        </div>
    </div>
</template>

<script>
export default {
    name: 'my-modal',
    props: {
        isShow: {
            type: Boolean,
            default: false,
        }
    }

}
</script>

<style scoped>
.dialog {
    background: white;
    width: 500px;
    height: 300px;
    margin: auto;
    padding: 20px 30px;
    display: flex;
    flex-direction: column;
    justify-content: center;
}
</style>