face_keypoints_v0 = [
    "left_eye_inner_corner",
    "left_eye_center",
    "left_eye_outer_corner",
    "nose_left_corner",
    "nose_center",
    "nose_right_corner",
    "nose_tip",
    "right_eye_inner_corner",
    "right_eye_center",
    "right_eye_outer_corner",
    "lip_upper_left",
    "lip_upper_center",
    "lip_upper_right",
    "lip_lower_left",
    "lip_lower_center",
    "lip_lower_right",
    "lip_left_center",
    "lip_right_center"
]

face_keypoints_v1 = [
    "left eye left",
    "left eye center",
    "left eye right",
    "right eye left",
    "right eye center",
    "right eye right",
    "tip nose",
    "left nostril corner",
    "center bottom nose",
    "right nopstril corner",
    "top mouth",
    "left mouth",
    "right mouth",
    "bottom mouth",
    "bottom chin"
]

mouth_keypoints = [
    "center top",
    "left top",
    "right top",
    "center bottom",
    "left bottom",
    "right bottom",
    "left",
    "right"
]

mouth_keypoints_v1 = [
    "tip nose",
    "left nostril corner",
    "center bottom nose",
    "right nopstril corner",
    "center top lip",
    "left top lip",
    "right top lip",
    "center bottom lip",
    "left bottom lip",
    "right bottom lip",
    "left lip",
    "right lip",
    "bottom chin"
]

face_keypoints_style_v0 = [
    "#00FF00",
    "#00FFFF",
    "#FFFF00",
    "#FF0000",
    "#FF00FF",
    "#666666",
    "#FF9933",
    "#CCFFCC",
    "#FF3486",
    "#FF9453",
    "#FF2211",
    "#FF22FF",
    "#663266",
    "#FF9645",
    "#CC4FAB",
    "#FF4926",
    "#FCA933",
    "#BB2211"
]

face_keypoints_style_v1 = [
    "#00FF00",
    "#00FFFF",
    "#FFFF00",
    "#FF0000",
    "#FF00FF",
    "#666666",
    "#FF9933",
    "#CCFFCC",
    "#FF3486",
    "#FF9933",
    "#FF2211",
    "#FF1326",
    "#999900",
    "#CB1326",
    "#FF9900"
]

mouth_keypoints_style = [
    "#00FF00",
    "#00FFFF",
    "#FFFF00",
    "#FF0000",
    "#FF00FF",
    "#FF6666",
    "#FFAB66",
    "#FFC266"
]

mouth_keypoints_style_v1 = [
    "#FF0034",
    "#FFFF22",
    "#00FF00",
    "#00FFFF",
    "#FFFF00",
    "#FF0000",
    "#FF00FF",
    "#FF6666",
    "#FF6241",
    "#FFAB66",
    "#FA6646",
    "#FF63B1",
    "#FCA766"
]

categories = [
    {
        "id": "0",
        "name": "face_v0",
        "supercategory": "human",
        "keypoints": face_keypoints_v0,
        "keypoints_style": face_keypoints_style_v0
    },
    {
        "id": "1",
        "name": "face_v1",
        "supercategory": "human",
        "keypoints": face_keypoints_v1,
        "keypoints_style": face_keypoints_style_v1
    },
    {
        "id": "2",
        "name": "mouth",
        "supercategory": "human",
        "keypoints": mouth_keypoints,
        "keypoints_style": mouth_keypoints_style
    },
    {
        "id": "3",
        "name": "mouth area",
        "supercategory": "human",
        "keypoints": mouth_keypoints_v1,
        "keypoints_style": mouth_keypoints_style_v1
    }
]