import face_recognition
import numpy as np
from PIL import Image

def detect_faces(image: Image.Image) -> list:
    """检测图片中的所有人脸位置"""
    img_array = np.array(image)
    face_locations = face_recognition.face_locations(img_array)
    return face_locations

def get_face_encodings(image: Image.Image) -> list:
    """获取所有人脸的128维特征编码"""
    img_array = np.array(image)
    face_encodings = face_recognition.face_encodings(img_array)
    return face_encodings

def recognize_faces(image: Image.Image, known_encodings: list, known_names: list) -> list:
    """识别人脸并返回对应的姓名"""
    face_encodings = get_face_encodings(image)
    face_names = []
    for encoding in face_encodings:
        matches = face_recognition.compare_faces(known_encodings, encoding)
        name = "Unknown"
        face_distances = face_recognition.face_distance(known_encodings, encoding)
        if len(face_distances) > 0:
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_names[best_match_index]
        face_names.append(name)
    return face_names
