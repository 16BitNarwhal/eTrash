print('importing')

# imports
from tensorflow.keras.models import load_model
import numpy as np
import cv2

# transform opencv image, size=(height, width)
def fit_image(img, size=(224, 224), cvt_color=cv2.COLOR_BGR2RGB):
  scale_percent = max(size[0] / img.shape[0], size[1] / img.shape[1])
  width = int(img.shape[1] * scale_percent)
  height = int(img.shape[0] * scale_percent)

  # convert color and resize image
  if cvt_color != None:
    img = cv2.cvtColor(img, cvt_color)
  scale_img = cv2.resize(img, (width, height), interpolation=cv2.INTER_NEAREST)

  # crop from center of image
  center = (int(scale_img.shape[0]/2), int(scale_img.shape[1]/2))
  half_size = (int(size[0]/2), int(size[1]/2))
  crop_img = scale_img[center[0]-half_size[0]:center[0]+half_size[0], center[1]-half_size[1]:center[1]+half_size[1]]
  return crop_img

# preprocess opencv image for classification
def preprocess_image(image):
  # transform image
  image = fit_image(image)
  image_array = np.asarray(image)
  normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1 # normalize image
  
  # reshape to fit the model
  data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
  data[0] = normalized_image_array
  return data

print('now loading model')
model = load_model('keras_model.h5')
print('finished loading model')

def predict(frame):

  labels = {
    0: 'none',
    1: 'trash',
    2: 'recycle',
    3: 'compost'
  }

  # predict the class
  frame = fit_image(frame, cvt_color=None)
  inp = preprocess_image(frame)
  prediction = model.predict(inp)
  result = np.argmax(prediction)

  return labels[result]
  
'''
if __name__=="__main__":
  cap = cv2.VideoCapture(0)

  while True:
    
    ret, frame = cap.read()
    
    if not ret:
      continue
      
    result = predict(inp)
    
    print(result)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
      break
      
  cap.release()
  '''

    
