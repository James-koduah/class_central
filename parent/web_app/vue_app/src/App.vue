<template>
  <div id="h"></div>
</template>

<script>
export default {
  name: 'App',
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
  --charcoal: #354555;
  --success-green: #27AE60;
  --error-red: #E74C3C;
  --text-normal: #34495E;
  --text-deep: #000;
  --text-light: #666;
  --mtn: #ffc403;
  --vodafone: #cc2131;
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
body::-webkit-scrollbar{
  width: 0;
}
#app{
  width: 100vw;
  height: fit-content;
  display: flex;
}

#shell{
  width: calc(100% - 60px);
  padding: 30px;
  min-height: 100vh;
  background: var(--cool-white);
}

.actionButton{
  padding: 8px 16px;
  border-radius: 15px;
  border: 1px var(--text-deep) solid;
  transition: .6s;
}
.actionButton:hover{
  background-color: var(--text-deep);
  color: var(--cool-white)
}
</style>