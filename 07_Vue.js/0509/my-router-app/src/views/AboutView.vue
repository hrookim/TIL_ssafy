<template>
  <div>
    This is About

    <button @click="moveToHome1">To Home</button>
    <button @click="moveToHome2">To Home</button>
    <button @click="moveToHome3">To Home</button>
    <button @click="moveToHome4">To Home</button>

  </div>
</template>

<script>
export default {
  name: 'AboutView',
  methods: {
    moveToHome1() {
      this.$router.push({name: 'home'})
    },
    moveToHome2() {
      this.$router.push('home') // localhost:8080/home으로 이동해줌 -> 지금 우리 상황에서는 아무 url과도 매칭되지 않는다.
    },
    moveToHome3() {
      this.$router.push({path: '/'})
    },
    moveToHome4() {
      this.$router.push({path: '/home'}) // 2와 똑같은 형태!!!
    },
  }
}
</script>

<style>

</style>