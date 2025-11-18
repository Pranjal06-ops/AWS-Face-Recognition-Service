from fastapi import APIRouter, UploadFile, File
from app.models.dummy_cnn import DummyCNN
from PIL import Image
import io

router = APIRouter()
model = DummyCNN()
model.eval()

@router.post('/recognize')
async def recognize_face(file: UploadFile = File(...)):
    image = Image.open(io.BytesIO(await file.read())).convert('RGB')
    # preprocessing placeholder
    # dummy prediction
    prediction = model(None)
    predicted_class = int(prediction.argmax())
    return {'predicted_class': predicted_class}