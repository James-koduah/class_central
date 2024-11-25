<template>
    <div class="container">
        <input id="searchInput" type="text" :placeholder="placeholder" v-model="searchString" @input="runSearch" ref="input" >
        <div class="suggestions" v-if="dropdown && suggestions.length > 0">
            <p v-for="(item, index) in suggestions" :key="index" v-html="item.searchDisplayText" @click="emitOption([item])" ></p>
        </div>
    </div>
</template>
<script>
export default {
    props: {
        placeholder: {
            type: String,
            default: 'Search'
        },
        searchFunction: {
            type: Object
        },
        dropdown: { // Set to false to not display the dropdown selections
            type: Boolean,
            default: true
        },
        liveUpdate: { // When true, each input into the search bar will transmit the results to the parent
            type: Boolean,
            default: true
        },
        activeStart: {
            type: Boolean, // When true, on mount the input becomes active
            default: false
        }
    },
    data(){
        return {
            suggestions: [],
            searchString: ''
        }
    },
    methods: {
        runSearch(){
            this.suggestions = this.searchFunction(this.searchString)
            if (this.liveUpdate){
                this.emitOption(this.suggestions)
            }
        },
        emitOption(value){
            this.$emit('filteredItems', value)
        }
    },
    mounted() {
        if (this.activeStart){
            this.$refs.input.focus()
        }
    }
    
}
</script>
<style scoped>
.container{
    position: relative;
    width: 100%;
}
#searchInput{
  width: 96%;
  padding: 0 2%;
  height: 35px;
}
.suggestions{
    position: absolute;
    top: 100%;
    left: 0px;
    width: 100%;
    padding: 10px 0;
    background: var(--cool-white);
    border: 1px var(--soft-gray) solid;
    z-index: 800;
}
.suggestions p{
    width: calc(100% - 20px);
    padding: 8px 10px;
    font-size: 2.4em;
}
.suggestions p:hover{
    background: var(--soft-gray);
    cursor: pointer
}
    
</style>