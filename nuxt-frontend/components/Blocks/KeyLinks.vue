<template>
  <div class="keylink-main">
    <v-subheader>
      <v-icon color="#fff">bolt</v-icon>
      <span class="keylinks-title">Important Links</span>
    </v-subheader>
    <div class="social-icons">
      <v-btn v-for="icon in socialIcons" :key="icon" dark class="mx-2" icon>
        <v-icon class="socialIcon" size="24px">{{ icon }}</v-icon>
      </v-btn>
    </div>
    <v-list class="link-list">
      <v-list-tile v-for="(keyLink, i) in keyLinks" :key="i">
        <v-list-tile-content>
          <v-btn flat :to="keyLink.link">
            <v-list-tile-title>{{ keyLink.title }}</v-list-tile-title>
          </v-btn>
        </v-list-tile-content>
      </v-list-tile>
    </v-list>
  </div>
</template>

<script>
export default {
  name: 'KeyLinks',
  data() {
    return {
      socialIcons: [
        'fab fa-facebook',
        'fab fa-twitter',
        'fab fa-instagram',
        'fab fa-linkedin',
        'fa fa-envelope'
      ],
      keyLinks: [
        { title: 'About', link: '/about' },
        // { title: 'Pricing', link: '/pricing' },
        { title: ' Privacy Policy', link: '/privacy-policy' },
        { title: 'Contact', link: '/contact' }
        // { title: 'Faq', link: '/faq' },
        // { title: 'Code of conduct', link: '/code-of-conduct' }
      ]
    }
  }
}
</script>

<style lang="scss" scoped>
.keylink-main {
  background: #337fb5;
  border-radius: 8px;
  .v-list {
    border-radius: 8px;
    border: 1px solid #337fb5;
    border-bottom: 4px solid #337fb5;
  }
  .keylinks-title {
    color: #fff;
    font-size: 18px;
    letter-spacing: 2px;
  }
  .social-icons {
    text-align: center;
  }
  .link-list {
    background: #fff;
    .v-btn {
      text-transform: capitalize;
    }
  }
}
</style>
