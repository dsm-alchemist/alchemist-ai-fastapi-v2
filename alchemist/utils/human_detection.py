# Import Library
import io

from fastapi import HTTPException, status, UploadFile
from typing import List
from PIL import Image

import torch
from torchvision.transforms import transforms as T
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

# Import Setting
from alchemist.config import DETECTION_ACC, load_model

# 파라미터
IMG_SIZE = 480
model = load_model(option="detection")


def human_detection(files: List[UploadFile]):
    try:
        for img_path in files:
            contents = img_path.file.read()
            # img = Image.open(contents)
            img = Image.open(io.BytesIO(contents))
            input_img = img.resize((IMG_SIZE, int(img.height * IMG_SIZE / img.width)))

            # 이미지를 텐서로 바꿔주기
            # trf = A.Compose([ToTensorV2()])  # 이미지를 0~1의 값을 값는 텐서로 변경
            trf = T.Compose([T.ToTensor()])
            input_img = trf(input_img)

            if return_detect(img=input_img):
                continue
            else:
                return False
        return True
    except:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="file is none")


def return_detect(img):
    try:
        out = model([img])[0]
        for box, score in zip(out['boxes'], out['scores']):
            score = score.detach().numpy()

            if score < DETECTION_ACC:
                continue
            else:
                return True
    except:
        return False