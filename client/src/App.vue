<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>

<style>
#app {
  color: rgb(255, 255, 255);
  background-color: rgb(0, 0, 0);
}
.container {
  align-items: center;
}
table, th, td {
  color: rgb(255, 255, 255);
  background-color: rgb(0, 0, 0);
}
h1 {
  color: rgb(190, 230, 255);
}
h2 {
  color: rgb(190, 230, 255);
}
</style>
