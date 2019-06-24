const actions = {
  info(context, payload) {
    this.$notify.info({
      class: 'notification-card',
      title: payload.title,
      message: payload.message,
      pauseOnHover: false,
      timeout: 3000,
      position: 'topRight',
      transitionIn: 'flipInX',
      transitionOut: 'flipOutX',
      transitionInMobile: 'flipInX',
      transitionOutMobile: 'flipOutX',
      progressBar: true
    })
  },
  success(context, payload) {
    this.$notify.success({
      class: 'notification-card',
      title: payload.title,
      message: payload.message,
      pauseOnHover: false,
      timeout: 3000,
      position: 'topRight',
      transitionIn: 'flipInX',
      transitionOut: 'flipOutX',
      transitionInMobile: 'flipInX',
      transitionOutMobile: 'flipOutX',
      progressBar: true
    })
  },
  warning(context, payload) {
    this.$notify.warning({
      class: 'notification-card',
      title: payload.title,
      message: payload.message,
      pauseOnHover: false,
      timeout: 3000,
      position: 'topRight',
      transitionIn: 'flipInX',
      transitionOut: 'flipOutX',
      transitionInMobile: 'flipInX',
      transitionOutMobile: 'flipOutX',
      progressBar: true
    })
  },
  error(context, payload) {
    this.$notify.error({
      class: 'notification-card',
      title: payload.title,
      message: payload.message,
      pauseOnHover: false,
      timeout: 3000,
      position: 'topRight',
      transitionIn: 'flipInX',
      transitionOut: 'flipOutX',
      transitionInMobile: 'flipInX',
      transitionOutMobile: 'flipOutX',
      progressBar: true
    })
  },
  progress(content, payload) {
    this.$notify.show({
      class: 'notification-card',
      title: payload.title,
      pauseOnHover: false,
      timeout: 2000,
      position: 'center',
      overlay: 'true',
      transitionIn: 'flipInX',
      transitionOut: 'flipOutX',
      progressBarColor: '#337fb5'
    })
  }
}

export default actions
