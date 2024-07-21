from deepface import DeepFace
import os
import cv2

delete_path = "./2"
models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID"]
files = os.listdir(delete_path)
result = None
images = []

def delete_file(delete_path):
    if os.path.exists(delete_path):
            os.remove(delete_path)
    return
            

for file in files:
    try:
        result = DeepFace.verify("d1.jpg", delete_path+"/"+file, model_name = models[0])
        print(file," = ",result['verified'])
        if not result['verified']:
            delete_file(delete_path+"/"+file)
    except:
       print(file,"error")
       delete_file(delete_path+"/"+file)
       continue
     
    