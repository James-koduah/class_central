<template>
    <div class="page">
        <div class="mainHeader">
            <h1>Update Student</h1>
            <button @click="updateStudent">Update Student</button>
        </div>
        <div class="detailsContainer">
            <div class="detailsInfo">
                <div class="infoBox">
                    <h2>Update Information</h2>
                    <div class="infoItem">
                        <p>Name</p>
                        <input type="text" v-model="name">
                    </div>
                    <div class="infoItem">
                        <p>Email</p>
                        <input type="text" v-model="email">
                    </div>
                    <div class="infoItem">
                        <p>Phone</p>
                        <input type="text" v-model="phone">
                    </div>
                    <div class="infoItem">
                        <p>Guardian</p>
                        <input type="text" v-model="guardian">
                    </div>
                    <div class="infoItem">
                        <p>Gender</p>
                        <input type="text" v-model="gender">
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
import apiClient from '@/axios';
import PopupMessage from '@/components/utils/PopupMessage.vue';
import { useAppStore } from '@/store/appStore';

export default {
    setup() {
        return {
            appStore: useAppStore()
        }
    },
    props: {
        data: Object
    },
    components: {
        SvgIcons,
        Popup,
        PopupMessage
    },
    data() {
        return {
            honorific: '',
            name: '',
            email: '',
            phone: '',
            guardian: '',
            gender: '',
            student_details: null,
            isPopupVisible: false,
            popupComponent: null,
            popupProps: {},
        }
    },
    methods: {
        openPopup(componentName, props) {
            if (componentName === 'popupMessage') this.popupComponent = PopupMessage
            this.popupProps = props;
            this.isPopupVisible = true;
        },
        async updateStudent() {
            const response = await apiClient.post('/students/update_student', {  
                student_id: this.student_details.id,   
                name: this.name,
                email: this.email,
                phone: this.phone,
                guardian: this.guardian,
                gender: this.gender,
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
        }
    },
    mounted(){
        this.student_details = this.appStore.findStudent(this.data.id)
        this.name = this.student_details.name
        this.email = this.student_details.email
        this.phone = this.student_details.phone
        this.guardian = this.student_details.guardian
        this.gender = this.student_details.gender
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