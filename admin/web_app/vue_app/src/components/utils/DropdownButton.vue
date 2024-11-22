<template>
    <div class="action" @click="dropdownVisible=!dropdownVisible">
        <p>{{ header }}</p>
        <SvgIcons :icon="icon" color="#000" />
        <div class="actionOptions" v-if="dropdownVisible">
            <p v-for="(option, index) in options" :key="index" @click="selectOption(option)" >{{option}}</p>
        </div>
    </div>
</template>
<script>
import SvgIcons from './SvgIcons.vue';

export default {
    components: {
        SvgIcons
    },
    props: {
        header: String,
        icon: {
            type: String,
            default: 'caretDown'
        },
        options: Array
    },
    data(){
        return {
            dropdownVisible: false
        }
    },
    methods: {
        selectOption(option){
            this.$emit('selected', option)
        }
    }
    
}
</script>
<style scoped>
.action {
    position: relative;
    padding: 10px 20px;
    box-shadow: var(--shadow);
    display: flex;
    --svg-width: 15px;
    --svg-height: 15px;
    border-radius: 3px;
    margin-right: 7px;
    cursor: pointer;
}

.action p {
    font-size: 2.5em;
    font-weight: 600;
    margin-right: 5px;
}

.actionOptions {
    position: absolute;
    top: 100%;
    left: 0px;
    width: fit-content;
    min-width: 150px;
    height: fit-content;
    background: var(--cool-white);
    border: 1px #aaa solid;
    border-radius: 4px;
    box-shadow: var(--shadow);
    padding-bottom: 10px;
    z-index: 1000;
}

.actionOptions p {
    width: calc(100% - 16px);
    padding: 5px 8px;
}
.actionOptions p:hover{
    background: var(--soft-gray);
}

    
</style>