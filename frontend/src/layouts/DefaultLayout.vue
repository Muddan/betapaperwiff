<template>
  <v-app class="grey lighten-5" id="mainlayout">
    <navigation-drawer></navigation-drawer>
    <slot/>
    <footer-component></footer-component>
  </v-app>
</template>
<script>
import NavigationDrawer from "../components/NavigationDrawer";
import FooterComponent from "../components/FooterComponent";
export default {
  name: "DefaultLayout",
  components: {
    NavigationDrawer,
    FooterComponent
  },

  props: {
    source: String
  }
};
</script>
<style lang="scss" >
#mainlayout {
  background: #fff;
  .container {
    max-width: 1400px;
  }
}
</style>


