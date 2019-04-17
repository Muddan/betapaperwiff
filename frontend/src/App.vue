<template>
  <default-layout>
    <router-view/>
  </default-layout>
</template>
<script>
import DefaultLayout from "./layouts/DefaultLayout";

export default {
  name: "App",
  components: {
    DefaultLayout
  },
  beforeMount() {
    this.$store.dispatch("User/sessionStart");
    this.$store.dispatch("Stories/getAllStories");
    this.$store.dispatch("Stories/getStoryTags");
  }
};
</script>

<style lang="scss">
body {
  background: #f2f2f2;
  a {
    text-decoration: none;
    color: #2e2e2e;
  }
}

#nav {
  padding: 30px;
  a {
    font-weight: bold;
    color: #2c3e50;
    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
