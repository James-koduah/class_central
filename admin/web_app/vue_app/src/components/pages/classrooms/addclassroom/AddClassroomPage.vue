<template>
    <div class="page">
        <div class="mainHeader">
            <h1>Add New Classroom</h1>
            <button @click="createClassroom">Add Classroom</button>
        </div>
        <div class="detailsContainer">
            <div class="detailsInfo">
                <div class="infoBox">
                    <h2>Enter Information</h2>
                    <div class="infoItem">
                        <p>Classroom Name</p>
                        <input type="text" v-model="name">
                    </div>
                    <div class="infoItem">
                        <p>Select Homeroom Teacher</p>
                        <div @click="openPopup('SelectTeacher', {})" class="shaded">{{ homeroomTeacher }}</div>
                        <button @click="openPopup('SelectTeacher', {})">Select</button>
                    </div>
                </div>
            </div>
        </div>
        <Popup 
        :isVisible="isPopupVisible" 
        :currentComponent="popupComponent" 
        :componentData="popupProps"
        @update:isVisible="isPopupVisible = $event" 
        @event="managePopupEvent"
        />
    </div>
</template>
<script>
import Popup from '@/components/utils/Popup.vue';
import SvgIcons from '@/components/utils/SvgIcons.vue';
import SelectTeacher from '../../../utils/SelectTeacher.vue';
import apiClient from '@/axios';
import PopupMessage from '@/components/utils/PopupMessage.vue';

export default {
    setup() {
        return {
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
            isPopupVisible: false,
            homeroomTeacher: '',
            homeroom_teacher_id: null,
            popupComponent: null,
            popupProps: {},
        }
    },
    methods: {
        openPopup(componentName, props) {
            if (componentName === 'SelectTeacher') this.popupComponent = SelectTeacher
            if (componentName === 'popupMessage') this.popupComponent = PopupMessage
            this.popupProps = props;
            this.isPopupVisible = true;
        },
        async createClassroom() {
            const response = await apiClient.post('/classrooms/new_classroom', {
                name: this.name,
                homeroom_teacher_id: this.homeroom_teacher_id
            })
            if (response.data.status) {
                window.location.reload()
            }else {
                const info = {
                    type: 'error', 
                    header:'Process Failed', 
                    message: response.data.message
                }
                this.openPopup('popupMessage', info)
            }
        },
        managePopupEvent(data){
            this.isPopupVisible = false
            if (data.source == 'selectTeacher'){
                this.homeroom_teacher_id = data.data.id,
                this.homeroomTeacher = data.data.name
            }
        }
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

.shaded {
    width: 96%;
    padding: 0 2%;
    height: 35px;
    background: var(--soft-gray);
    display: flex;
    align-items: center;
    font-size: 2.5em;
}
</style>