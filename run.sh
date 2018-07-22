source activate py27
python generate_old_bounding_boxes.py
source deactivate
python logistics.py
export PYTHONPATH=$PYTHONPATH:/home/sumit/Coding/tensorflow-master/models-master/research
python generate_tfrecord.py --csv_input=output/ssd_train_labels.csv  --output_path=output/train.record
python generate_tfrecord.py --csv_input=output/ssd_test_labels.csv  --output_path=output/test.record
python post_processing.py
