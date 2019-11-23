from setuptools import setup

setup(
    name              = 'objectDetectionD3MWrapper',
    version           = '0.1.0',
    description       = 'Keras implementation of RetinaNet as a D3M primitive.',
    author            = 'Sanjeev Namjoshi',
    author_email      = 'sanjeev@yonder.co',
    packages          = ['objectDetectionD3MWrapper'],
    install_requires  = ['numpy>=1.14.0',
                         'object_detection_retinanet @ git+https://github.com/NewKnowledge/object-detection-retinanet@f55d251eb1ce4aaa639e3a2c1a1cb363b59b7ecf#egg=object_detection_retinanet'],                        
    entry_points      = {
        'd3m.primitives': [
            'object_detection.retinanet_convolutional_neural_network = objectDetectionD3MWrapper:ObjectDetectionRNPrimitive'
        ],
    },
)
