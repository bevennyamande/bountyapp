import os, shutil
from fastapi import FastAPI, File, UploadFile
from train import train, predict

app = FastAPI()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'trained_knn_model.clf')
TRAIN_DIR = os.path.join(BASE_DIR, 'train')

@app.post("/image_upload/")
async def create_upload_file(image: UploadFile = File(...)):
    with open("temporary.jpg", "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    classifier = train(TRAIN_DIR, model_save_path=MODEL_PATH)
    predictions = predict(os.path.join(BASE_DIR,image.filename, model_path=MODEL_PATH))
    return {"predictions": predictions}

