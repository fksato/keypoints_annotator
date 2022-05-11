face_keypoints_v0 = [
    "left_eye_inner_corner",
    "left_eye_center",
    "left_eye_outer_corner",
    "nose_tip",
    "right_eye_inner_corner",
    "right_eye_center",
    "right_eye_outer_corner",
    "lip_upper_center",
    "lip_lower_center",
    "lip_left_corner",
    "lip_right_corner"
]

face_keypoints_v1 = [
    "left eye left",
    "left eye center",
    "left eye right",
    "right eye left",
    "right eye center",
    "tip nose",
    "right eye right",
    "bottom nose",
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
    "nose tip",
    "bottom nose",
    "center top",
    "left top",
    "right top",
    "center bottom",
    "left bottom",
    "right bottom",
    "left",
    "right",
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
    "#FF9933",
    "#FF2211"
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
    "#999900"
]

mouth_keypoints_style = [
    "#00FF00",
    "#00FFFF",
    "#FFFF00",
    "#FF0000",
    "#FF00FF",
    "#FF6666",
    "#FFAB66"
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
    "#FFAB66"
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