<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <!-- TODO: 보여주기 방식 -->
    <!-- <TheAbout/> -->
    <the-about my-message="This is prop data" theMessage="The Message" :parentData="parentData"
    @child-input-change="onBoss"></the-about>
  </div>
</template>

<script>
import TheAbout from '@/components/TheAbout.vue'

export default {
  name: 'App',
  components: {
    TheAbout
  },
  data() {
    return {
      parentData: 'This is Parent Data'
  }},
  methods: {
    onBoss(inputData) {
      console.log('들려들려...', '"'+inputData+'"')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
