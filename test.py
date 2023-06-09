import os
import time

import cv2

from detector import YOLOv8_face

if __name__ == "__main__":
    for model in os.listdir("models"):
        YOLOv8_face_detector = YOLOv8_face(path=f"models/{model}",
                                           conf_thres=0.2,
                                           iou_thres=0.5,
                                           blur=True)
        srcimg = cv2.imread("./selfie.jpg")

        past = time.time()
        boxes, scores, classids, kpts = YOLOv8_face_detector.detect(srcimg)
        print(model, time.time() - past)
        dstimg = YOLOv8_face_detector.draw_detections(srcimg, boxes, scores, kpts)
        cv2.imwrite(f'{model}.jpg', dstimg)
