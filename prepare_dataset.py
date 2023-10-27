
# Core Python libraries
import copy
import fire
import json
import shutil
import os

# Package files
import constants

def get_dataset_attr(type):
    if type == "train":
        print(f"fetching details for train")
        return constants.TRAIN
    elif type == "val":
        print(f"fetching details for train")
        return constants.VAL
    else:
        print(f"Invalid dataset type, choose amoung train|val")
        return dict()
    
def download_dataset(url, redownload = False):
    print(f'Downloading from {url}')
    filename = os.path.basename(url)
    if os.path.exists(filename) and redownload == False:
        print(f'{filename} found, not downloading again')
        return filename
    if os.path.exists(filename) and redownload == True:
        print(f'{filename} found, but downloading again')
        shutil.rmtree(filename)
    os.system(f'wget {url}')
    return filename

def unzip_file(zipfile, redownload = False):
    print(f'Unzipping {zipfile}')
    foldername = zipfile.split('.')[0]
    if os.path.exists(foldername) and redownload == False:
        print(f'{foldername} found, not unzipping again')
        return foldername
    if os.path.exists(foldername) and redownload == True:
        print(f'{foldername} found, but unzipping again')
        shutil.rmtree(foldername)
    os.system(f'unzip -qq {zipfile}')
    return foldername

def load_annotated_json(filename):
    print(f'Loading annotations for {filename}')
    with open(filename) as f:
        annotated_json = json.load(f)
    return annotated_json

def list_files_under_folder(foldername):
    return os.listdir(foldername)

def create_target_folder(folder):
    print(f'creating {folder}')
    if os.path.exists(folder):
        print(f'target folder found, clearing it')
        shutil.rmtree(folder)
    os.makedirs(folder)


def prepare_vqav2_dataset(annotations, src_folder, target_folder, vqa_therapy, file_root):
    print(f'Preparing dataset for vqav2')
    for annotation in annotations:
        image_id = annotation["image_id"]
        image_filename = file_root + '0'*(12-len(image_id)) + image_id + '.jpg'
        os.system(f'cp -rL {src_folder}/{image_filename} {target_folder}/.')
        annotation_copy = copy.deepcopy(annotation)
        annotation_copy["image_filename"] = image_filename
        vqa_therapy.append(annotation_copy)
    return vqa_therapy

def prepare_vizwiz_dataset(annotations, src_folder, target_folder, vqa_therapy):
    print(f'Preparing dataset for vqav2')
    for annotation in annotations:
        image_id = annotation["image_id"]
        image_filename = image_id
        os.system(f'cp -rL {src_folder}/{image_filename} {target_folder}/.')
        annotation_copy = copy.deepcopy(annotation)
        annotation_copy["image_filename"] = image_filename
        vqa_therapy.append(annotation_copy)
    return vqa_therapy
        
def write_metadata(annotation, target_folder):
    print(f'Writing metadata')
    with open(os.path.join(target_folder, 'metadata.jsonl'), 'w') as f:
        for entry in annotation:
            json.dump(entry, f)
            f.write('\n')

def main(
        type = "train",
        redownload = False,
):
    dataset = get_dataset_attr(type)
    if not dataset:
        return
    
    zipfiles = list()
    for url in dataset["url"]:
        zipfiles.append(download_dataset(url, redownload))

    folders = list()
    for zipfile in zipfiles:
        folders.append(unzip_file(zipfile, redownload))

    annotation_data = list()
    for annotation_file in dataset["annotations"]:
        annotation_data.append(load_annotated_json(annotation_file))

    files_under_folder = list()
    for folder in folders:
        files_under_folder.append(list_files_under_folder(folder))

    create_target_folder(dataset["save_dir"])

    vqa_therapy = list()
    vqa_therapy = prepare_vqav2_dataset(annotation_data[0], folders[0], dataset["save_dir"], vqa_therapy, dataset["vqav2_file_root"])
    vqa_therapy = prepare_vizwiz_dataset(annotation_data[1], folders[1], dataset["save_dir"], vqa_therapy)

    write_metadata(vqa_therapy)


if __name__ == "__main__":
    fire.Fire(main)

