<template>
    <div id="container">
        <Search :searchFunction="appStore.classroomSearch" :activeStart="true"  @filteredItems="applyFilter" :liveUpdate="false" placeholder="Search Classrooms Database" />
        <div class="results"></div>
    </div>
</template>
<script>
import Search from '@/components/utils/Search.vue';
import { useAppStore } from '@/store/appStore';

export default {
    setup(){
        return {
            appStore: useAppStore()
        }
    },
    components: {
        Search
    },
    methods: {
        applyFilter(arg){
            let info = {
                source: 'selectClassroom',
                data: arg[0]
            }
            this.$emit('event', info)
        }
    },
    mounted(){
        this.appStore.loadClassroomsData()
    }

    
}
</script>
<style>
#container{
    width: 90vw;
    max-width: 500px;
}
.results{
    margin-top: 15px;
    width: 100%;
    min-height: 200px;
}
</style>