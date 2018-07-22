Might need these:

export PYTHONPATH=$PYTHONPATH:/home/sumit/Coding/tensorflow-master/models-master/research/slim
export PYTHONPATH=$PYTHONPATH:/home/sumit/Coding/tensorflow-master/cocoapi-master/PythonAPI



python object_detection/model_main.py \
    --pipeline_config_path=/media/sumit/DATA/uChicago/Capstone/ssd/output/data/embedded_ssd_mobilenet_v1_coco.config \
    --model_dir=/media/sumit/DATA/uChicago/Capstone/ssd/output/models \
    --num_train_steps=50000 \
    --num_eval_steps=2000 \
    --alsologtostderr

# detection:
https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/exporting_models.md

python object_detection/export_inference_graph.py \
    --input_type=image_tensor \
    --pipeline_config_path=/media/sumit/DATA/uChicago/Capstone/ssd/output/data/embedded_ssd_mobilenet_v1_coco.config \
    --trained_checkpoint_prefix=/media/sumit/DATA/uChicago/Capstone/ssd/output/models/model.ckpt \
    --output_directory=/media/sumit/DATA/uChicago/Capstone/ssd/output/export
