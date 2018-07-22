import os
import shutil
import random
import configparser
from osgeo import gdal
import subprocess

config = configparser.ConfigParser()
config.read('config.ini')
tif_path = config['FILE_PATHS']['TIF_PATH']
TEST_SIZE = float(config['PARAMS']['TEST_SIZE'])

if not os.path.exists("output"):
    os.mkdir("output")

filelist = []
with open("converted_files.txt", "r") as jpglist:
    for line in jpglist:
        filelist.append(line)

if not os.path.exists("images"):
    os.mkdir("images")
fname = []
for raster in filelist:
    srcRaster = gdal.Open(tif_path+os.path.splitext(raster)[0]+".tif")
    outputRaster = "images/"+os.path.splitext(raster)[0]+".jpg"

    cmd = ['gdal_translate', '-ot', 'Byte', '-of', 'JPEG', '-co', 'PHOTOMETRIC=rgb']
    scaleList = []
    for bandId in range(srcRaster.RasterCount):
        bandId = bandId+1
        band=srcRaster.GetRasterBand(bandId)
        min = band.GetMinimum()
        max = band.GetMaximum()

        # if not exist minimum and maximum values
        if min is None or max is None:
            (min, max) = band.ComputeRasterMinMax(1)
        cmd.append('-scale_{}'.format(bandId))
        cmd.append('{}'.format(0))
        cmd.append('{}'.format(max))
        cmd.append('{}'.format(0))
        cmd.append('{}'.format(255))

    cmd.append(tif_path+os.path.splitext(raster)[0]+".tif")
    cmd.append(outputRaster)
    print(cmd)
    subprocess.call(cmd)
    os.remove("images/"+os.path.splitext(raster)[0]+".jpg.aux.xml")

lMap = """item {
  id: 1
  name: 'building'
}
"""

with open("output/train.pbtxt", "w") as labelMap:
    labelMap.write(lMap)

shutil.copy2("output/train.pbtxt","output/test.pbtxt")
shutil.copy2("run.sbatch","output/")
shutil.move("ssd_train_labels.csv","output/")
shutil.move("ssd_test_labels.csv","output/")
print("Logistics done!")

