import { GetterTree } from "vuex"
import RootState from "@/store/types/rootState"
import userState from "../../types/userState"

const getters: GetterTree<userState, RootState> = {
  isSignedIn: state => state.isSignedIn,
  currentUser: state => state.current,
  getUserProfile: state => state.userProfile,
  getAccessTokens: state => {
    return {
      acces_token: state.access_token,
      refresh_token: state.refresh_token
    }
  },
  currentUserId: state => state.current.userId
}

export default getters
