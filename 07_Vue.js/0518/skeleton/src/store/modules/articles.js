import axios from 'axios'
import router from '@/router'
import drf from '@/api/drf'

import _ from 'lodash'

export default {
  // namespaced: true,
  state: {
    articles: [],  // 전체 게시글 리스트
    article: {},  // 디테일로 볼 게시글
  },

  getters: {
    articles(state) {return state.articles},
    article(state) {return state.article},
    isAuthor(state, getters) {
      return state.article.user?.username === getters.currentUser.username
    },
    isArticle(state) {return !_.isEmpty(state.article)}
  },

  mutations: {
    SET_ARTICLES(state, articles) {state.articles = articles},
    SET_ARTICLE(state, article) {state.article = article}
  },

  actions: {
    fetchArticles({ commit, getters }) {
      /* 게시글 목록 받아오기
      GET: articles URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.articles.articles(),
        method: 'get',
        headers: getters.authHeader,
      })
      .then(res => commit('SET_ARTICLES', res.data))
      .catch(err => console.log(err.response))
    },

    fetchArticle({ commit, getters }, articlePk) {
      /* 단일 게시글 받아오기
      GET: article URL (token)
        성공하면
          응답으로 받은 게시글들을 state.articles에 저장
        실패하면
          단순 에러일 때는
            에러 메시지 표시
          404 에러일 때는
            NotFound404 로 이동
      */
      axios({
        url: drf.articles.article(articlePk),
        method: 'get',
        headers: getters.authHeader
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => {
          console.error(err.response)
          if (err.response.status === 404) {
            router.push({name: 'NotFound404'})
          }
        })
    },

    createArticle({ commit, getters }, article) {
      /* 게시글 생성
      POST: articles URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.articles.articles(), // POST /articles
        method: 'post',
        data: article,
        headers: getters.authHeader
      })
        .then(res => {
          console.log(res.data)
          commit('SET_ARTICLE', res.data)
          router.push({name:'article', params: {articlePk: getters.article.pk}})
        })
        .catch(err => console.error(err.response))
    },

    updateArticle({ commit, getters }, {pk, title, content}) {
      /* 게시글 수정
      PUT: article URL (게시글 입력정보, token)
        성공하면
          응답으로 받은 게시글을 state.article에 저장
          ArticleDetailView 로 이동
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.articles.article(article.pk), // PUT /article
        method: 'put',
        data: {title, content},
        headers: getters.authHeader
      })
        .then(res => {
          console.log(res.data)
          commit('SET_ARTICLE', res.data)
          router.push({name:'article', params: {articlePk: getters.article.pk}})
        })
        .catch(err => console.error(err.response))
    },

    deleteArticle({ commit, getters }, articlePk) {
      /* 게시글 삭제
      사용자가 확인을 받고
        DELETE: article URL (token)
          성공하면
            state.article 비우기
            AritcleListView로 이동
          실패하면
            에러 메시지 표시
      */
      
      if (confirm('정말 삭제하시겠습니까?')) {
        axios({
          url: drf.articles.article(articlePk),
          method: 'delete',
          headers: getters.authHeader,
        })
          .then(() => {
            commit('SET_ARTICLE', {})
            router.push({ name: 'articles' })
          })
          .catch(err => console.error(err.response))
      }
    },

    likeArticle({ commit, getters }, articlePk) {
      /* 좋아요
      POST: likeArticle URL(token)
        성공하면
          state.article 갱신
        실패하면
          에러 메시지 표시
      */
      axios({
        url: drf.articles.likeArticle(articlePk),
        method: 'post',
        headers: getters.authHeader
      })
        .then(res => commit('SET_ARTICLE', res.data))
        .catch(err => console.err(err.response))
    },

    createComment({ commit, getters }) {
      /* 댓글 생성
      POST: comments URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      */

    },

    updateComment({ commit, getters }, { articlePk, commentPk, content }) {
      /* 댓글 수정
      PUT: comment URL(댓글 입력 정보, token)
        성공하면
          응답으로 state.article의 comments 갱신
        실패하면
          에러 메시지 표시
      
      */
    },

    deleteComment({ commit, getters }, { articlePk, commentPk }) {
      /* 댓글 삭제
      사용자가 확인을 받고
        DELETE: comment URL (token)
          성공하면
            응답으로 state.article의 comments 갱신
          실패하면
            에러 메시지 표시
      */
    },
  },
}
