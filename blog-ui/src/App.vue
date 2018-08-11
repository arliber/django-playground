<template>
  <div id="app">
    <header>
      <h2>View Post</h2>
      <el-tag type="success">{{latestPosts > 0 ? latestPosts + ' new posts' : 'no new posts'}}</el-tag>
    </header>
    <new-post :authors="authors" v-if="formVisisble" @saved="refreshPosts"></new-post>
    <posts :posts="currentPosts" :authors="authors"></posts>
    <section class="controls">
      <el-pagination background 
                    layout="prev, pager, next" 
                    :total="posts.length" :page-size="2" 
                    @current-change="handleCurrentChange">
      </el-pagination>
      <el-button type="primary" icon="el-icon-plus" @click="formVisisble = !formVisisble">New post</el-button>
    </section>
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
      formVisisble: false
    }
  },
  created ()
  {
    Promise.all([
      getPosts(),
      getAuthors(),
      getNewPostsCount()
    ]).then(([posts, authors, latestPosts]) => {
      this.posts = posts;
      this.authors = authors;
      this.latestPosts = latestPosts;
    });
  },
  methods: {
    handleCurrentChange (page)
    {
      this.page = page;
    },
    refreshPosts ()
    {
      getPosts().then((posts) =>
      {
        this.posts = posts;
      });
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
  font-family: 'Avenir', Helvetica, Arial, sans-serif !important;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  width: 600px;
  margin: 30px auto;
}
header, .controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.controls {
  margin-top: 20px;
}
</style>
