# Import Library
from fastapi import HTTPException, status
from typing import List
from PIL import Image

import torch
import albumentations as A
from albumentations.pytorch.transforms import ToTensorV2

# Import Setting
from alchemist.config import CLASSIFICATION_ACC, load_model


def posture_classity(files: List):
    return True