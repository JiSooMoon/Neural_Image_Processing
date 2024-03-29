
import os
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Conv2D, MaxPooling2D
from tensorflow.keras.layers import Dense, Dropout, Flatten
import matplotlib.pyplot as plt
import random
import logging

os.environ["CUDA_VISIBILE_DEVICES"] = "1"

random.seed(1618)
np.random.seed(1618)
tf.set_random_seed(1618)

tf.logging.set_verbosity(tf.logging.ERROR)
# logger = tf.get_logger()
# logger.setLevel(logging.ERROR)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

# ALGORITHM = "guesser"
ALGORITHM = "tf_net"
# ALGORITHM = "tf_conv"

# DATASET = "mnist_d"
# DATASET = "mnist_f"
# DATASET = "cifar_10"
# DATASET = "cifar_100_f"
DATASET = "cifar_100_c"

if DATASET == "mnist_d":
    NUM_CLASSES = 10
    IH = 28
    IW = 28
    IZ = 1
    IS = 784
elif DATASET == "mnist_f":
    NUM_CLASSES = 10
    IH = 28
    IW = 28
    IZ = 1
    IS = 784
elif DATASET == "cifar_10":
    # pass                                 # TODO: Add this case.
    NUM_CLASSES = 10
    IH = 32
    IW = 32
    IZ = 3
    IS =  3072
elif DATASET == "cifar_100_f":
    # pass  
    NUM_CLASSES = 100
    IH = 32
    IW = 32
    IZ = 3
    IS =  3072                               # TODO: Add this case.
elif DATASET == "cifar_100_c":
    # pass                                 # TODO: Add this case.
    NUM_CLASSES = 20
    IH = 32
    IW = 32
    IZ = 3
    IS =  3072  

#=========================<Classifier Functions>================================

def guesserClassifier(xTest):
    ans = []
    for entry in xTest:
        pred = [0] * NUM_CLASSES
        pred[random.randint(0, 9)] = 1
        ans.append(pred)
    return np.array(ans)


def buildTFNeuralNet(x, y, eps = 6):
    # pass        #TODO: Implement a standard ANN here.
 
    model = tf.keras.models.Sequential()
    model.add(tf.keras.layers.Dense(600, input_dim = IS, activation=tf.nn.sigmoid))
    model.add(tf.keras.layers.Dense(600,activation=tf.nn.sigmoid))
    model.add(tf.keras.layers.Dense(600,activation=tf.nn.sigmoid))
    
    model.add(tf.keras.layers.Dropout(rate=0.3))
    model.add(tf.keras.layers.Dense(600,activation=tf.nn.sigmoid))
    model.add(tf.keras.layers.Dense(600,activation=tf.nn.sigmoid))
    model.add(tf.keras.layers.Dense(NUM_CLASSES,activation=tf.nn.sigmoid))
    # model.add(tf.keras.layers.Dense(NUM_CLASSES, activation=tf.nn.relu))
    

    model.compile(optimizer='adam', loss=keras.losses.categorical_crossentropy, metrics=['accuracy'])
    model.fit(x,y,1000, 20) #but accuracy is only 96.96%..
    # history = model.fit(x, y, validation_split=0.33, epochs=50, batch_size=1, verbose=0) #but accuracy is only 96.96%..

    # print(history.history.keys())
    # plt.plot(history.history['accuracy'])
    # plt.plot(history.history['val_accuracy'])
    # plt.title('model accuracy')
    # plt.ylabel('accuracy')
    # plt.xlabel('epoch')
    # plt.legend(['train', 'test'], loc='upper left')
    # plt.show()
        
    return model
    # elif DATASET == "mnist_f":
    # elif DATASET == "cifar_10":
    # elif DATASET == "cifar_100_f":
    # elif DATASET == "cifar_100_c":



def buildTFConvNet(x, y, eps = 10, dropout = True, dropRate = 0.2):
    # pass        #TODO: Implement a CNN here. dropout option is required.
    if(DATASET == "mnist_d"):
        model = tf.keras.models.Sequential()

        #add more layers
        model.add(Conv2D(64, kernel_size=(3,3), activation=tf.nn.relu, input_shape=(IH,IW,IZ)))
        model.add(Conv2D(32, kernel_size=(3,3), activation=tf.nn.relu))
        model.add(tf.keras.layers.MaxPooling2D(pool_size = (2,2)))
        model.add(tf.keras.layers.Flatten())
        model.add(Dropout(dropRate))
        model.add(tf.keras.layers.Dense(128,activation=tf.nn.sigmoid))
        model.add(tf.keras.layers.Dense(128,activation=tf.nn.sigmoid))
        
     
        
        model.add(Dense(NUM_CLASSES, activation=tf.nn.sigmoid))
        
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(x, y, 1000, eps)
        # model.fit(x,y,1000, 1)
        return model
        
    elif DATASET == "mnist_f":
        model = tf.keras.models.Sequential()

        #add more layers
        model.add(Conv2D(64, kernel_size=(3,3), activation=tf.nn.relu, input_shape=(IH,IW,IZ)))
        model.add(Conv2D(32, kernel_size=(3,3), activation=tf.nn.relu))
        model.add(tf.keras.layers.MaxPooling2D(pool_size = (2,2)))
        model.add(tf.keras.layers.Flatten())
        model.add(Dropout(dropRate))
        model.add(tf.keras.layers.Dense(625,activation=tf.nn.sigmoid))
        model.add(tf.keras.layers.Dense(625,activation=tf.nn.sigmoid))
        
     
        
        model.add(Dense(NUM_CLASSES, activation=tf.nn.sigmoid))
        
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(x, y, 1000, 13) #91.92%
        # model.fit(x,y,1000, 1)
        return model
    elif DATASET == "cifar_10":
        model = tf.keras.models.Sequential()

        model.add(Conv2D(32, kernel_size=(3,3), activation=tf.nn.relu, input_shape=(IH,IW,IZ)))
        model.add(Conv2D(64, kernel_size=(3,3), activation=tf.nn.relu, strides=2))
        
        model.add(tf.keras.layers.MaxPooling2D(pool_size = (2,2)))
        model.add(Flatten())
        model.add(Dropout(dropRate))
        model.add(tf.keras.layers.Dense(625,activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(625,activation=tf.nn.relu))

        
        
        model.add(Dense(NUM_CLASSES, activation=tf.nn.softmax))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(x,y,640, 25)
        return model
    elif DATASET == "cifar_100_f":
        model = tf.keras.models.Sequential()

        model.add(Conv2D(32, kernel_size=(3,3), activation=tf.nn.relu, input_shape=(IH,IW,IZ)))
        model.add(Conv2D(64, kernel_size=(3,3), activation=tf.nn.relu, strides=2))
        
        model.add(tf.keras.layers.MaxPooling2D(pool_size = (2,2)))
        model.add(Flatten())
        model.add(Dropout(dropRate))
        model.add(tf.keras.layers.Dense(625,activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(625,activation=tf.nn.relu))

        
        
        model.add(Dense(NUM_CLASSES, activation=tf.nn.softmax))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(x,y,640, 50)
        return model
    elif DATASET == "cifar_100_c":
        model = tf.keras.models.Sequential()

        model.add(Conv2D(32, kernel_size=(3,3), activation=tf.nn.relu, input_shape=(IH,IW,IZ)))
        model.add(Conv2D(64, kernel_size=(3,3), activation=tf.nn.relu, strides=2))
        
        model.add(tf.keras.layers.MaxPooling2D(pool_size = (2,2)))
        model.add(Flatten())
        model.add(Dropout(dropRate))
        model.add(tf.keras.layers.Dense(625,activation=tf.nn.relu))
        model.add(tf.keras.layers.Dense(625,activation=tf.nn.relu))

        
        
        model.add(Dense(NUM_CLASSES, activation=tf.nn.softmax))
        model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
        model.fit(x,y,640, 50)
        return model

#=========================<Pipeline Functions>==================================

def getRawData():
    if DATASET == "mnist_d":
        mnist = tf.keras.datasets.mnist
        (xTrain, yTrain), (xTest, yTest) = mnist.load_data()
    elif DATASET == "mnist_f":
        mnist = tf.keras.datasets.fashion_mnist
        (xTrain, yTrain), (xTest, yTest) = mnist.load_data()
    elif DATASET == "cifar_10":
        # pass      # TODO: Add this case.
        mnist = tf.keras.datasets.cifar10
        (xTrain, yTrain), (xTest, yTest) = mnist.load_data()
        xTrain = xTrain.astype('float32')
        xTest = xTest.astype('float32')
        xTrain /= 255
        xTest /= 255
    elif DATASET == "cifar_100_f":
        # pass      # TODO: Add this case.
        mnist = tf.keras.datasets.cifar100
        (xTrain, yTrain), (xTest, yTest) = mnist.load_data('fine')
        xTrain = xTrain.astype('float32')
        xTest = xTest.astype('float32')
        xTrain /= 255
        xTest /= 255
    elif DATASET == "cifar_100_c":
        # pass      # TODO: Add this case.
        mnist = tf.keras.datasets.cifar100
        (xTrain, yTrain), (xTest, yTest) = mnist.load_data('coarse')
        xTrain = xTrain.astype('float32')
        xTest = xTest.astype('float32')
        xTrain /= 255
        xTest /= 255
    else:
        raise ValueError("Dataset not recognized.")
    print("Dataset: %s" % DATASET)
    print("Shape of xTrain dataset: %s." % str(xTrain.shape))
    print("Shape of yTrain dataset: %s." % str(yTrain.shape))
    print("Shape of xTest dataset: %s." % str(xTest.shape))
    print("Shape of yTest dataset: %s." % str(yTest.shape))
    return ((xTrain, yTrain), (xTest, yTest))



def preprocessData(raw):
    ((xTrain, yTrain), (xTest, yTest)) = raw
    if ALGORITHM != "tf_conv":
        # print("XTrain: " , xTrain.shape[1])
        # print("XTrain.shape[0] : " , xTrain.shape[0])
        xTrainP = xTrain.reshape((xTrain.shape[0], IS))
        xTestP = xTest.reshape((xTest.shape[0], IS))
    else:
        xTrainP = xTrain.reshape((xTrain.shape[0], IH, IW, IZ))
        xTestP = xTest.reshape((xTest.shape[0], IH, IW, IZ))
    yTrainP = to_categorical(yTrain, NUM_CLASSES)
    yTestP = to_categorical(yTest, NUM_CLASSES)
    print("New shape of xTrain dataset: %s." % str(xTrainP.shape))
    print("New shape of xTest dataset: %s." % str(xTestP.shape))
    print("New shape of yTrain dataset: %s." % str(yTrainP.shape))
    print("New shape of yTest dataset: %s." % str(yTestP.shape))
    return ((xTrainP, yTrainP), (xTestP, yTestP))



def trainModel(data):
    xTrain, yTrain = data
    if ALGORITHM == "guesser":
        return None   # Guesser has no model, as it is just guessing.
    elif ALGORITHM == "tf_net":
        print("Building and training TF_NN.")
        return buildTFNeuralNet(xTrain, yTrain)
    elif ALGORITHM == "tf_conv":
        print("Building and training TF_CNN.")
        return buildTFConvNet(xTrain, yTrain)
    else:
        raise ValueError("Algorithm not recognized.")



def runModel(data, model):
    if ALGORITHM == "guesser":
        return guesserClassifier(data)
    elif ALGORITHM == "tf_net":
        print("Testing TF_NN.")
        preds = model.predict(data)
        for i in range(preds.shape[0]):
            oneHot = [0] * NUM_CLASSES
            oneHot[np.argmax(preds[i])] = 1
            preds[i] = oneHot
        return preds
    elif ALGORITHM == "tf_conv":
        print("Testing TF_CNN.")
        preds = model.predict(data)
        for i in range(preds.shape[0]):
            oneHot = [0] * NUM_CLASSES
            oneHot[np.argmax(preds[i])] = 1
            preds[i] = oneHot
        return preds
    else:
        raise ValueError("Algorithm not recognized.")



def evalResults(data, preds):
    xTest, yTest = data
    acc = 0
    for i in range(preds.shape[0]):
        if np.array_equal(preds[i], yTest[i]):   acc = acc + 1
    accuracy = acc / preds.shape[0]
    print("Classifier algorithm: %s" % ALGORITHM)
    print("Classifier accuracy: %f%%" % (accuracy * 100))
    print()



#=========================<Main>================================================

def main():
    raw = getRawData()
    data = preprocessData(raw)
    model = trainModel(data[0])
    preds = runModel(data[1][0], model)
    evalResults(data[1], preds)



if __name__ == '__main__':
    main()

