
import tensorboard


import tensorflow as tf
tf.enable_eager_execution()

import tempfile
import zipfile
import os




# Load the serialized model
loaded_model = tf.keras.models.load_model('model_data_its-tiny/trained_weights_final_tiny_17_2.h5')

