from rest_framework import status

from core.fixtures.user import user
from core.fixtures.post import post


class TestPostViewSet:
    
    endpoint = '/api/posts/'
    
    def test_list_posts(self, api_client, post):
        api_client.force_authenticate(user=user)
        response = api_client.get(self.endpoint)
        assert response.status_code == status.HTTP_200_OK
        assert response.data["count"] == 1
        
    def test_retrieve(self, client, post):
        client.force_authenticate(user=user)
        response = client.get(self.endpoint + str(post.public_id) + '/')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] == post.public_id.hex
        assert response.data["body"] == post.body
        assert response.data["author"]['id'] == post.author.public_id.hex