import streamlit as st
from PIL import Image, ImageDraw
from src.face_utils import detect_faces, get_face_encodings, recognize_faces
import face_recognition

# 初始化已知人脸库（示例）
known_face_encodings = []
known_face_names = []

# 示例：加载一张已知人脸
# sample_image = face_recognition.load_image_file("known_faces/zhangsan.jpg")
# sample_encoding = face_recognition.face_encodings(sample_image)[0]
# known_face_encodings.append(sample_encoding)
# known_face_names.append("Zhang San")

st.title("🧑 Face Detection & Recognition Demo")

# 上传图片或选择示例
uploaded_file = st.file_uploader("上传图片", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="上传的图片", use_column_width=True)

    # 检测人脸
    face_locations = detect_faces(image)
    st.write(f"检测到 {len(face_locations)} 张人脸")

    # 绘制人脸框
    draw = ImageDraw.Draw(image)
    for (top, right, bottom, left) in face_locations:
        draw.rectangle([(left, top), (right, bottom)], outline="red", width=3)

    # 识别人脸（可选）
    face_names = recognize_faces(image, known_face_encodings, known_face_names)

    # 显示结果
    st.image(image, caption="检测结果", use_column_width=True)
    if face_names:
        st.write("识别结果：")
        for name in face_names:
            st.write(f"- {name}")
