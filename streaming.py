import cv2

from detector import YOLOv8_face

WINDOW_NAME = "Opencv Webcam"


def run():
    cv2.namedWindow(WINDOW_NAME)

    video_capture = cv2.VideoCapture(0)

    model = YOLOv8_face(path="models/yolov8-lite-t.onnx",
                        conf_thres=0.2,
                        iou_thres=0.5,
                        show_keypoint=False)
    while True:
        ret, frame = video_capture.read()
        try:
            boxes, scores, _, kpts = model.detect(frame)
            output = model.draw_detections(frame, boxes, scores, kpts)
        except:
            output = frame
        cv2.imshow(WINDOW_NAME, output)
        cv2.waitKey(1)


if __name__ == "__main__":
    print("RUNNING")
    run()
