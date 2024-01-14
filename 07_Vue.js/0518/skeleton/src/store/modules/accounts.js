import router from '@/router'
import axios from 'axios'
import drf from '@/api/drf'

export default {
  // namespaced: true,

  // 직접 접근하지 않겠다!
  state: {
    token: localStorage.getItem('token') || '',  // 로그인했을 때 반환받는 Token (key에 대한 value)
    currentUser: {},  // token 값 기반현재 유저
    profile: {},  // 누구의 프로필인지
    authError: null,  // 회원가입 혹은 로그인 실패시 오는 에러메시지
  },
  // 모든 state는 getters를 통해서 접근하겠따! -> 우리가 다른 컴포넌트에서 mapGetters만 소환할 것이다
  getters: {
    isLoggedIn(state) {return !!state.token},
    currentUser(state) {return state.currentUser},
    profile(state) {return state.profile},
    authError(state) {return state.authError},
    authHeader(state) {return {'Authorization': `Token ${state.token}`}} // 객체임을 나타내기 위해 소괄호->객체중괄호
  },

  mutations: {
    SET_TOKEN: (state, token) => state.token = token,
    SET_CURRENT_USER: (state, user) => state.currentUser = user,
    SET_PROFILE: (state, profile) => state.profile = profile,
    SET_AUTH_ERROR: (state, error) => state.authError = error
  },

  actions: {
    saveToken({ commit }, token) {
     commit('SET_TOKEN', token)  // state.token 추가 
     localStorage.setItem('token', token) // localStorage에 token 추가
    },
    removeToken({ commit }) {
      commit('SET_TOKEN', '')  // state.token 추가 
      localStorage.setItem('token', '') // localStorage에 token 추가
    },

    login({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 login URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.login(),
        method: 'post',
        data: credentials
      })
        .then(res => {
          const token = res.data.key
          dispatch('saveToken', token)
          dispatch('fetchCurrentUser')
          router.push({name: 'articles'})
        })
        .catch(err => {
          console.log(err.response.data)
          commit('SET_AUTH_ERROR', err.response.data)
          // if (err.response.status === 404) {
          //   router.push({name: 'NotFound404'})
          // }
        })
    },

    signup({ commit, dispatch }, credentials) {
      /* 
      POST: 사용자 입력정보를 signup URL로 보내기
        성공하면
          응답 토큰 저장
          현재 사용자 정보 받기
          메인 페이지(ArticleListView)로 이동
        실패하면
          에러 메시지 표시
      */
    axios({
       url: drf.accounts.signup(),
       method: 'post',
       data: credentials
    })
      .then(res => {
        const token = res.data.key
        dispatch('saveToken', token)
        dispatch('fetchCurrentUser')
        router.push({name: 'articles'})
      })
      .catch(err => {
        console.log(err.response.data)
        commit('SET_AUTH_ERROR', err.response.data)
        // if (err.response.status === 404) {
        //   router.push({name: 'NotFound404'})
        // }
      })
    },

    logout({ getters, dispatch }) {
      /* 
      POST: token을 logout URL로 보내기
        성공하면
          토큰 삭제
          사용자 알람
          LoginView로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.accounts.logout(),
        method: 'post',
        headers: getters.authHeader
      })
        .then(() => {
          dispatch('removeToken')
          alert('로그아웃 되었습니당!')
          router.push({name: 'login'})
        })
        .catch(err => {
          console.log(err.response)
        })

    },

    fetchCurrentUser({ commit, getters, dispatch }) {
      /*
      GET: 사용자가 로그인 했다면(토큰이 있다면)
        currentUserInfo URL로 요청보내기
          성공하면
            state.cuurentUser에 저장
          실패하면(토큰이 잘못되었다면)
            기존 토큰 삭제
            LoginView로 이동
      */
     if (getters.isLoggedIn) {
       axios({
         url: drf.accounts.currentUserInfo(),
         method: 'get',
         headers: getters.authHeader
       })
        .then(res => {
          commit('SET_CURRENT_USER', res.data)
        })
        .catch(err => {
          console.log(err.response)
          if (err.response.state === 401) {
            dispatch('removeToken')
            router.push({name: 'login'})
          }
        })

     }
    },

    fetchProfile({ commit, getters }, { username }) {
      /*
      GET: profile URL로 요청보내기
        성공하면
          state.profile에 저장
      */
      axios({
        url: drf.accounts.profile(username),
        method: 'get',
        headers: getters.authHeader,
      })
        .then(res => {
          commit('SET_PROFILE', res.data)
        })
    },
  },
}
