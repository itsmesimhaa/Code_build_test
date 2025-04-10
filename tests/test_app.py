from src.app import app

def test_home():
    tester = app.test_client()
    response = tester.get('/')
    assert response.status_code == 200
    assert response.json['message'] == 'Hello from Flask App!'

def test_health():
    tester = app.test_client()
    response = tester.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'OK'
