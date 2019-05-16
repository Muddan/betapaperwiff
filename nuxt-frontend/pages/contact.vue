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
          <v-btn v-for="icon in socialIcons" :key="icon" class="mx-2" icon>
            <v-icon class="socialIcon" size="24px">{{ icon }}</v-icon>
          </v-btn>
        </v-card>
      </v-layout>
    </v-container>
  </div>
</template>

<script>
export default {
  data() {
    return {
      socialIcons: [
        'fab fa-facebook',
        'fab fa-twitter',
        'fab fa-instagram',
        'fab fa-linkedin',
        'fa fa-envelope'
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
