<template>
  <v-app id="mainlayout">
    <navigation-drawer></navigation-drawer>
    <v-container>
      <v-content>
        <slot/>
      </v-content>
    </v-container>
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
  background: #f2f2f2;
  .container {
    max-width: 1400px;
  }
}
</style>


