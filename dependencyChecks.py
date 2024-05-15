import tensorflow
import tf_keras as keras
import numpy
import matplotlib
import sklearn
import sys

def main():
    print("System python interpreter version :",sys.version)
    print("Tensorflow version :",tensorflow.__version__)
    print("Keras version :", keras.__version__)
    print("Numpy version",numpy.__version__)
    print("Matplotlib version", matplotlib.__version__)
    print("Scikit-learn version",sklearn.__version__)

if __name__ == '__main__':
    main()