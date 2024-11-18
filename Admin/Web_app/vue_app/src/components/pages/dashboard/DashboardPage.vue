<template>
    <div class="page">
    </div>
</template>
<script>
// import SvgIcons from '@/components/utils/SvgIcons.vue';
import { useAppStore } from '@/store/appStore';

export default {
    components: {
        // SvgIcons
    },
    setup(){
        return {
            appStore: useAppStore()
        }
    },
    methods: {
    }
}
</script>
<style scoped>
.page{
    width: calc(100% - 20px);
    padding: 10px 10px 100px 10px;
}
</style>