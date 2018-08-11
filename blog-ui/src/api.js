import axios from 'axios'

const customAxios = axios.create(
  {
    baseURL: 'http://127.0.0.1:8000/api'
  }
);

export function getPosts ()
{
  return customAxios.get('/posts').then((response) =>
  {
    return response.data.reduce((result, item) =>
    {
      result.push({
        author: item.fields.author,
        category: item.fields.category,
        body: item.fields.body
      });
      return result;
    }, []);
  });
}

export function getAuthors ()
{
  return customAxios.get('/authors').then((response) =>
  {
    return response.data.reduce((result, item) =>
    {
      result.push({
        id: item.pk,
        firstName: item.fields.first_name,
        lastName: item.fields.last_name
      });
      return result;
    }, []);
  });
}

export function savePost (bodyFormData)
{
  return customAxios({
    method: 'post',
    url: '/new-post',
    data: bodyFormData,
    config: { headers: {'Content-Type': 'multipart/form-data' }}
  });
}

export function getNewPostsCount ()
{
  return customAxios.get('/recently-published').then((response) =>
  {
    return response.data.count;
  });
}
