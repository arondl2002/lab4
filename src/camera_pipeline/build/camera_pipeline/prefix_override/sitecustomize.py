import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/aron-larsen/lab4/src/camera_pipeline/install/camera_pipeline'
