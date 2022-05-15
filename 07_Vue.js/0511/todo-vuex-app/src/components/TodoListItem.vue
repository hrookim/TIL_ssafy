<template>
  <div>
    <span @click="updateTodos(todo)" :class="{'is-completed': todo.isCompleted}">{{todo.title}}</span>
    <button @click="deleteTodo(todo)">X</button>
    <button @click="printLog()">TEST</button>
  </div>
</template>

<script>
import {mapActions} from 'vuex'


export default {
  name: 'TodoListItem',
  props: {
    todo: Object
  },
  methods: {
    ...mapActions(['updateTodos', 'deleteTodo']),
    printLog(){
      console.log('실행됩니다.')
    }
  }

}
</script>

<style scoped>
.is-completed {
  text-decoration: line-through;
}

div {
  border: 2px solid black;
}

span:hover {
  cursor: pointer;
  background-color: rgb(218, 222, 222);
}
</style>