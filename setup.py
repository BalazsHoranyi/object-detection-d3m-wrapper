from setuptools import setup

setup(
    name              = 'objectDetectionD3MWrapper',
    version           = '0.1.0',
    description       = 'Keras implementation of RetinaNet as a D3M primitive.',
    author            = 'Sanjeev Namjoshi',
    author_email      = 'sanjeev@yonder.co',
    packages          = ['objectDetectionD3MWrapper'],
    install_requires  = ["object-detection-retinanet @ git+https://github.com/NewKnowledge/object-detection-retinanet.git@dcfdb2442564893a92a0ba0eb0aac9958a28f59d#egg=object-detection-retinanet"],                        
    entry_points      = {
        'd3m.primitives': [
            'object_detection.retinanet_convolutional_neural_network = objectDetectionD3MWrapper:ObjectDetectionRNPrimitive'
        ],
    },
)