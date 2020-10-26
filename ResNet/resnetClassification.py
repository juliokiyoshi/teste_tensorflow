from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
#import sys
#lenght = int(sys.argv[2])
#folder = sys.argv[1]
length = 736
#folder_name = "/home/ubuntu/prediction/hot_dog"
folder_name = "hot_dog"

model = ResNet50(weights='imagenet')

images = []
prediction = []
count = 0
for i in range(lenght):
    img_path = folder_name + '/' + str(i) + '.jpg'  
    img = image.load_img(img_path, target_size=(224, 224))
    images.append(image.img_to_array(img))
    images[i] = np.expand_dims(images[i], axis=0)
    images[i] = preprocess_input(images[i])
    
    prediction.append(model.predict(images[i]))
    #print(decode_predictions(prediction[i], top=1)[0][0][1])
    strPrediction = decode_predictions(prediction[i], top=1)[0][0][1]
    if (strPrediction == 'hotdog'):
        count += 1
    else:
        print(str(i) + " -> " + strPrediction)

print("RIGHTS: {}".format(count))
print("WRONGS: {}".format(lenght - count))
print("ACC: {}".format(count/length))
