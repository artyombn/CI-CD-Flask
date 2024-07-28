def test_get_items(client):
    response = client.get('/items/')
    assert response.status_code == 200
    assert response.json == {
        "items": ["a", "b"],
    }
