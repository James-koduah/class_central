<template>
    <div>
        <div class="blank">
            <header>Teachers Management</header>
            <div class="searchBox">
                <Search :searchFunction="appStore.teachersSearch"  @filteredItems="applyFilter" placeholder="Search Teachers Database" />
            </div>
        </div>
        <div class="database">
            <div class="actions">
                <DropdownButton header="Actions" :options="['Delete']" @selected="" />
                <DropdownButton header="Sort By" icon="sort" :options="['Students No. Assending', 'Student No. Decending']" />

                <div class="action addClassroom" @click="openPopup('createTeacher', {})" @selected="" >
                    <p>Add New Teacher</p>
                    <SvgIcons icon="add" color="#000" />
                </div>

            </div>
            <div class="dbItems">
                <table>
                    <thead>
                        <tr>
                            <th><input type="checkbox" v-model="selectAll" @change="toggleSelectAll" /></th>
                            <th v-for="(header, index) in headers" :key="index">{{ header }}</th>
                            <th>Actions</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(row, rowIndex) in rows" :key="rowIndex">
                            <td><input type="checkbox" v-model="selectedRows[rowIndex]" /></td>
                            <td>{{row.honorific}}. {{ row.name }}</td>
                            <td>{{ row.email }}</td>
                            <td>{{ row.phone }}</td>
                            <td>{{ row.subjects }}</td>
                            <td>{{ row.position ? row.position : '-'  }}</td>
                            <td><div class="rowActions"  @click="openPopup('updateTeacher', {id: row.id})"><SvgIcons icon="menu2" color='#000' /></div></td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
        <Popup :isVisible="isPopupVisible" :currentComponent="popupComponent" :componentData="popupProps"
            @update:isVisible="isPopupVisible = $event" 
        />
    </div>
</template>
<script>
import { useAppStore } from '@/store/appStore';
import SvgIcons from '@/components/utils/SvgIcons.vue';
import Search from '@/components/utils/Search.vue';
import DropdownButton from '@/components/utils/DropdownButton.vue';
import AddTeacherPage from './addteacher/AddTeacherPage.vue';
import UpdateTeacherPage from './updateteacher/UpdateTeacherPage.vue';
import Popup from '@/components/utils/Popup.vue';

export default {
    components: {
        SvgIcons,
        Search,
        Popup,
        DropdownButton,
        AddTeacherPage,
        UpdateTeacherPage
    },
    setup(){
        return {
            appStore: useAppStore()
        }
    },
    data() {
        return {
            headers: ['Name', 'Email', 'Phone Number', 'Subjects Teaching', 'Position'],
            rows: [],
            selectedRows: [],
            selectAll: false,
            isPopupVisible: false,
            popupComponent: null,
            popupProps: {}
        };
    },
    methods: {
        toggleSelectAll() {
            this.selectedRows = this.selectedRows.map(() => this.selectAll);
        },
        async loadTeachersData(){
            let data = this.appStore.getTeachers
            if (data === false){
                data = await this.appStore.fetchTeachers()
            }
            this.rows = data
            this.selectedRows = new Array(data.length).fill(false)
        },
        applyFilter(data){
            if (data.length > 0) this.rows = data
            else this.loadTeachersData()
        },
        openPopup(componentName, props) {
            if (componentName === 'updateTeacher') this.popupComponent = UpdateTeacherPage
            if (componentName === 'createTeacher') this.popupComponent = AddTeacherPage
            this.popupProps = props;
            this.isPopupVisible = true;
        },
    },
    watch: {
        selectedRows(newVal) {
            this.selectAll = newVal.every(Boolean);
        },
    },
    mounted(){
        this.loadTeachersData()
    }

}
</script>
<style scoped>
.database {
    width: 86%;
    height: 100vh;
    background: var(--cool-white);
    border-radius: 10px;
    margin: -100px 5% 0 5%;
    padding: 10px 2%;
    border: 1px var(--soft-gray) solid;
}

.actions {
    width: 100%;
    display: flex;
}

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
    width: 150px;
    height: fit-content;
    background: var(--cool-white);
    border: 1px var(--soft-gray) solid;
    display: none;
}

.actionOptions p {
    width: 96%;
    padding: 5px 2%;
    color: var(--text-light)
}


.addClassroom {
    margin-left: auto;
    background: var(--success-green);
    color: var(--cool-white)
}


table {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
}
table input{
    padding: 0;
    box-shadow: none;
    width: 14px;
    height: 14px;
}
th,
td {
    padding: 10px;
    text-align: left;
}

th {
    background-color: #f4f4f4;
    font-size: 2.7em;
    font-weight: 600;
}

td {
    font-size: 2.6em;
}

.rowActions{
    width: fit-content;
    padding: 4px;
    --svg-width: 15px;
    --svg-height: 15px;
    border: 1px var(--soft-gray) solid;
    margin-left: 8px;
}
</style>