from fastapi import FastAPI
from ultralytics import YOLO
from pydantic import BaseModel
from typing import List
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "SynerX"}


# # Load a pretrained YOLO11n model
# model = YOLO("yolo11n.pt")

# # Train the model on the COCO8 dataset for 100 epochs
# train_results = model.train(
#     data="coco8.yaml",  # Path to dataset configuration file
#     epochs=100,  # Number of training epochs
#     imgsz=640,  # Image size for training
#     device="cpu",  # Device to run on (e.g., 'cpu', 0, [0,1,2,3])
# )

# # Evaluate the model's performance on the validation set
# metrics = model.val()

# # Perform object detection on an image
# results = model("path/to/image.jpg")  # Predict on an image
# results[0].show()  # Display results

# # Export the model to ONNX format for deployment
# path = model.export(format="onnx")  # Returns the path to the exported model
