export default function({ store, redirect }) {
  if (!store.state.user.isSignedIn) {
    store.commit('ui/SET_SHOW_POPUP', {
      status: true,
      component: 'SignUp'
    })
    return redirect('/')
  }
}
