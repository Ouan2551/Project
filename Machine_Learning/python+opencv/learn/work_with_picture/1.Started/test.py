import os

image_path = "D:\\Important files Nannaphat\\coding\\Project\\Machine_Learning\\python+opencv\\learn\\work_with_picture\\started\\geeksforgeek.png"

if os.path.exists(image_path):
    print("✔ Found image file!")
else:
    print("❌ Error: File not found!")
