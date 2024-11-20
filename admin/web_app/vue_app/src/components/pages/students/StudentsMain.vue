<template>
    <div>
        <div class="blank">
            <header>Students Management</header>
            <input type="text" placeholder="Search Students Database">
        </div>
        <div class="database">
            <div class="actions">
                <div class="action">
                    <p>Actions</p>
                    <SvgIcons icon="caretDown" color="#000" />
                    <div class="actionOptions">
                        <p>Option Select</p>
                        <p>Option Select</p>
                        <p>Option Select</p>
                        <p>Option Select</p>
                    </div>
                </div>
                <div class="action">
                    <p>Filter</p>
                    <SvgIcons icon="filter" color="#000" />
                    <div class="actionOptions">
                        <p>Option Select</p>
                        <p>Option Select</p>
                        <p>Option Select</p>
                        <p>Option Select</p>
                    </div>
                </div>

                <div class="action addClassroom">
                    <p>Add New Student</p>
                    <SvgIcons icon="add" color="#000" />
                </div>

            </div>
            <div class="dbItems">
                <table>
                    <thead>
                        <tr>
                            <th>
                                <input type="checkbox" v-model="selectAll" @change="toggleSelectAll" />
                            </th>
                            <th v-for="(header, index) in headers" :key="index">{{ header }}</th>

                            <th>
                                Actions
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(row, rowIndex) in rows" :key="rowIndex">
                            <td>
                                <input type="checkbox" v-model="selectedRows[rowIndex]" />
                            </td>
                            <td v-for="(column, colIndex) in row" :key="colIndex">{{ column }}</td>
                            <td>
                                <div class="rowActions"><SvgIcons icon="menu2" color='#000' /></div>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>
<script>
import SvgIcons from '@/components/utils/SvgIcons.vue';

export default {
    components: {
        SvgIcons
    },
    data() {
        return {
            headers: ['Name', 'Classroom', 'Email', 'Guardian', 'Contact Number', 'Gender'],
            rows: [
                ['David Tompta', 'Grade 5', 'davidtompta@gmail.com', 'Mr. Tompta Joseph', '123456789', 'M'],
                ['Abigal Darko', 'Grade 4', 'abigaldarko@gmail.com', 'Mrs. Emilia Darko', '456789123', 'F'],
                ['Abraham Awo', 'Grade 5', 'abrahamawo@gmail.com', 'Mr. Justice Awo', '987654321', 'M'],
            ],
            selectedRows: new Array(3).fill(false),
            selectAll: false,
        };
    },
    methods: {
        toggleSelectAll() {
            this.selectedRows = this.selectedRows.map(() => this.selectAll);

        },
    },
    watch: {
        selectedRows(newVal) {
            this.selectAll = newVal.every(Boolean);
        },
    },
    computed: {
  },

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