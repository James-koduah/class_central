<template>
    <div class='container'>
        <div class="header" :style="{background: backgound, color: color}" >{{ data.header }}</div>
        <div class="message">{{ data.message }}</div>
    </div>
</template>
<script>
export default {
    props: {
        data: Object
    },
    data(){
        return {
            backgound: 'var(--success-green)',
            color: '#fff'
        }
    },
    mounted(){
        if (this.data.type === 'error'){
            this.backgound = 'var(--error-red)'
        }else if(this.data.type === 'success'){
            this.backgound = 'var(--success-green)'
        }
    }
    
}
</script>
<style scoped>
    .container{
        width: 90vw;
        max-width: 350px;
    }
    .header{
        width: 80%;
        height: 100px;
        padding: 0px 10%;
        display: flex;
        justify-content: center;
        align-items: center;
        text-align: center;
        font-size: 3em;
    }
    .message{
        width: 90%;
        padding: 20px 5%;
        font-size: 2.7em;
        text-align: center;
    }
</style>