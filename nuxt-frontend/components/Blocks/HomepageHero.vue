<template>
  <div class="hero-main">
    <h1 class="welcome-title">Welcome to <strong>Paperwiff</strong></h1>
    <p class="main-info">
      A platform for Readers and Writers, for people to express themselves. We'd
      like you to go beyond social media. We know you all have a lot to say.
    </p>
    <!-- <router-link class="hero-know-more" to="/about">Know More</router-link> -->
    <div class="write-cta">
      <v-btn color="#337fb5" to="/write">
        <v-icon color="white" size="18px" left>fas fa-feather-alt</v-icon> Write
        Now
      </v-btn>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomepageHero'
}
</script>

<style lang="scss">
.hero-main {
  box-sizing: border-box;
  padding: 20px 15px;
  margin: 20px 0;

  .welcome-title {
    font-size: 50px;
    color: #2e2e2e;
    font-weight: normal;
  }
  .main-info {
    font-weight: 300;
    color: #2e2e2e;
    font-size: 18px;
    max-width: 60%;
    line-height: 35px;
  }
  .write-cta {
    margin-top: 40px;
    a {
      margin: 0;
      border: none;
      border-radius: 50px;
      outline: none;
      background: #337fb5;
      color: #fff;
      box-sizing: border-box;
      padding: 10px 20px;
      box-shadow: 0 10px 30px 0 rgba(75, 103, 249, 0.2);
      text-transform: capitalize;
    }
  }
  @media (max-width: 768px) {
    margin: 0 0 20px 0;
    .welcome-title {
      font-size: 36px;
    }
    .main-info {
      margin-top: 10px;
      font-size: 16px;
      max-width: 100%;
      line-height: 25px;
    }
    .write-cta {
      margin-top: 20px;
    }
  }
  .hero-know-more {
    margin: 10px 0;
    display: inline-block;
    font-weight: normal;
    letter-spacing: 1px;
    border-bottom: none;
    color: #337fb5;
    border-bottom: 1px solid #337fb5;
  }
}
</style>
