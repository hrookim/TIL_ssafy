<template>
  <div>
    <h1>New Article</h1>
    <article-form :article="article" action="create"></article-form>
  </div>
</template>

<script>
import ArticleForm from '@/components/ArticleForm.vue'
// 이곳에서 article form으로 props를 보낼것, new일 경우는 title content 비어있고,
// edit일 경우에는 현재 저장된 title content를 보낸다!

  export default {
    name: 'AritcleNewView',
    components: {ArticleForm},
    data() {
      return {
        article : {
          pk: null,
          title: '',
          content: '',
        }
      }
    },
  }
</script>

<style></style>
