<template>
  <div class="container">
    <div class="row">
      <div class="col-12 py-5">
        <h1>{{ listName }}</h1>
      </div>
    </div>
    <div class="row mb-3">
      <create-todo @on-new-todo="addTodo($event)" />
    </div>
    <div class="row">
      <div class="col-12 col-sm-10 col-lg-6">
        <ul class="list-group">
          <todo
            v-for="(todo, index) in todos"
            :key="index"
            :description="todo.description"
            :completed="todo.completed"
            @on-toggle="toggleTodo(todo)"
            @on-delete="deleteTodo(todo)"
            @on-edit="editTodo(todo, $event)"
          />
        </ul>
      </div>
    </div>
  </div>
</template>

<script>
import Todo from "./Todo.vue";
import CreateTodo from "./CreateTodo.vue";
import axios from "axios";

const endpoint = "http://127.0.0.1:50090/api/todos/";

export default {
  props: {
    listName: String
  },
  data() {
    return {
      todos: []
    };
  },
  mounted() {
    axios.get(endpoint).then(response => (this.todos = response.data));
  },
  methods: {
    addTodo(newTodo) {
      axios
        .post(endpoint, { description: newTodo })
        .then(response => (this.todos = response.data));
    },
    toggleTodo(todo) {
      let params = {
        id: todo.id,
        description: todo.description,
        completed: !todo.completed
      };
      axios
        .put(endpoint, params)
        .then(response => (this.todos = response.data));
    },
    deleteTodo(deletedTodo) {
      let params = { id: deletedTodo.id };
      axios
        .delete(endpoint, { data: params })
        .then(response => (this.todos = response.data));
    },
    editTodo(todo, newTodoDescription) {
      let params = {
        id: todo.id,
        description: newTodoDescription,
        completed: todo.completed
      };

      axios
        .put(endpoint, params)
        .then(response => (this.todos = response.data));
    }
  },
  components: { Todo, CreateTodo }
};
</script>

<style scoped lang="scss">
h1 {
  color: #dee2e6;
}
</style>
