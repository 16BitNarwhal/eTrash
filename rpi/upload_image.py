import os
import uuid
import firebase_admin
from firebase_admin import credentials, auth, storage, firestore

def get_path(filename):
  return os.path.join(os.path.dirname(__file__), filename)

cred = credentials.Certificate(get_path('firebase-sdk.json'))
firebase_admin.initialize_app(cred, { 'storageBucket': 'etrash-35222.appspot.com' })

bucket = storage.bucket()
db = firestore.client()

email = 'ericzh1616@gmail.com'

def upload_image(filename, category):
  
  save_name = str(uuid.uuid1())

  # uuid - unique random id
  blob = bucket.blob(f'images/{save_name}.jpg')
  blob.upload_from_filename(get_path(filename))

  # get the image url
  url = blob.public_url

  # get the user
  user = auth.get_user_by_email(email)
  
  # firestore
  data = {
    'uid': user.uid,
    'category': category, # trash, recycle, compost
    'url': blob.public_url,
    'timestamp': firestore.SERVER_TIMESTAMP
  }
  
  db.collection('garbage_history').document(save_name).set(data)

if __name__ == '__main__':
  upload_image('test_apple.jpg', 'compost')
  upload_image('test_paper.jpg', 'recycle')