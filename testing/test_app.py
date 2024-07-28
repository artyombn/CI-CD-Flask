def test_hello_world(client):
    response = client.get('/')
    assert response.status_code == 200

def test_hello_name(client):
    response_with_no_name = client.get('/hello/')
    response_with_name = client.get('/hello/Anton/')
    assert response_with_no_name.status_code == 200
    assert response_with_no_name.json == {
        "message": "Hello World!"
    }

    assert response_with_name.status_code == 200
    assert response_with_name.json == {
        "message": "Hello Anton!"
    }
