export default function({ store, redirect }) {
  if (!store.state.user.isSignedIn) {
    store.dispatch('notification/warning', {
      title: '',
      message: 'You need to login to visit the page'
    })
    store.commit('ui/SET_SHOW_POPUP', {
      status: true,
      component: 'SignUp'
    })
    return redirect('/')
  }
}
