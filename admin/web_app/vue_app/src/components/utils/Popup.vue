<template>
    <div v-if="isVisible" class="popup-overlay fadein" ref="overlay">
        <div class="closeDiv" @click="closePopup"></div>
        <div class="popup-content slideup" ref="content">
            <div @click="closePopup" class="closeButton"><SvgIcons icon="close" color="#000" />  </div>
            <component :is="currentComponent" :data="componentData" @event="transmitEvent" />
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
        isVisible: {
            type: Boolean,
            required: true
        },
        currentComponent: {
            type: Object,  // Define it as an Object, as it will be a component
            required: true
        },
        componentData: {
            type: Object, // Define `componentData` according to the type you expect to receive
            required: true
        }
    },
    methods: {
        closePopup() {
            this.$refs.content.classList.add('slideDown')
            this.$refs.overlay.classList.add('fadeout')
            setTimeout(() => {
                this.$emit('update:isVisible', false);
            }, 300);   
        },
        transmitEvent(args={}){
            this.$emit('event', args)
        }
    },
    mounted(){
    }
}
</script>

<style scoped>
.popup-overlay {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    background: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 100;
    transition: 1s;
}
.closeDiv{
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
}
.closeButton{
    width: fit-content;
    position: relative;
    padding: 4px;
    --svg-width: 16px;
    --svg-height: 16px;
    border-radius: 9px;
    margin-bottom: 5px;
    margin-left: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;
}
.popup-content {
    background: white;
    padding: 20px;
    border-radius: 8px;
    z-index: 102;
    transition: 1s;
}

.slideup{
    animation: slideup .3s 1;
}
@keyframes slideup {
    0%{
        margin-top: 100vh;
        transform: scale(0.5);
    }
    100%{
        margin-top: 0vh;
        transform: scale(1)
    }
}

.slideDown{
    animation: slidedown .3s 1;
}
@keyframes slidedown {
    0%{
        margin-top: 0vh;
        transform: scale(1)
    }
    100%{
        margin-top: 100vh;
        transform: scale(0.5);
    }
}

.fadein {
    animation: fadein 0.3s ease-in-out 1;
}

@keyframes fadein {
    0% {
        opacity: 0;
    }
    100% {
        opacity: 1;
    }
}

.fadeout {
    animation: fadeout 0.3s ease-in-out 1;
}

@keyframes fadeout {
    0% {
        opacity: 1;
    }
    100% {
        opacity: 0;
    }
}
</style>