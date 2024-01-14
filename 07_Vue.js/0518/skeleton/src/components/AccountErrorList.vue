<template>
  <div class="account-error-list">
    <p v-for="(errors, field) in authError" :key="field">
      {{ field }} (***이건 나중에 안 띄워도 되는 아이다!)
      <ul>
        <li v-for="(error, idx) in errors" :key="idx">{{ error }}</li>
      </ul>
    </p>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

  export default {
    name: 'AccountErrorList',
    computed: {
      ...mapGetters(['authError'])
    },
  }
</script>

<style>
  .account-error-list {
    color: red;
  }
</style>
