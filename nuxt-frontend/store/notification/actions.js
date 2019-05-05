const actions = {
  info(context, payload) {
    this.$notify.info({
      class: 'notification-card',
      title: payload.title,
      message: payload.message,
      pauseOnHover: false,
      timeout: 3000,
      position: 'topCenter',
      transitionIn: 'flipInX',
      transitionOut: 'flipOutX',
      progressBar: false
    })
  },
  success(context, payload) {
    this.$notify.success({
      class: 'notification-card',
      title: payload.title,
      message: payload.message,
      pauseOnHover: false,
      timeout: 3000,
      position: 'topCenter',
      progressBar: false
    })
  },
  warning(context, payload) {
    this.$notify.warning({
      class: 'notification-card',
      title: payload.title,
      message: payload.message,
      pauseOnHover: false,
      timeout: 3000,
      position: 'topCenter',
      progressBar: false
    })
  },
  error(context, payload) {
    this.$notify.error({
      class: 'notification-card',
      title: payload.title,
      message: payload.message,
      pauseOnHover: false,
      timeout: 3000,
      position: 'topCenter',
      progressBar: false
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
      progressBarColor: '#337fb5'
    })
  }
}

export default actions
