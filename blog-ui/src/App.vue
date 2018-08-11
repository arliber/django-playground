<template>
  <div id="app">
    <header>
      <h2>View Post</h2>
      <el-tag type="success">{{latestPosts > 0 ? latestPosts + ' new posts' : 'no new posts'}}</el-tag>
    </header>
    <new-post :authors="authors"></new-post>
    <posts :posts="currentPosts" :authors="authors"></posts>
    <el-pagination background layout="prev, pager, next" :total="posts.length" :page-size="2" @current-change="handleCurrentChange">
</el-pagination>
  </div>
</template>
<script>
import NewPost from './components/NewPost.vue'
import Posts from './components/Posts.vue'
import { getPosts, getAuthors, getNewPostsCount } from './api';

export default {
  name: 'app',
  components: {
    NewPost,
    Posts
  },
  data ()
  {
    return {
      posts: [],
      authors: [],
      latestPosts: 0,
      page: 1,
    }
  },
  created ()
  {
    Promise.all([
      getPosts(),
      getAuthors(),
      getNewPostsCount()
    ]).then(([posts, authors, latestPosts]) => {
      console.log('done');
      this.posts = posts;
      this.authors = authors;
      this.latestPosts = latestPosts;
    });
  },
  methods: {
    handleCurrentChange (page)
    {
      this.page = page;
    }
  },
  computed: {
    currentPosts ()
    {
      const start = (this.page-1)*2;
      return this.posts.slice(start, start+2);
    }
  }
}
</script>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 600px;
  margin: 30px auto;
}
header {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>
