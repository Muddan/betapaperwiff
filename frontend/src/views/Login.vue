<template>
  <div id="login">
    <login-component></login-component>
  </div>
</template>
<script>
import LoginComponent from "@/components/Auth/LoginComponent.vue";
export default {
  name: "Login",
  components: {
    LoginComponent
  }
};
</script>
<style lang="scss" scoped>
#login {
  width: 100%;
  height: 100%;
}
</style>


