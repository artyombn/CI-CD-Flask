def test_get_items(client):
    response = client.get('/items/')
    assert response.status_code == 200
    assert response.json == {
        "items": ["a", "b"],
    }

def test_get_item_by_id(client):
    response = client.get('/items/10/')
    assert response.json == {
        "data": {
            "item_id": 10,
            "res": 5,
        }
    }
