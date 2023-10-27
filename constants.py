## Annotations file path
# VQAV2
VQAV2_ANNOTATION_TRAIN = './Annotations/VQA_train.json'
VQAV2_ANNOTATION_VAL = './Annotations/VQA_val.json'
# VizWiz
VIZWIZ_ANNOTATION_TRAIN = './Annotations/VizWiz_train.json'
VIZWIZ_ANNOTATION_VAL = './Annotations/VizWiz_val.json'

## URLS for IMAGES
# VQAV2
VQAV2_URL_TRAIN = 'http://images.cocodataset.org/zips/train2014.zip'
VQAV2_URL_VAL = 'http://images.cocodataset.org/zips/val2014.zip'
# VizWiz
VIZWIZ_URL_TRAIN = 'https://vizwiz.cs.colorado.edu/VizWiz_final/images/train.zip'
VIZWIZ_URL_VAL = 'https://vizwiz.cs.colorado.edu/VizWiz_final/images/val.zip'

## VQA Therapy Target folder
VQA_THERAPY_TRAIN = './vqa_therapy/train'
VQA_THERAPY_VAL = './vqa_therapy/val'

TRAIN = {
    "urls": [VQAV2_URL_TRAIN, VIZWIZ_URL_TRAIN],
    "annotations": [VQAV2_ANNOTATION_TRAIN, VIZWIZ_ANNOTATION_TRAIN],
    "save_dir": VQA_THERAPY_TRAIN,
    "vqav2_file_root": "COCO_train2014_"
}

VAL = {
    "urls": [VQAV2_URL_TRAIN, VIZWIZ_URL_VAL],
    "annotations": [VQAV2_ANNOTATION_VAL, VIZWIZ_ANNOTATION_VAL],
    "save_dir": VQA_THERAPY_VAL,
    "vqav2_file_root": "COCO_train2014_"
}
