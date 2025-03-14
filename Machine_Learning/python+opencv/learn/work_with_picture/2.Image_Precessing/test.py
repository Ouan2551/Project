import cv2

# เปิดกล้อง
cap = cv2.VideoCapture(0)

# อ่านเฟรมแรกเพื่อใช้เป็นพื้นหลัง
ret, frame1 = cap.read()
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while True:
    # อ่านเฟรมปัจจุบัน
    ret, frame2 = cap.read()
    if not ret:
        break

    # แปลงเฟรมเป็นภาพขาวดำและเบลอ
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # คำนวณความแตกต่างระหว่างเฟรม
    diff = cv2.absdiff(gray1, gray2)
    thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)[1]

    # ทำ Morphological operations เพื่อลดสัญญาณรบกวน
    thresh = cv2.dilate(thresh, None, iterations=2)

    # หา contours
    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # วาดสี่เหลี่ยมรอบวัตถุที่เคลื่อนไหว
    for contour in contours:
        if cv2.contourArea(contour) < 500:
            continue
        (x, y, w, h) = cv2.boundingRect(contour)
        cv2.rectangle(frame2, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # แสดงผล
    cv2.imshow("Motion Detection", frame2)

    # อัพเดทเฟรมพื้นหลัง
    gray1 = gray2.copy()

    # กด 'q' เพื่อออก
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# ปล่อยกล้องและปิดหน้าต่าง
cap.release()
cv2.destroyAllWindows()