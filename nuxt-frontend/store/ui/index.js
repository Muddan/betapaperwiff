export const state = () => ({
  isShowPopup: false,
  componentName: ''
})
export const getters = {
  showPopup: state => state.isShowPopup
}
export const actions = {
  showPopup(context, payload) {
    context.commit('SET_SHOW_POPUP', payload)
  }
}
export const mutations = {
  SET_SHOW_POPUP(state, { status, component }) {
    state.isShowPopup = status
    state.componentName = component
  }
}
export const strict = false
