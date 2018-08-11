<template>
  <el-table :data="posts" stripe style="width: 100%">
    <el-table-column prop="author" label="Author" width="180">
      <template slot-scope="scope">
        <i class="el-icon-document"></i>
        <span style="margin-left: 10px">{{ authors.find((a) => a.id === scope.row.author).firstName }}</span>
      </template>
    </el-table-column>
    <el-table-column prop="category" label="Category" width="180"></el-table-column>
    <el-table-column prop="body" label="Post"></el-table-column>
  </el-table>
</template>
<script>
export default {
  props: ['posts', 'authors']
}
</script>
