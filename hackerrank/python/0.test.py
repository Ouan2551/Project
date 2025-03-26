import os

# Check if there is valid GPU to be used
if(tf.test.is_gpu_available(cuda_only=True)):
    os.environ['CUDA_VISIBLE_DEVICES'] = '0'