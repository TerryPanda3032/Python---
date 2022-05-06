from keras.datasets import mnist
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers import Convolution2D,Activation,MaxPooling2D,Flatten,Dense


nb_class = 10       #代表10个类别
nb_epoch = 2       #迭代4次epoch
batchsize = 128     #批次 根据自己的电脑配置设置

(X_train,Y_train),(X_test,Y_test) = mnist.load_data()

X_train = X_train.reshape(-1,28,28,1) #-1代表未知，系统自己找，也可以自己设置60000，因为图片只有黑白通道所以设置1 RGB图片设置3
X_test = X_test.reshape(-1,28,28,1)

#归一化（收敛）
# X_train = X_train.astype('float32')
# X_test = X_test.astype('float32')
# X_train /= 255.0
# X_test /= 255.0
#- 7s 117us/step - loss: 0.0870 - acc: 0.9741 - val_loss: 0.0742 - val_acc: 0.9769

#标签转换为One-hot格式 [0,0,0,0,0,1,0,0,0,0] = 5
Y_train = np_utils.to_categorical(Y_train,nb_class)
Y_test = np_utils.to_categorical(Y_test,nb_class)

#初始化模型
model = Sequential()

#1st
model.add(Convolution2D(
    filters=32,             #32个卷积核
    kernel_size=(5,5),      #卷积核设置(5,5)
    padding='same',         #步长
    input_shape=(28,28,1)   #输入图片的维度
))
model.add(Activation('relu'))
model.add(MaxPooling2D(
    pool_size=(2,2),    #设置2*2的核
    strides=(2,2),      #跳过2*2执行
    padding='same',     #步长
))

#2nd
model.add(Convolution2D(
    filters=64,             #64个卷积核
    kernel_size=(5,5),      #卷积核设置(5,5)
    padding='same',         #步长
    input_shape=(28,28,1)   #输入图片的维度
))
model.add(Activation('relu'))
model.add(MaxPooling2D(
    pool_size=(2,2),    #设置2*2的核
    strides=(2,2),      #跳过2*2执行
    padding='same',     #步长
))

#1st Dense
model.add(Flatten())
model.add(Dense(64))
model.add(Activation('relu'))
model.add(Dense(32))
model.add(Activation('relu'))
model.add(Dense(16))
model.add(Activation('relu'))

#2nd Dense
model.add(Dense(10)) #tabel
model.add(Activation('softmax'))

#Optimizer and setup Param


#compile model
model.compile(
    
    loss='categorical_crossentropy',
    metrics=['accuracy'],
)

#fit model
model.fit(
    x=X_train,
    y=Y_train,
    epochs=nb_epoch,
    batch_size=batchsize,
    validation_data=(X_test,Y_test)
)
model.save('yyds.h5')