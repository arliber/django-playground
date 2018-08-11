<template>
  <el-form ref="form" :model="form" label-width="120px" class="form">
    <el-form-item label="Category">
      <el-input v-model="form.category"></el-input>
    </el-form-item>
    <el-form-item label="Author">
      <el-select v-model="form.author" placeholder="please an author">
        <el-option v-for="author in authors" 
                  :label="author.firstName + ' ' + author.lastName" 
                  :value="author.id" 
                  :key="author.id">
      </el-option>
      </el-select>
    </el-form-item>
    <el-form-item label="Activity form">
      <el-input type="textarea" v-model="form.body"></el-input>
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit">Submit</el-button>
    </el-form-item>
  </el-form>
</template>
<script>
import { savePost } from '../api'

export default {
  props: ['authors'],
  data ()
  {
    return {
      form: {
        category: '',
        author: 1,
        body: ''
      }
    };
  },
  methods: {
    onSubmit ()
    {
      let bodyFormData = new FormData();
      bodyFormData.set('author', this.form.author);
      bodyFormData.set('category', this.form.category);
      bodyFormData.set('body', this.form.body);
      savePost(bodyFormData).then(() =>
      {
        // Notify
        this.$message({
          message: 'Congrats, post saved!',
          type: 'success'
        });
        // Clear form
        this.form.category = '';
        this.form.body = '';
        // Notify parent (so he can reload)
        this.$emit('saved');
      });
    }
  }
}
</script>
<style scoped>
.form {
  border: 1px solid #28d428;
  border-radius: 5px;
  padding: 15px 15px 0 0;
}
</style>


