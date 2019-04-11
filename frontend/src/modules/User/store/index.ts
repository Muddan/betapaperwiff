import RootState from '@/store/types/rootState';
import { Module } from 'vuex';
import UserState from '../../types/userState';
const User: Module<UserState, RootState> = {
  namespaced: true,
  state: {
    isSignedIn: false,
    current: null,
    session_started: new Date().toLocaleString(),
  },
};
export default User;
