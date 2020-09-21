import gluoncv
import mxnet
import numpy

import googlenet_mod1



_CNN_1 = mxnet.gluon.nn.HybridSequential()
_CNN_1.add(mxnet.gluon.nn.Conv2D(channels = 50, kernel_size = 10, activation = "relu"))
_CNN_1.add(mxnet.gluon.nn.MaxPool2D(pool_size = 2, strides = 2))
_CNN_1.add(mxnet.gluon.nn.Conv2D(channels = 30, kernel_size = 5, activation = "relu"))
_CNN_1.add(mxnet.gluon.nn.MaxPool2D(pool_size = 2, strides = 2))
_CNN_1.add(mxnet.gluon.nn.Conv2D(channels = 10, kernel_size = 2, activation = "relu"))
_CNN_1.add(mxnet.gluon.nn.MaxPool2D(pool_size = 2, strides = 2))
_CNN_1.add(mxnet.gluon.nn.Flatten())
_CNN_1.add(mxnet.gluon.nn.Dense(50, activation = "relu"))
_CNN_1.add(mxnet.gluon.nn.Dense(1, activation = "sigmoid"))



_CNN_2 = mxnet.gluon.nn.HybridSequential()
_CNN_2.add(mxnet.gluon.nn.Conv2D(channels = 50, kernel_size = 10, activation = "relu"))
_CNN_2.add(mxnet.gluon.nn.MaxPool2D(pool_size = 2, strides = 2))
_CNN_2.add(mxnet.gluon.nn.Conv2D(channels = 30, kernel_size = 5, activation = "relu"))
_CNN_2.add(mxnet.gluon.nn.MaxPool2D(pool_size = 2, strides = 2))
_CNN_2.add(mxnet.gluon.nn.Conv2D(channels = 10, kernel_size = 2, activation = "relu"))
_CNN_2.add(mxnet.gluon.nn.MaxPool2D(pool_size = 2, strides = 2))
_CNN_2.add(mxnet.gluon.nn.Flatten())
_CNN_2.add(mxnet.gluon.nn.Dense(300, activation = "relu"))
_CNN_2.add(mxnet.gluon.nn.Dense(300, activation = "relu"))
_CNN_2.add(mxnet.gluon.nn.Dense(1, activation = "sigmoid"))



# Aravind's autoencoder
class CenteredLayer(mxnet.gluon.nn.HybridSequential):
    def __init__(self, **kwargs):
        super(CenteredLayer, self).__init__(**kwargs)
    
    def forward(self, x):
        return x.softmax(axis=1)

_HolurAE = mxnet.gluon.nn.HybridSequential()
_HolurAE.add(mxnet.gluon.nn.Dense ( 24*24 , activation = "relu"))
_HolurAE.add(mxnet.gluon.nn.Dense ( 8*8   , activation = "relu"))
_HolurAE.add(mxnet.gluon.nn.Dense ( 24*24 , activation = "relu"))
_HolurAE.add(mxnet.gluon.nn.Dense ( 40*40 , activation = "relu"))
_HolurAE.add(mxnet.gluon.nn.Dense ( 40*40                      ))
_HolurAE.add(CenteredLayer()                                    )



# GoogleNet
#_GoogleNet = gluoncv.model_zoo.googlenet(
_GoogleNet = googlenet_mod1.googlenet(
    classes = 2,
    pretrained = False,
    pretrained_base = True,
    ctx = mxnet.gpu(),
    dropout_ratio = 0.4,
    aux_logits = False,
)


# GoogleNet from http://d2l.ai/chapter_convolutional-modern/googlenet.html
class Inception(mxnet.gluon.nn.HybridBlock):
    # c1 - c4 are the number of output channels for each layer in the path
    def __init__(self, c1, c2, c3, c4, **kwargs):
        super(Inception, self).__init__(**kwargs)
        # Path 1 is a single 1 x 1 convolutional layer
        self.p1_1 = mxnet.gluon.nn.Conv2D(c1, kernel_size=1, activation='relu')
        # Path 2 is a 1 x 1 convolutional layer followed by a 3 x 3
        # convolutional layer
        self.p2_1 = mxnet.gluon.nn.Conv2D(c2[0], kernel_size=1, activation='relu')
        self.p2_2 = mxnet.gluon.nn.Conv2D(c2[1], kernel_size=3, padding=1,
                              activation='relu')
        # Path 3 is a 1 x 1 convolutional layer followed by a 5 x 5
        # convolutional layer
        self.p3_1 = mxnet.gluon.nn.Conv2D(c3[0], kernel_size=1, activation='relu')
        self.p3_2 = mxnet.gluon.nn.Conv2D(c3[1], kernel_size=5, padding=2,
                              activation='relu')
        # Path 4 is a 3 x 3 maximum pooling layer followed by a 1 x 1
        # convolutional layer
        self.p4_1 = mxnet.gluon.nn.MaxPool2D(pool_size=3, strides=1, padding=1)
        self.p4_2 = mxnet.gluon.nn.Conv2D(c4, kernel_size=1, activation='relu')

    def hybrid_forward(self, F, x):
        p1 = self.p1_1(x)
        p2 = self.p2_2(self.p2_1(x))
        p3 = self.p3_2(self.p3_1(x))
        p4 = self.p4_2(self.p4_1(x))
        # Concatenate the outputs on the channel dimension
        return F.concat(p1, p2, p3, p4, dim=1)

b1 = mxnet.gluon.nn.HybridSequential()
b1.add(mxnet.gluon.nn.Conv2D(64, kernel_size=7, strides=2, padding=3, activation='relu'),
       mxnet.gluon.nn.MaxPool2D(pool_size=3, strides=2, padding=1))

b2 = mxnet.gluon.nn.HybridSequential()
b2.add(mxnet.gluon.nn.Conv2D(64, kernel_size=1, activation='relu'),
       mxnet.gluon.nn.Conv2D(192, kernel_size=3, padding=1, activation='relu'),
       mxnet.gluon.nn.MaxPool2D(pool_size=3, strides=2, padding=1))

b3 = mxnet.gluon.nn.HybridSequential()
b3.add(Inception(64, (96, 128), (16, 32), 32),
       Inception(128, (128, 192), (32, 96), 64),
       mxnet.gluon.nn.MaxPool2D(pool_size=3, strides=2, padding=1))

b4 = mxnet.gluon.nn.HybridSequential()
b4.add(Inception(192, (96, 208), (16, 48), 64),
       Inception(160, (112, 224), (24, 64), 64),
       Inception(128, (128, 256), (24, 64), 64),
       Inception(112, (144, 288), (32, 64), 64),
       Inception(256, (160, 320), (32, 128), 128),
       mxnet.gluon.nn.MaxPool2D(pool_size=3, strides=2, padding=1))

b5 = mxnet.gluon.nn.HybridSequential()
b5.add(Inception(256, (160, 320), (32, 128), 128),
       Inception(384, (192, 384), (48, 128), 128),
       mxnet.gluon.nn.GlobalAvgPool2D())

_GoogleNet_d2lai = mxnet.gluon.nn.HybridSequential()
_GoogleNet_d2lai.add(b1, b2, b3, b4, b5, mxnet.gluon.nn.Dense(50))

_GoogleNet_d2lai.add(mxnet.gluon.nn.Dense(1, activation = "sigmoid"))


d_network = {
    "CNN-1": _CNN_1,
    
    "CNN-2": _CNN_2,
    
    "HolurAE": _HolurAE,
    
    "GoogleNet": _GoogleNet,
    
    "GoogleNet-d2lai": _GoogleNet_d2lai,
}

