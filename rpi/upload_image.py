import os
import uuid
import firebase_admin
from firebase_admin import credentials, auth, storage, firestore
from time import sleep

def get_path(filename):
	return os.path.join(os.path.dirname(__file__), filename)
	
cred = credentials.Certificate(get_path('firebase-sdk.json'))
firebase_admin.initialize_app(cred, { 'storageBucket': 'etrash-35222.appspot.com' })

bucket = storage.bucket()
db = firestore.client()

email = 'ericzh1616@gmail.com'

def upload_image(filename, cat):
	save_name = str(uuid.uuid1())
	
	blob = bucket.blob(f'images/{save_name}.jpg')
	blob.upload_from_filename(get_path(filename))
	
	url = blob.public_url
	
	user = auth.get_user_by_email(email)
	
	data = {
		'uid': user.uid,
		'category': cat,
		'url': blob.public_url,
		'timestamp': firestore.SERVER_TIMESTAMP
	}
	
	db.collection('garbage_history').document(save_name).set(data)
