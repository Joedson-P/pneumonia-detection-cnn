from fastapi import FastAPI, UploadFile, File
import uvicorn
import numpy as np
import tensorflow as tf
from PIL import Image
import io

app = FastAPI(title="Pneumonia Detection API")

# Carregar o modelo pré-treinado
MODEL_PATH = "models/pneumonia_model_v1.keras"
model = tf.keras.models.load_model(MODEL_PATH)

def preprocess_image(image_bytes):
    """Lê a imagem, redimensiona e normaliza."""
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    image = image.resize((224, 224))
    image_array = np.array(image) / 255.0
    image_array = np.expand_dims(image_array, axis=0)
    return image_array

@app.get("/")
def read_root():
    return {"message": "API de Detecção de Pneumonia está ativa."}

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Ler bytes da imagem enviada
    contents = await file.read()

    # Pré-processar a imagem
    processed_image = preprocess_image(contents)

    # Fazer a predição
    prediction = model.predict(processed_image)[0][0]
    
    # Interpretar o resultado
    label = "PNEUMONIA" if prediction > 0.5 else "NORMAL"
    confidence = float(prediction) if label == "PNEUMONIA" else float(1 - prediction)

    return {
        "image_name": file.filename,
        "label": label,
        "confidence": round(confidence * 100, 2)
    }

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)