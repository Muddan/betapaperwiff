import { GetterTree } from "vuex"
import RootState from "@/store/types/rootState"
import userState from "../../types/userState"

const getters: GetterTree<userState, RootState> = {
  isSignedIn: state => state.isSignedIn,
  currentUser: state => state.current
}

export default getters
