<template>
  <div class="keylink-main">
    <v-subheader>
      <v-icon color="#fff">bolt</v-icon>
      <span class="keylinks-title">Important Links</span>
    </v-subheader>
    <div class="social-icons">
      <v-btn dark v-for="icon in socialIcons" :key="icon" class="mx-2" icon>
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
  name: "KeyLinks",
  data() {
    return {
      socialIcons: [
        "fab fa-facebook",
        "fab fa-twitter",
        "fab fa-instagram",
        "fab fa-linkedin",
        "fa fa-envelope"
      ],
      keyLinks: [
        { title: "About", link: "/about" },
        { title: "Sponsors", link: "/about" },
        { title: " Privacy Policy", link: "/about" },
        { title: "Contact", link: "/about" },
        { title: "Faq", link: "/about" },
        { title: "Code of conduct", link: "/about" }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.keylink-main {
  background: #2a7b9c;
  border-radius: 8px;
  .v-list {
    border-radius: 8px;
    border: 1px solid #2a7b9c;
    border-bottom: 4px solid #2a7b9c;
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
    .v-btn {
      text-transform: capitalize;
    }
  }
}
</style>

