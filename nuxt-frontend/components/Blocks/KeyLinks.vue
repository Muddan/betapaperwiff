<template>
  <v-scroll-y-transition>
    <div class="keylink-main">
      <v-subheader>
        <v-icon small left color="#fff">flare</v-icon>
        <h3 class="keylinks-title">Important Links</h3>
      </v-subheader>
      <div class="social-icons">
        <v-btn
          v-for="(icon, index) in socialIcons"
          :key="index"
          :href="icon.link"
          dark
          class="mx-2"
          icon
        >
          <v-icon class="socialIcon">{{ icon.name }}</v-icon>
        </v-btn>
      </div>
      <v-list class="link-list">
        <v-list-tile v-for="(keyLink, i) in keyLinks" :key="i">
          <v-list-tile-content>
            <nuxt-link class="page-link" :to="keyLink.link">
              <v-list-tile-title>{{ keyLink.title }}</v-list-tile-title>
            </nuxt-link>
          </v-list-tile-content>
        </v-list-tile>
      </v-list>
    </div>
  </v-scroll-y-transition>
</template>

<script>
export default {
  name: 'KeyLinks',
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
  margin-top: 20px;
  .v-list {
    border-radius: 8px;
    // border: 1px solid #337fb5;
    border-bottom: 4px solid #337fb5;
    box-shadow: 0 10px 20px 0 rgba(0, 0, 0, 0.05);
  }
  .keylinks-title {
    color: #fff;
    font-size: 16px;
    font-weight: bold;
    letter-spacing: 1px;
  }
  .link-list {
    background: #fff;
    .page-link {
      text-transform: capitalize;
      font-size: 14px;
      &:hover {
        color: #337fb5;
      }
    }
  }
}
</style>
