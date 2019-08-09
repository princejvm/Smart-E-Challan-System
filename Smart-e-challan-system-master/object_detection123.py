# coding: utf-8

# # Object Detection Demo
# Welcome to the object detection inference walkthrough!  This notebook will walk you step by step through the process of using a pre-trained model to detect objects in an image. Make sure to follow the [installation instructions](https://github.com/tensorflow/models/blob/master/object_detection/g3doc/installation.md) before you start.

# # Imports
import urllib
import numpy as np
import os
import json
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile
import cv2
from collections import defaultdict
from io import StringIO
import matplotlib.pyplot as plt
from PIL import Image
import datetime
import pickle
import utils.dataFileGlobal

sys.path.append("..")

from utils import label_map_util, dataFileGlobal
from utils import visualization_utils as vis_util

MODEL_NAME = 'ssd_mobilenet_v1_coco_11_06_2017'
MODEL_FILE = MODEL_NAME + '.tar.gz'
DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'mscoco_label_map.pbtxt')

NUM_CLASSES = 90

# ## Download Model

# In[ ]:

#opener = urllib.request.URLopener()
#opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
tar_file = tarfile.open(MODEL_FILE)
for file in tar_file.getmembers():
    file_name = os.path.basename(file.name)
    if 'frozen_inference_graph.pb' in file_name:
        tar_file.extract(file, os.getcwd())

detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
        (im_height, im_width, 3)).astype(np.uint8)
# # Detection

# In[ ]:

# For the sake of simplicity we will use only 2 images:
# image1.jpg
# image2.jpg
# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
#PATH_TO_TEST_IMAGES_DIR = 'test_images'
#TEST_IMAGE_PATHS = [os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 3)]
#print("loding done")
if __name__ == '__main__':
    # Size, in inches, of the output images.
    IMAGE_SIZE = (12, 8)
    # In[ ]:
    cam = cv2.VideoCapture('test1.mp4')
    ok, frame = cam.read()
    frame = cv2.resize(frame, (1280, 720))
    #frame = cv2.resize(frame, (800, 600))
    bbox_tmp = (287, 23, 86, 320)
    bbox_tmp = cv2.selectROI('ROI',frame, False)
    print(bbox_tmp,'Object Detection 123')
    dataFileGlobal.init()
    dataFileGlobal.myList.append(bbox_tmp)
    cv2.destroyWindow('ROI')
    #shared = {"a":bbox_tmp[0],"b":bbox_tmp[1],"c":bbox_tmp[2],"d":bbox_tmp[3]}
    #fp = open("shared.txt","wb")
    #pickle.dump(shared, fp)
    with detection_graph.as_default():
        with tf.Session(graph=detection_graph) as sess:
                image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
                detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
                detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
                detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = detection_graph.get_tensor_by_name('num_detections:0')
                ret = True
                while ret == True :
                    ret, image_np = cam.read()
                    #image_np = cv2.resize(image_np, (1280, 720))
                    #image_np = cv2.resize(image_np, (800, 600))
                    image_np_expanded = np.expand_dims(image_np, axis=0)
                    (boxes, scores, classes, num) = sess.run(
                        [detection_boxes, detection_scores, detection_classes, num_detections],
                        feed_dict={image_tensor: image_np_expanded})
                    vis_util.visualize_boxes_and_labels_on_image_array(
                        image_np,
                        np.squeeze(boxes),
                        np.squeeze(classes).astype(np.int32),
                        np.squeeze(scores),
                        category_index,
                        use_normalized_coordinates=True,
                        line_thickness=8)
                    cv2.rectangle(image_np, (bbox_tmp[0], bbox_tmp[1]), (bbox_tmp[0]+bbox_tmp[2], bbox_tmp[1]+bbox_tmp[3]), (0, 255, 0), 2)
                    cv2.imshow('object detection', image_np)
                    if cv2.waitKey(100) & 0xFF == ord('q'):
                        print(dataFileGlobal.numTrack)
                        lenth = len(dataFileGlobal.listTrack)
                        cv2.destroyAllWindows()
                        break