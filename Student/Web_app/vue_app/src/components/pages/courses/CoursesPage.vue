<template>
    <div class="page">
        <div class="search">
            <input type="text" placeholder="Search">
            <SvgIcons icon="search" color="#000" />
        </div>
        <div class="continueLearning">
            <header id="continueLearningHeader">Continue Learning</header>
            <div class="cLItems">
                <div class="cLItem"></div>
                <div class="cLItem"></div>
            </div>
        </div>
        <div class="allSubjects">
            <div class="allSubjectsHeader">All Subjects</div>
            <div class="allSubjectsTags">
                <div class="subjectTags">
                    <div class="tag">All Subjects</div>
                    <div class="tag">In Progress</div>
                    <div class="tag">Completed</div>
                </div>
                <div class="filter">
                    <div class="filterItem">
                        <SvgIcons icon="sort" color="#000"/>
                        <p>Sort By</p>
                    </div>
                </div>
            </div>
            <div class="subjects">
                <div class="subject"></div>
                <div class="subject"></div>
                <div class="subject"></div>
                <div class="subject"></div>
                <div class="subject"></div>
                <div class="subject"></div>
                <div class="subject"></div>
                <div class="subject"></div>
                <div class="subject"></div>
            </div>
        </div>
    </div>
</template>
<script>
import SvgIcons from '@/components/utils/SvgIcons.vue';

export default {
    components: {
        SvgIcons
    }
    
}
</script>
<style scoped>
.page{
    width: calc(100% - 20px);
    padding: 20px 10px 100px 10px;
}
.search{
    display: flex;
    align-items: center;
    --svg-width: 30px;
    --svg-height: 30px;
}
.search input{
    padding: 0 5px;
    width: 400px;
    height: 35px;
    box-shadow: var(--shadow);
    border-radius: 8px;
}
.continueLearning{
    margin-top: 50px;
}
#continueLearningHeader{
    font-size: 4.8em;
    font-weight: 600;
    margin-bottom: 7px;
}
.cLItems{
    width: 100%;
    display: flex;
}
.cLItem{
    width: 300px;
    height: 100px;
    border-radius: 8px;
    box-shadow: var(--shadow);
    margin-right: 30px;
}




.allSubjects{
    width: 100%;
    margin-top: 80px;
}
.allSubjectsHeader{
    font-size: 4.5em;
    margin-bottom: 5px;
}
.allSubjectsTags{
    width: 95%;
    margin-bottom: 30px;
    display: flex;
    justify-content: space-between;
}
.subjectTags{
    width: fit-content;
    display: flex;
}
.tag{
    padding: 7px 20px;
    border-radius: 14px;
    font-size: 2.5em;
    margin-right: 15px;
    background-color: var(--soft-gray);
}

.filter{
    display: flex;
}
.filterItem{
    display: flex;
    align-items: center;
    justify-content: center;
    --svg-width: 15px;
    --svg-height: 20px;
    padding: 2px 4px;
    box-shadow: var(--shadow);
    /* background-color: var(--soft-gray) */
}
.filterItem p{
    font-size: 2.8em;
    margin-left: 3px;
}



.subjects{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
}
.subject{
    width: 30%;
    height: 400px;
    max-width: 400px;
    box-shadow: var(--shadow);
    border-radius: 8px;
    margin-right: 3%;
    margin-bottom: 40px;
}
</style>