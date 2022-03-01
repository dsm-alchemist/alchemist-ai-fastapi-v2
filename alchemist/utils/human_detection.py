# Import Library
from fastapi import HTTPException, status
from typing import List
from PIL import Image

import torch
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

# Import Setting
from alchemist.config import DETECTION_ACC, load_model

# 파라미터
IMG_SIZE = 480
model = load_model("detection")


def human_detection(files: List[str]):
    try:
        for img_path in files:
            img = Image.open(img_path)
            img = img.resize((IMG_SIZE, int(img.height * IMG_SIZE / img.width)))

            # 이미지를 텐서로 바꿔주기
            trf = A.Compose([ToTensorV2()])  # 이미지를 0~1의 값을 값는 텐서로 변경
            input_img = trf(img)

            if return_detect(img=input_img):
                continue
            else:
                return False
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="file is none")


def return_detect(img):
    out = model([img])[0]
    try:
        for box, score in zip(out['boxes'], out['scores']):
            score = score.detach().numpy()

            if score < DETECTION_ACC:
                continue
            else:
                return True
    except:
        return False