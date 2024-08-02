import os

# The path to the python exectuable
EXEC_HOME = os.path.dirname(__file__)
# The project root directory
PROJECT_ROOT = os.path.join(EXEC_HOME, os.pardir)
# The user home directory
USER_HOME = os.path.expanduser("~")

# data paths
DATA_PATH = os.path.join(PROJECT_ROOT, 'data')
IMG_PATH = os.path.join(PROJECT_ROOT, 'data', 'stimuli')
XML_PATH = os.path.join(PROJECT_ROOT, 'data', 'segmentations')
DRAWINGS_PATH = os.path.join(PROJECT_ROOT, 'data', 'drawings')

# results path
RESULTS_PATH = os.path.join(PROJECT_ROOT, 'results')



