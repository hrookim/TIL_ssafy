<template>
  <div>
    <h1>Edit Article</h1>
    <article-form v-if="isArticle" :article="article" action="update"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
import { mapGetters, mapActions } from 'vuex'

  export default {
    name: 'AritcleEditView',
    components: {ArticleForm},
    computed: {
      ...mapGetters(['article', 'isArticle'])
    },
    methods: {
      ...mapActions(['fetchArticle'])
    },
    created() {
      const articlePk = this.$route.params.articlePk
      this.fetchArticle(articlePk)  // 비동기라 안보일 것임 ㅜ
    },
  }
</script>

<style></style>
