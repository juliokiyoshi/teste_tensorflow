from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
import sys
import time
from datetime import datetime

begin = time.time()

#folder = sys.argv[1]
length = 731
length = int(sys.argv[1])
if (length > 731):
    print("Using maximum length: 731")
    lenght = 731
again = int(sys.argv[2])
folder_name = "hot_dog"

model = ResNet50(weights='imagenet')

images = []
count = 0
for i in range(length):
    img_path = folder_name + '/' + str(i) + '.jpg'  
    img = image.load_img(img_path, target_size=(224, 224))
    images.append(image.img_to_array(img))
    images[i] = np.expand_dims(images[i], axis=0)
    images[i] = preprocess_input(images[i])

for j in range(again):
    for i in range(length):
        prediction = model.predict(images[i])
        #print(decode_predictions(prediction[i], top=1)[0][0][1])
        strPrediction = decode_predictions(prediction, top=1)[0][0][1]
        if (strPrediction == 'hotdog'):
            count += 1
        else:
            #print(str(i) + " -> " + strPrediction)
            pass

print("Begin: " + datetime.now().strftime("%H:%M:%S"))
print("End: " + datetime.now().strftime("%H:%M:%S"))
print("RIGHTS: {}".format(count))
print("WRONGS: {}".format(again*length - count))
print("ACC: {}".format(count/(again*length)))
print("Time Elapsed: {}s".format(time.time() - begin))
