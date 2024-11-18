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
input, textarea, button{
	border: none;
	color: inherit;
}
button, a{
    cursor: pointer;
}
button{
  background: inherit
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

</style>