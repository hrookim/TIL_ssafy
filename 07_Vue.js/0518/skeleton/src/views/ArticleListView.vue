<template>
  <div>
    <h1>Home</h1>
    <ul>
      <li v-for="article in articles" :key="article.pk">
        <router-link :to="{name: 'profile', params: {username: article.user.usename} }">{{ article.user.username }}</router-link>
        <router-link :to="{ name:'article', params: {articlePk: article.pk} }">
          {{ article.title }}
        </router-link>
        댓글: {{ article.comment_count }} | 좋아요: {{ article.like_count }}
      </li>
    </ul>
  </div>
</template>

<script>
import { mapActions, mapGetters } from 'vuex'

  export default {
    name: 'ArticleList',
    computed: {
      ...mapGetters(['articles'])
    },
    methods: {
      ...mapActions(['fetchArticles'])
    },
    created() {
      this.fetchArticles()
    },
  }
</script>

<style></style>
