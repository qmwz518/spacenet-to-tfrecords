import os
import shutil

os.remove("converted_files.txt")
os.remove("output/ssd_train_labels.csv")
os.remove("output/ssd_test_labels.csv")
shutil.rmtree("images")
shutil.copy2("embedded_ssd_mobilenet_v1_coco.config","output/")

os.mkdir("output/data")
shutil.move("output/train.pbtxt","output/data/")
shutil.move("output/test.pbtxt","output/data/")
shutil.move("output/train.record","output/data/")
shutil.move("output/test.record","output/data/")
shutil.move("output/embedded_ssd_mobilenet_v1_coco.config","output/data/")
os.mkdir("output/models")
os.mkdir("output/models/train")
os.mkdir("output/models/eval")
for myfile in os.listdir("ssd_mobilenet_v1_coco_2018_01_28"):
    if os.path.isfile("ssd_mobilenet_v1_coco_2018_01_28/"+myfile):
        shutil.copy2("ssd_mobilenet_v1_coco_2018_01_28/"+myfile,"output/models/")
os.mkdir("output/models/saved_model")
os.mkdir("output/models/saved_model/variables")
for myfile in os.listdir("ssd_mobilenet_v1_coco_2018_01_28/saved_model"):
    if os.path.isfile("ssd_mobilenet_v1_coco_2018_01_28//saved_model/"+myfile):
        shutil.copy2("ssd_mobilenet_v1_coco_2018_01_28/saved_model/"+myfile,"output/models/saved_model/")
#shutil.copytree("ssd_mobilenet_v1_coco_2018_01_28/","output/models/")

shutil.make_archive("output", 'zip', 'output')
print("Post processing done! Upload output.zip to RCC.")
print("You can also delete the output directory now.")
