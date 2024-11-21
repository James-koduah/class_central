<template>
    <div class="page">
        <div class="mainHeader">
            <h1>Update Classroom</h1>
            <button @click="createClassroom">Update Classroom</button>
        </div>
        <div class="detailsContainer">
            <div class="detailsInfo">
                <div class="infoBox">
                    <h2>Update Information</h2>
                    <div class="infoItem">
                        <p>Classroom Name</p>
                        <input type="text" v-model="name">
                    </div>
                    <div class="infoItem">
                        <p>Select Homeroom Teacher</p>
                        <div class="shaded">{{ homeroomTeacher }}</div>
                        <button @click="openPopup('SelectTeacher', {})"  >Select</button>
                    </div>
                </div>
            </div>
        </div>
        <Popup 
        :isVisible="isPopupVisible" 
        :currentComponent="popupComponent"
        :componentData="popupProps"    
        @update:isVisible="isPopupVisible = $event" 
        />
    </div>
</template>
<script>
import Popup from '@/components/utils/Popup.vue';
import SvgIcons from '@/components/utils/SvgIcons.vue';
import SelectTeacher from '../SelectTeacher.vue';
import { useAppStore } from '@/store/appStore';
import apiClient from '@/axios';
import PopupMessage from '@/components/utils/PopupMessage.vue';

export default {
    props: {
        data: Object
    },
    setup() {
        return {
            appStore: useAppStore()
        }
    },
    components: {
        SvgIcons,
        Popup,
        SelectTeacher,
        PopupMessage
    },
    data() {
        return {
            name: '',
            homeroomTeacher: '',
            classroom_details: null,
            isPopupVisible: false,
            popupComponent: null,
            popupProps: {}
        }
    },
    methods: {
        openPopup(componentName, props) {
            if (componentName === 'SelectTeacher') this.popupComponent = SelectTeacher
            if (componentName === 'popupMessage') this.popupComponent = PopupMessage
            this.popupProps = props;
            this.isPopupVisible = true;
        },
        async createClassroom(){
            const response = await apiClient.post('/classrooms/update_classroom', {
                classroom_id: this.classroom_details.id,
                name: this.name,
                homeroom_teacher_id: null
            })
            if (response.data.status) window.location.reload()
            else {
                const info = {
                    type: 'error', 
                    header:'Process Failed', 
                    message: response.data.message
                }
                this.openPopup('popupMessage', info)
            }
        }
    },
    mounted(){
        this.classroom_details = this.appStore.findClassroom(this.data.id)
        this.name = this.classroom_details.name
        this.homeroomTeacher = this.classroom_details.homeroom_teacher
    }
}
</script>
<style scoped>
.page {
    width: 70vw;
    max-width: 700px;
    padding: 20px;
}

.mainHeader {
    display: flex;
    justify-content: space-between;
    margin-top: 30px;
}

.mainHeader h1 {
    font-size: 4.5em;
}

h2 {
    font-size: 4em;
    margin-bottom: 15px;
}

h3 {
    font-size: 3.5em;
    margin-bottom: 10px;
}

.mainHeader button {
    width: fit-content;
    box-shadow: 0px 1px 1px 1px var(--charcoal);
    padding: 10px 18px;
    border-radius: 15px;
    background: var(--oynx);
    color: #fff;
}

.detailsContainer {
    display: flex;
    width: 100%;
    justify-content: space-between;
    margin-top: 40px;
}

.detailsInfo {
    width: 100%;
    max-width: 700px;
}

.infoBox {
    width: calc(100% - 30px);
    padding: 15px;
    border: 1px var(--soft-gray) solid;
    border-radius: 14px;
    margin-bottom: 40px;
}

.infoItem {
    width: 100%;
    margin-bottom: 20px;
}

.half {
    width: 45% !important;
}

.infoItem p {
    font-size: 2.5em;
    font-weight: 600;
    margin-bottom: 5px;
}

.infoItem input {
    width: 94%;
    padding: 0 3%;
    height: 35px;
    border-radius: 5px;
    background: var(--soft-gray);
}

.infoItem textarea {
    width: 94%;
    padding: 10px 3%;
    height: 65px;
    border-radius: 5px;
    background: var(--soft-gray);
}

.infoItem button {
    padding: 8px 18px;
    box-shadow: var(--shadow);
    border-radius: 3px;
}

.shaded{
    width: 96%;
    padding: 0 2%;
    height: 35px;
    background: var(--soft-gray);
    display: flex;
    align-items: center;
    font-size: 2.5em;
}
</style>