from deepface import DeepFace
import os
import cv2

models = ["VGG-Face", "Facenet", "OpenFace", "DeepFace", "DeepID"]

videos_path = "./videos"
faceset_path = "./faceset"
include_folder = "./include"
exclude_folder = "./exclude"

videos = os.listdir(videos_path)
includes = os.listdir(include_folder)
excludes  = os.listdir(exclude_folder)

def delete_file(delete_path):
    if os.path.exists(delete_path):
            os.remove(delete_path)
    return

for vid in videos:
    vid_path = videos_path+"/"+vid
    print(vid_path)
    video = cv2.VideoCapture(vid_path)
    frame_no = 0
    while video.isOpened():
        if frame_no%100==0:
            print(frame_no)
        ret, frame = video.read()
        frame_no += 1
        result_flag = False
        incexc_flag = True
        result = None
        for include in includes:
            include_path = include_folder+"/"+include
            try:
                if DeepFace.verify(include_path, frame, model_name = models[0])['verified']:
                    result = DeepFace.verify(include_path, frame, model_name = models[0])['verified']
                    incexc_flag = True
                    break
                else:
                    incexc_flag = False
            except:
                incexc_flag = False
                print("face not found")
        else:
            continue
        break
        
        for exclude in excludes:
            exclude_path = exclude_folder+"/"+exclude
            try:
                if DeepFace.verify(exclude_path, frame, model_name = models[0])['verified']:
                    incexc_flag = True
                    break
                else:
                    incexc_flag = False
            except:
                incexc_flag = False
                print("face not found")
        else:
            continue
        break
        if not result is None:
            cv2.imwrite(faceset_path+"/"+str(frame_no)+".jpg",frame)
            
    
    
            
            

        















    try:
        result = DeepFace.verify("d1.jpg", delete_path+"/"+file, model_name = models[0])
        print(file," = ",result['verified'])
        if not result['verified']:
            delete_file(delete_path+"/"+file)
    except:
       print(file,"error")
       delete_file(delete_path+"/"+file)
       continue
     
    