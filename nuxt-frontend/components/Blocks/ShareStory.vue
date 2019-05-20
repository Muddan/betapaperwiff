<template>
  <social-sharing :url="url" inline-template>
    <div class="links-main">
      <ul>
        <li>
          <network network="facebook">
            <i class="fab fa-facebook" aria-hidden="true"></i>
          </network>
        </li>
        <li>
          <network network="twitter">
            <i class="fab fa-twitter" aria-hidden="true"></i>
          </network>
        </li>
        <li>
          <network network="whatsapp">
            <i class="fab fa-whatsapp" aria-hidden="true"></i>
          </network>
        </li>
        <li>
          <network network="linkedin">
            <i class="fab fa-linkedin" aria-hidden="true"></i>
          </network>
        </li>
      </ul>
    </div>
  </social-sharing>
</template>

<script>
export default {
  name: 'ShareStory',
  props: {
    url: {
      type: String,
      default: ''
    }
  }
}
</script>
<style lang="scss">
.links-main {
  ul {
    list-style: none;
    margin: 0;
    padding: 0;
    li {
      box-sizing: border-box;
      padding: 10px;
      margin-bottom: 5px;

      cursor: pointer;
      i {
        font-size: 24px;
      }
    }
  }
}
</style>
