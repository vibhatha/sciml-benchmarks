import numpy as np
import tensorflow as tf
from sciml_bench.benchmarks.dms_classifier.constants import IMG_HEIGHT, IMG_WIDTH, N_CHANNELS, N_CLASSES
from sciml_bench.benchmarks.dms_classifier.model import dms_classifier


def test_dms_classifier():
    model = dms_classifier((IMG_HEIGHT, IMG_WIDTH, N_CHANNELS))

    assert isinstance(model, tf.keras.Model)
    assert model.input_shape == (None, IMG_HEIGHT, IMG_WIDTH, N_CHANNELS)
    assert model.output_shape == (None, N_CLASSES)


def test_dms_classifier_feed_forward():
    model = dms_classifier((IMG_HEIGHT, IMG_WIDTH, N_CHANNELS))
    output = model.predict(np.random.random((1, IMG_HEIGHT, IMG_WIDTH, N_CHANNELS)))
    assert output.shape == (1, N_CLASSES)


def test_dms_classifier_backprop():
    X = np.random.random((1, IMG_HEIGHT, IMG_WIDTH, N_CHANNELS))
    Y = np.random.random((1, N_CLASSES))
    model = dms_classifier((IMG_HEIGHT, IMG_WIDTH, N_CHANNELS), learning_rate=0.001)
    model.compile(loss='binary_crossentropy', optimizer='adam')
    history = model.fit(x=X, y=Y)
    assert isinstance(history, tf.keras.callbacks.History)
