<template>
  <div>
    <h1>{{ profile.username }}</h1>

    <h2>작성한 리뷰: {{ reviewCnt }}개</h2>
    <ul>
      <li v-for="review in profile.reviews" :key="review.pk">
        <router-link :to="{ name: 'article', params: { articlePk: review.pk } }">
          {{ review.title }}
        </router-link>
      </li>
    </ul>

    <h2>좋아요 한 글</h2>
    <ul>
      <li v-for="review in profile.like_reviews" :key="review.pk">
        <router-link :to="{ name: 'article', params: { articlePk: review.pk } }">
          {{ review.title }}
        </router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import { mapGetters, mapActions } from 'vuex'


export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['profile']),
    reviewCnt() {
      return this.profile.reviews.length
    }
  },
  methods: {
    ...mapActions(['fetchProfile'])
  },
  created() {
    const payload = { username: this.$route.params.username }
    this.fetchProfile(payload)
  },
}
</script>
