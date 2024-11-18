<template>
    <div class="page">
        <div class="date">{{ appStore.getDate() }}</div>
        <div class="courses">
            <header class="coursesHeader">Continue Classes</header>
            <div class="coursesSliderControl left" @click="scrollCourses(0)"><SvgIcons icon="arrowLeft" color="#000"/>  </div>
            <div class="coursesSliderControl right" @click="scrollCourses(1)"><SvgIcons icon="arrowRight" color="#000"/></div>
            <div class="coursesSliderCover" ref="coursesSliderCover">
                <div class="coursesSlider">    
                    <div class="course"></div>
                    <div class="course"></div>
                    <div class="course"></div>
                    <div class="course"></div>
                    <div class="course"></div>
                </div>
            </div>
        </div> 
        <div class="improve">
            <header id="improveHeader">Improve your subjects with these short lessons</header>
            <p id="improveSubHeader">Based on recent marked results</p>
            <div class="improveSuggestions">
                <div class="imsItems"></div>
                <div class="imsItems"></div>
                <div class="imsItems"></div>
            </div>
        </div>
        <div class="general">
            <div class="metrics"></div>
            <div class="assignments"></div>
            <div class="hours"></div>
        </div>
    </div>
</template>
<script>
import SvgIcons from '@/components/utils/SvgIcons.vue';
import { useAppStore } from '@/store/appStore';

export default {
    components: {
        SvgIcons
    },
    setup(){
        return {
            appStore: useAppStore()
        }
    },
    methods: {
        scrollCourses(arg){
            const div = this.$refs.coursesSliderCover
            let scrollAmount;
            if (arg == 0) scrollAmount = -200
            else scrollAmount = 200
            div.scrollBy({
                left: scrollAmount,
                behavior: "smooth",
            });
        }
    }
}
</script>
<style scoped>
.page{
    width: calc(100% - 20px);
    padding: 10px 10px 100px 10px;
}
.date{
    font-size: 2.3em;
    font-weight: 600;
    color: var(--text-deep);
    text-align: right;
}

.aqu{
    display: flex;
}
.courses{
    position: relative;
    width: 100%;
}
.coursesSliderControl{
    position: absolute;
    top: 0;
    width: 50px;
    height: 100%;
    background-color: #ffffff22;
    display: flex;
    justify-content: center;
    align-items: center;
    --svg-width: 20px;
    --svg-height: 20px;
    cursor: pointer;
}
.left{left: 0}
.right{right: 0}

.coursesSliderCover{
    width: 100%;
    overflow-x:  auto;
}
.coursesSliderCover::-webkit-scrollbar{
    display: none;
}
.coursesHeader{
    font-size: 3em;
    font-weight: 600;
    margin-bottom: 4px;
}
.coursesSlider{
    width: 100%;
    display: flex;
}
.course{
    width: 300px;
    height: 140px;
    background-color: #222;
    margin-right: 40px;
    flex-shrink: 0;
    border-radius: 9px;
}
.welcome{
    width: 250px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    flex-shrink: 0;
}
.welcome p{
    font-size: 2.8em;
}
.welcome header{
    font-size: 6em;
}



.improve{
    width: 100%;
    max-width: 1100px;
    margin-top: 40px;
}
#improveHeader{
    font-size: 3.8em;
    color: var(--blue);
}
#improveSubHeader{
    font-size: 2.8em;
    color: var(--text-light)
}
.improveSuggestions{
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
    margin-top: 5px;
}
.imsItems{
    width: 30%;
    height: 350px;
    border: 1px #ccc solid;
    box-shadow: var(--shadow);
    border-radius: 5px;
}



.general{
    width: 100%;
    display: flex;
    flex-wrap: wrap;
    margin-top: 80px;
    gap: 30px;
}
.metrics{
    width: 40%;
    height: 250px;
    min-width: 400px;
    border: 1px #ccc solid;
    box-shadow: var(--shadow);
    border-radius: 5px;
}
.assignments{
    width: 20%;
    min-width: 100px;
    max-width: 250px;
    border: 1px #ccc solid;
    box-shadow: var(--shadow);
    border-radius: 5px;
}

.hours{
    width: 30%;
    min-width: 100px;
    border: 1px #ccc solid;
    box-shadow: var(--shadow);
    border-radius: 5px;
}
</style>