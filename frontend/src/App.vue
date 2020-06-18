<template>
  <body>
    <todo-list list-name="Simple To Do App" />
  </body>
</template>

<script>
import TodoList from "./components/TodoList.vue";

export default {
  name: "App",
  components: {
    TodoList
  }
};
</script>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #dee2e6;
  margin-top: 60px;
}

// Colors
$bg-color: hsl(256, 33, 10);
$dot-color: hsl(256, 33, 70);

// Dimensions
$dot-size: 1px;
$dot-space: 22px;

body {
  background: linear-gradient(
        90deg,
        $bg-color ($dot-space - $dot-size),
        transparent 1%
      )
      center,
    linear-gradient($bg-color ($dot-space - $dot-size), transparent 1%) center,
    $dot-color;
  background-size: $dot-space $dot-space;
}
</style>
