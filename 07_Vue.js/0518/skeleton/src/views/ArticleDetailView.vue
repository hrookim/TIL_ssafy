<template>
  <div>
    <h1>{{ article.title }}</h1>

    <p>
      {{ article.content }}
    </p>
    <!-- Article Edit/Delete UI -->
    <div v-if="isAuthor">
      <router-link :to="{ name: 'articleEdit', params: {articlePk} }">
        <button>Edit</button>
      </router-link>
      |
      <button @click="deleteArticle(articlePk)">Delete</button>
    </div>

    <!-- Article Like UI -->
    <div>
      Likeit:
      <button @click="likeArticle(articlePk)"
      >{{ likeCount }}</button>
      <!-- 만약 내가 좋아요를 눌렀는지 확인하려면,
      like_users.username과 currentUser.username이 같은지 확인한다 -->
    </div>

    <hr />
    <!-- Comment UI -->
  </div>
</template>

<script>
  import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'ArticleDetail',
    data() {
      return {
        articlePk: this.$route.params.articlePk,
      }
    },
    computed: {
      ...mapGetters(['isAuthor', 'article']),
      likeCount() {
        return this.article.like_users?.length
      }
    },
    methods: {
      ...mapActions(['fetchArticle', 'likeArticle', 'deleteArticle'])
    },
    created() {
      this.fetchArticle(this.articlePk)
    },
  }
</script>

<style></style>
