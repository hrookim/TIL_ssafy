<template>
  <div>
    <h1>User Profile</h1>
    <p>당신의 id는 {{user.userId}}</p>
    <p>당신의 article id는 {{user.articleId}}</p>
  </div>
</template>

<script>
export default {
  name: 'UserProfile',
  data() {
    return {
      user: this.$route.params
    }
  }

}
</script>

<style>

</style>