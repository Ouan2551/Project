import tensorflow as tf

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

if tf.config.list_physical_devices('GPU'):
    print("GPU devices found:", tf.config.list_physical_devices('GPU'))
    # Optional: Run a simple TensorFlow operation on the GPU
    with tf.device('/GPU:0'):  # Use the first GPU
        a = tf.random.normal((1000, 1000))
        b = tf.random.normal((1000, 1000))
        c = tf.matmul(a, b)
    print("GPU computation successful.")
else:
    print("TensorFlow is using CPU.")