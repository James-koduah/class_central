<template>
  <main id="main">
    <SideBar />
    <div id="shell">
      <RouterView />
    </div>
  </main>
</template>

<script>
import SideBar from './components/nav/SideBar.vue';

export default {
  name: 'App',
  components: {
    SideBar
  }
}
</script>

<style>
@font-face {
    font-family: 'Cabin';
    src: url('@/assets/fonts/Cabin-VariableFont_wdth,wght.ttf') format('truetype');
    font-weight: 100 900;
    font-style: normal;
}

*{
  padding: 0;
  margin: 0
}

:root{
  --cool-white: #fafafc;
  --white: #ffffff;
  --deep-blue: #202531;
  --soft-gray: #e3e8e9;
  --charcoal: #282828;
  --slate-black: #1b1b1b;
  --success-green: #27AE60;
  --error-red: #E74C3C;
  --text-normal: #202122;
  --text-deep: #000;
  --text-light: #666;
  --yellow: #ffc403;
  --blue: #0066ff;
  --bright-red: #cc2131;
  --oynx: #121212;
  --shadow: 0px 2px 2px 2px var(--soft-gray);

}

input:focus, textarea:focus{
    outline: none;
}
input, textarea{
	border: none;
	color: inherit;
  border-radius: 8px;
  box-shadow: var(--shadow);
  width: 96%;
  padding: 0 2%;
  height: 35px;
}
button, a{
    cursor: pointer;
}
button{
  background: inherit;
	border: none;
	color: inherit;
}
a{
    text-decoration: none;
    color: inherit;
}
img{
    width: 100%;
    height: 100%;
    object-fit: cover;
}
a{
    text-decoration: none;
}
body{
  width: 100vw;
  height: fit-content;
  font-size: 5px;
  font-family: 'Cabin';
  color: var(--text-normal);
  overflow-x: hidden;
}
#main{
  width: 100%;
  display: flex;
}
#app{
  width: 100vw;
  height: fit-content;
  display: flex;
}

#shell{
  width: calc(100% - 60px);
  min-height: 100vh;
  background: var(--cool-white);
}

.blank{
  width: 90%;
  background: var(--slate-black);
  color: var(--cool-white);
  padding: 100px 5% 200px 5%;
  display: flex;
  flex-direction: column;
  align-items: center;
}
.blank header{
    font-size: 7em;
}
.blank input{
  margin-top: 35px;
  width: 60%;
}


.goBack{
  width: fit-content;
  height: fit-content;
  padding: 10px;
  --svg-width: 25px;
  --svg-height: 25px;
  margin-bottom: 20px;
  box-shadow: 0px 2px 2px 2px var(--soft-gray);
  border-radius: 5px;
  cursor: pointer;
}
</style>