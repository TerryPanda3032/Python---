from keras.models import load_model
import numpy as np
import cv2


model = load_model('C:\\Users\\pxm\\Desktop\\909\\yyds.h5')


def pred(filename):
    pred_img = cv2.imread(filename)    #读取图片
	#使用cv.resize将原图大小(224, 222,3) 转换成 (28,28,3)
    pred_img = cv2.resize(pred_img,(28,28))                          #resize图片大小
    #将图片转换成灰度图 从(28,28,3) ---> (28,28)
    pred_img = cv2.cvtColor(pred_img,cv2.COLOR_BGR2GRAY)             #BGR转灰度图
    #将图片转换成np数组格式
    pred_img = np.array(pred_img)                                    #转换np数组格式
    #-1代表未知 系统自己找 也可以自己设置60000 最后1代表灰度只有黑白色
    pred_img = pred_img.reshape(-1,28,28,1)                          #reshape图片
	#将处理好的图片丢到模型中预测
    prediction = model.predict(pred_img)                             #使用模型测试图片
    Final_prediction = [result.argmax() for result in prediction][0] #取预测出来的最大值 #[1,5,3,4,2,9,8,7]
    
	#遍历输入0-9的概率
    for i in prediction[0]:
        print('Percent:{:.10f}'.format(i))
    return Final_prediction                           #使用模型测试图片
    
	

if __name__ =='__main__':
    res = pred('C:\\Users\\pxm\Desktop\\909\\3.png')
    print(res)