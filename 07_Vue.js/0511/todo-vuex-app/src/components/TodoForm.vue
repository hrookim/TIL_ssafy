<template>
  <div>
    <input type="text" v-model.trim="todoTitle" @keyup.enter="createTodoItem"> 
    <button>제출</button>
  </div>
</template>

<script>
import {mapActions} from 'vuex'

export default {
  name: 'TodoForm',
  data() {
    return {
      todoTitle: '',
    }
  },
  methods: {
    ...mapActions(['createTodo']),
    createTodoItem() {
      const newTodo = {
        title: this.todoTitle,
        isCompleted: false,
        data: new Date().getTime()
      }
      this.createTodo(newTodo)
      this.todoTitle = ''
    }
  }

}
</script>

<style>

</style>