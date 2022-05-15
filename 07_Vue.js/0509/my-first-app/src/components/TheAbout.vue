<template>
<div>
  <h1>About</h1>
  <div>
    <h3>{{ myMessage }}</h3>
    <h3>{{ theMessage }}</h3>
    <strong>{{ parentData }}</strong>
  </div>
  
  <div>
    <input type="text" v-model="childInputData" @keyup.enter="childInputEnter">
  </div>
</div>
</template>

<script>
export default {
  name: 'TheAbout',
  data() {
    return {
      childInputData: ''
    }
  },
  methods: {
    childInputEnter() {
      console.log('Enter', this.childInputData)
      // 부모 컴포넌트에세 boss라는 이름의 이벤트를 발생시킨다. 넘길 인자는 두번째 인자부터 작성하면 된다 
      this.$emit('child-input-change', this.childInputData, 123, 456, 789)
    }
  },
  props: {
    myMessage: String,
    theMessage: String,
    parentData: String
  }
}
</script>

<style>

</style>