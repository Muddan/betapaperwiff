<template>
  <v-footer height="auto" color="#5199c3">
    <v-layout justify-center row wrap>
      <v-flex class="site-links" xs12>
        <v-btn
          v-for="(link, index) in keyLinks"
          :key="index"
          :to="link.link"
          color="white"
          flat
          round
        >
          {{ link.title }}
        </v-btn>
      </v-flex>
      <v-flex xs12 class="footer-info">
        <p class="footer-text">
          A platform for Readers and Writers, for people to express themselves.
          We'd like us to go beyond social media. We know you all have a lot to
          say. Remember this, "there’s always someone out there who could
          benefit from your experiences". We said “experiences”, not “expertise”
          because Paperwiff is for everyone.
        </p>
      </v-flex>
      <v-flex xs12 class="copyright" py-3 text-xs-center white--text>
        &copy;2019 — <strong>Paperwiff</strong>
      </v-flex>
    </v-layout>
  </v-footer>
</template>
<script>
export default {
  data: () => ({
    keyLinks: [
      { title: 'About', link: '/about' },
      // { title: 'Pricing', link: '/pricing' },
      { title: ' Privacy Policy', link: '/privacy-policy' },
      { title: 'Contact', link: '/contact' }
      // { title: 'Faq', link: '/faq' },
      // { title: 'Code of conduct', link: '/code-of-conduct' }
    ]
  })
}
</script>
<style lang="scss" scoped>
.copyright {
  background: #337fb5;
}
.footer-info {
  max-width: 60%;
  box-sizing: border-box;
  padding: 20px;
  border-top: 1px solid #fff;
  @media (max-width: 768px) {
    max-width: 100%;
  }
  .footer-text {
    color: #fff;
    text-align: center;
    font-size: 16px;
    @media (max-width: 768px) {
      font-size: 14px;
    }
  }
}
.site-links {
  text-align: center;
}
</style>
