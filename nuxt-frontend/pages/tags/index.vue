<template>
  <div>
    404 Page-Not-Found
  </div>
</template>

<script>
export default {
  asyncData({ params, error }) {
    error({ statusCode: 404 })
  }
}
</script>

<style></style>
