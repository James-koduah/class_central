<template>
    <div>
        <div class="blank">
            <header>Course Management</header>
            <div class="searchBox">
                <Search :searchFunction="appStore.teachersSearch"  @filteredItems="applyFilter" placeholder="Search Courses Database" />
            </div>
        </div>
        <div class="database">
            <div class="actions">
                <DropdownButton header="Actions" :options="['Delete']" @selected="" />
                <DropdownButton header="Sort By" icon="sort" :options="['Students No. Assending', 'Student No. Decending']" />

                <div class="action addClassroom" @click="openPopup('createCourse', {})" @selected="" >
                    <p>Add New Course</p>
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
                            <td>{{ row.name }}</td>
                            <td>{{ row.classroom }}</td>
                            <td>{{ row.teacher }}</td>
                            <td>{{ row.students ? row.students :  '0' }}</td>
                            <td><div class="rowActions"  @click="openPopup('updateCourse', {id: row.id})"><SvgIcons icon="menu2" color='#000' /></div></td>
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
import Popup from '@/components/utils/Popup.vue';
import AddCoursePage from './addcourse/AddCoursePage.vue';
import UpdateCoursePage from './updatecourse/UpdateCoursePage.vue';

export default {
    components: {
        SvgIcons,
        Search,
        Popup,
        DropdownButton,
        AddCoursePage,
        UpdateCoursePage
    },
    setup(){
        return {
            appStore: useAppStore()
        }
    },
    data() {
        return {
            headers: ['Name', 'Classroom', 'Teacher', 'Students Learning'],
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
        async loadCourses(){
            let data = this.appStore.getCourses
            if (data === false){
                data = await this.appStore.fetchCourses()
            }
            this.rows = data
            this.selectedRows = new Array(data.length).fill(false)
        },
        
        applyFilter(data){
            if (data.length > 0) this.rows = data
            else this.loadCourses()
        },
        openPopup(componentName, props) {
            if (componentName === 'updateCourse') this.popupComponent = UpdateCoursePage
            if (componentName === 'createCourse') this.popupComponent = AddCoursePage
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
        this.loadCourses()
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