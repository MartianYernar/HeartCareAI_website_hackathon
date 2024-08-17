from ultralytics import YOLO
# import cv2 as cv
# import numpy as np
# import torch
# import os

# device = 'cuda' if torch.cuda.is_available() else 'cpu'
# print(device)
# torch.cuda.set_device(0)

# Fire_detection# # Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
# model = YOLO("/content/drive/MyDrive/Waste_recognition/best.pt").to(device)  # load a pretrained model (recommended for training)

# Use the model
model.train(data=r"C:\Users\Ernar\Documents\HeartCareAI_flask_webapp\config.yaml", epochs=20)  # train the model
# # metrics = model.val()  # evaluate model performance on the validation set
# path = model.export(format="ONNX")  # export the model to ONNX format
