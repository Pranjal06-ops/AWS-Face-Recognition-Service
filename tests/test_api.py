from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_recognition():
    from io import BytesIO
    from PIL import Image
    img = Image.new('RGB', (64,64), color = 'red')
    buf = BytesIO()
    img.save(buf, format='JPEG')
    buf.seek(0)
    response = client.post('/face/recognize', files={'file': ('test.jpg', buf, 'image/jpeg')})
    assert response.status_code == 200
    assert response.json()['predicted_class'] == 1