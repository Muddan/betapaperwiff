<template>
  <div class="not-found-container">
    <v-container class="content-main">
      <img src="~assets/images/404.png" alt="page-not-found" />
      <div class="header">
        <h3>Sorry, the paper you are looking for is not available.</h3>
        <v-btn outline flat color="#2e2e2e">
          <nuxt-link to="/">Take me back to my Desk</nuxt-link>
        </v-btn>
      </div>
    </v-container>
  </div>
</template>

<script>
export default {}
</script>
<style lang="scss">
.not-found-container {
  background: #fcfffc;

  .content-main {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    height: 90vh;
    .header {
      text-align: center;
    }
    img {
      width: 400px;
      @media (max-width: 768px) {
        width: 250px;
      }
    }
  }
}
</style>
