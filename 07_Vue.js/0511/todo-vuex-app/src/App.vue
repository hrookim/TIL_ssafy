<template>
  <div id="app">
    <h1>My Todos</h1>
    <p>전체 할일: {{todosCount}}</p>
    <p>끝난 일: {{ completedTodosCount }}</p>
    <todo-form></todo-form>
    <todo-list></todo-list>
  </div>
</template>

<script>
import TodoForm from '@/components/TodoForm.vue'
import TodoList from '@/components/TodoList.vue'

import {mapGetters, mapMutations} from 'vuex'

export default {
  name: 'App',
  components: {
    TodoForm, TodoList
  },
  computed: {
    ...mapGetters(['todosCount', 'completedTodosCount'])
  },
  methods: {
    ...mapMutations(['LOAD_TODOS'])
  },
  created() {
    this.LOAD_TODOS()
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
