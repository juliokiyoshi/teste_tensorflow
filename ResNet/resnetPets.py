from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
import numpy as np
#import sys
#lenght = int(sys.argv[2])
#folder = sys.argv[1]
length = 2000
folder_dogs = "cats_and_dogs_filtered/validation/dogs"
folder_catc = "cats_and_dogs_filtered/validation/cats"

model = ResNet50(weights='imagenet')

images_dogs = []
images_cats = []
count = 0
for i in range(length):
    img_path = folder_dogs + '/' + str(i) + '.jpg'
    img = image.load_img(img_path, target_size=(224, 224))
    images_dogs.append(image.img_to_array(img))
    images_dogs[i] = np.expand_dims(images_dogs[i], axis=0)
    images_dogs[i] = preprocess_input(images_dogs[i])

    img_path = folder_cats + '/' + str(i) + '.jpg'
    img = image.load_img(img_path, target_size=(224, 224))
    images_cats.append(image.img_to_array(img))
    images_cats[i] = np.expand_dims(images_cats[i], axis=0)
    images_cats[i] = preprocess_input(images_cats[i])

    prediction = model.predict(images_dogs[i])
    #print(decode_predictions(prediction[i], top=1)[0][0][1])
    strPrediction = decode_predictions(prediction, top=1)[0][0][1]
    if (strPrediction == 'dog'):
        count += 1
    else:
        #print(str(i) + " -> " + strPrediction)
        pass

    prediction = model.predict(images_cats[i])
    #print(decode_predictions(prediction[i], top=1)[0][0][1])
    strPrediction = decode_predictions(prediction[i], top=1)[0][0][1]
    if ('cat' in strPrediction):
        count += 1
    else:
        #print(str(i) + " -> " + strPrediction)
        pass

print("RIGHTS: {}".format(count))
print("WRONGS: {}".format(2*length - count))
print("ACC: {}".format(count/(2*length)))
