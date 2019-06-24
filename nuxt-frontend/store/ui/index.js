export const state = () => ({
  isShowPopup: false,
  componentName: '',
  isShowImageViewer: false,
  imageViewUrl: ''
})
export const getters = {
  showPopup: state => state.isShowPopup,
  imageViewUrl: state => state.imageViewUrl
}
export const actions = {
  showPopup(context, payload) {
    context.commit('SET_SHOW_POPUP', payload)
  },
  showImage(context, payload) {
    context.commit('SET_IMAGE_VIEWER', payload)
  }
}
export const mutations = {
  SET_SHOW_POPUP(state, { status, component }) {
    state.isShowPopup = status
    state.componentName = component
  },
  SET_IMAGE_VIEWER(state, payload) {
    state.isShowImageViewer = payload.status
    state.imageViewUrl = payload.imageViewUrl
  }
}
export const strict = false
