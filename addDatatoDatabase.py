
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {           #writing in json format
    'databseURL':"https://faceattendancerealtime-25b60-default-rtdb.firebaseio.com/"
})

ref =

