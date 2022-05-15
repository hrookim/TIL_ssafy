import Vue from 'vue'
import Vuex from 'vuex'

import createPersistedState from 'vuex-persistedstate'

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    todoItem: '',
    todos: [
      {title:'저녁먹기', isCompleted:false, date: new Date().getTime()},
    ],
  },
  getters: {
    todosCount(state) {
      return state.todos.length
    },
    completedTodosCount(state) {
      const completedTodos = state.todos.filter(
        todo => {
          return todo.isCompleted
        }
      )
      return completedTodos.length
    }
  },
  mutations: {
    LOAD_TODOS(state) {
      const data = localStorage.getItem('todos')
      state.todos = JSON.parse(data)
    },
    CREATE_TODO(state, todoItem) {state.todos.push(todoItem)},
    UPDATE_TODOS(state, todoItem) {
      state.todos = state.todos.map(todo => {
        if (todo === todoItem) {
          return {
            ...todo,
            isCompleted: !todo.isCompleted
          }
        }
        return todo
      })
  },
    DELETE_TODO(state, todoItem) {
      const idx = state.todos.indexOf(todoItem)
      state.todos.splice(idx, 1)
    },
  },
  actions: {
    saveTodos({state}) {
      const strTodos = JSON.stringify(state.todos)
      localStorage.setItem('todos', strTodos)
    },
    createTodo({commit, dispatch}, todoItem) {
      commit('CREATE_TODO', todoItem)
      dispatch('saveTodos')
    },
    updateTodos({commit}, todoItem) {
      commit('UPDATE_TODOS', todoItem)
    },
    deleteTodo({commit}, todoItem) {
      if (confirm('진짜로.. 삭제하게..?')) {
        commit('DELETE_TODO', todoItem)
      }
    }
  },
  modules: {
  },
})
