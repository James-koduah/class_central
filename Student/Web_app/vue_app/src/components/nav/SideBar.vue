<template>
    <div id="sidebar">
        <div id="sidebarMini" :style="{ marginLeft: expandSideBar ? '0%' : '-65px' }">
            <div class="miniItem" @click="expandSideBar = !expandSideBar"><SvgIcons icon="expandRight" color="white" /></div>
            <div class="group">
                <div class="miniItem" :class="{active: currentRoute === '/'}" @click="this.$router.push('/')"><SvgIcons icon="dashboard" color="white" /></div>
            </div>
            <div class="group">
                <div class="miniItem" :class="{active: currentRoute.startsWith('/courses')}" @click="this.$router.push('/courses')" ><SvgIcons icon="book" color="white" /></div>
                <div class="miniItem" :class="{active: currentRoute.startsWith('/assignments')}" @click="this.$router.push('/assignments')" ><SvgIcons icon="homework" color="white" /></div>
                <div class="miniItem" :class="{active: currentRoute.startsWith('/results')}" @click="this.$router.push('/results')" ><SvgIcons icon="studentResults" color="white" /></div>
            </div>
            <div class="group">
                <div class="miniItem" :class="{active: currentRoute.startsWith('/calender')}" @click="this.$router.push('/calender')" ><SvgIcons icon="calender" color="white" /></div>
                <div class="miniItem" :class="{active: currentRoute.startsWith('/events')}" @click="this.$router.push('/events')" ><SvgIcons icon="calenderEvent" color="white" /></div>
                <div class="miniItem" :class="{active: currentRoute.startsWith('/messages')}" @click="this.$router.push('/messages')" ><SvgIcons icon="message" color="white" /></div>
            </div>
            <div class="group">
                <div class="miniItem" :class="{active: currentRoute.startsWith('/profile')}" @click="this.$router.push('/profile')" ><SvgIcons icon="person" color="white" /></div>
                <div class="miniItem" :class="{active: currentRoute.startsWith('/settings')}" @click="this.$router.push('/settings')" ><SvgIcons icon="settings" color="white" /></div>
            </div>
            <div class="group">
                    <div class="miniItem" :class="{active: currentRoute.startsWith('/school')}" @click="this.$router.push('/school')" ><SvgIcons icon="school" color="white" /></div>
            </div>

        </div>
        <div id="sidebarMax" :style="{ left: expandSideBar ? '-100%' : '0%' }">
            <div class="maxItem" @click="expandSideBar = !expandSideBar"><SvgIcons icon="expandLeft" color="white" /></div>
            <div class="group">
                <div class="maxItem" :class="{active: currentRoute === '/'}" @click="this.$router.push('/')"> <SvgIcons icon="dashboard" color="white" /> <p>Dashboard</p></div>
            </div>
            <div class="group">
                <div class="maxItem" :class="{active: currentRoute.startsWith('/courses')}" @click="this.$router.push('/courses')"> <SvgIcons icon="book" color="white" /><p>Courses</p></div>
                <div class="maxItem" :class="{active: currentRoute.startsWith('/assignments')}" @click="this.$router.push('/assignments')"> <SvgIcons icon="homework" color="white" /><p>Assignments</p></div>
                <div class="maxItem" :class="{active: currentRoute.startsWith('/results')}" @click="this.$router.push('/results')"> <SvgIcons icon="studentResults" color="white" /><p>Results</p></div>
            </div>
            <div class="group">
                <div class="maxItem" :class="{active: currentRoute.startsWith('/calender')}" @click="this.$router.push('/calender')"> <SvgIcons icon="calender" color="white" /><p>Calender</p></div>
                <div class="maxItem" :class="{active: currentRoute.startsWith('/events')}" @click="this.$router.push('/events')"> <SvgIcons icon="calenderEvent" color="white" /><p>Events</p></div>
                <div class="maxItem" :class="{active: currentRoute.startsWith('/messages')}" @click="this.$router.push('/messages')"> <SvgIcons icon="message" color="white" /><p>Messages</p></div>
            </div>
            <div class="group">
                <div class="maxItem" :class="{active: currentRoute.startsWith('/profile')}" @click="this.$router.push('/profile')"> <SvgIcons icon="person" color="white" /><p>Profile</p></div>
                <div class="maxItem" :class="{active: currentRoute.startsWith('/settings')}" @click="this.$router.push('/settings')"> <SvgIcons icon="settings" color="white" /><p>Settings</p></div>
            </div>
            <div class="group">
                <div class="maxItem" :class="{active: currentRoute.startsWith('/school')}" @click="this.$router.push('/school')"> <SvgIcons icon="school" color="white" /><p>School</p></div>
            </div>
        </div>
    </div>
</template>
<script>
import SvgIcons from '../utils/SvgIcons.vue';

export default {
    components: {
        SvgIcons
    },
    data() {
        return {
            currentRoute: this.$route.path,
            expandSideBar: true
        }
    },
    watch: {
        $route(to) {
            this.currentRoute = to.path
        }
    }

}
</script>
<style scoped>
#sidebar {
    position: sticky;
    height: 100vh;
    top: 0;
    width: fit-content;
    min-width: 60px;
    color: var(--cool-white);
    flex-shrink: 0;
    z-index: 100;
    overflow-y: auto;
    overflow-x: hidden;
}
#sidebar::-webkit-scrollbar{
    width: 3px;
    display: none;
}
#sidebar::-webkit-scrollbar-track{
    background-color: transparent
}
#sidebar::-webkit-scrollbar-thumb{
    background-color: var(--oynx)
}

#sidebarMini {
    position: relative;
    width: 50px;
    height: fit-content;
    min-height: 100vh;
    padding: 5px 5px;
    background-color: var(--oynx);
    transition: .3s;
    z-index: 101;
}

.group {
    padding: 15px 0;
    border-bottom: 1px var(--text-light) solid;
}
.group:last-of-type{
    border: none;
}

.miniItem {
    width: 100%;
    height: 45px;
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 4px 0;
    --svg-width: 25px;
    --svg-height: 25px;
    cursor: pointer;
}
.miniItem:hover{
    background: var(--charcoal)
}



#sidebarMax {
    position: fixed;
    top: 0;
    left: 0;
    width: 200px;
    height: 100vh;
    padding: 5px;
    background-color: var(--oynx);
    transition: .7s cubic-bezier(1, 0, 0, 0.9);
    z-index: 102;
    overflow-y: auto;
}
#sidebarMax::-webkit-scrollbar{
    display: none;
}
.maxItem{
    width: calc(100% - 20px);
    height: 45px;
    display: flex;
    align-items: center;
    padding-left: 20px;
    margin: 4px 0;
    --svg-width: 25px;
    --svg-height: 25px;
    --svg-margin: 0 20px 0 0;
    font-size: 3em;
    cursor: pointer;
}
.maxItem:hover{
    background: var(--charcoal)
}


.active{
    background: var(--charcoal);
}

</style>