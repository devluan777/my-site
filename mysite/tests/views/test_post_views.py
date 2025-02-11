import json
import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_post_view(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200

    response_content = response.content.decode('utf-8') 
    assert response_content == 'hello word'


