<template>
  <div class="contact-main">
    <v-container>
      <v-layout justify-center>
        <v-card class="contact-card">
          <v-card-title primary-title>
            <div>
              <h1 class="page-title">Contact Paperwiff !</h1>
              <p>We would love to hear from you!</p>
            </div>
          </v-card-title>
          <v-btn
            v-for="(icon, index) in socialIcons"
            :key="index"
            :href="icon.link"
            class="mx-2"
            icon
          >
            <v-icon class="socialIcon" size="24px">{{ icon.name }}</v-icon>
          </v-btn>
        </v-card>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  transition: 'slidedown',

  data() {
    return {
      socialIcons: [
        {
          name: 'fab fa-facebook',
          link: 'https://www.facebook.com/paperwiff/'
        },
        {
          name: 'fab fa-twitter',
          link: 'https://twitter.com/paperwiff?lang=en'
        },
        {
          name: 'fab fa-instagram',
          link: 'https://www.instagram.com/paperwiff/'
        }
      ]
    }
  }
}
</script>

<style lang="scss">
.contact-main {
  .contact-card {
    box-sizing: border-box;
    padding: 20px;
    border-radius: 8px;
    .page-title {
      color: #337fb5;
    }
  }
}
</style>
