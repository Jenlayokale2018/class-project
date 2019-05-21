import requests
import json
import pymysql.cursors

conn = pymysql.Connection(db="image_service", host="127.0.0.1", user="root", password="password", use_unicode=0,charset="utf8")

crsr = conn.cursor()
crsr.execute("SELECT * FROM face_emotions")

print ("cursor.description: ", crsr.description)
# TODO: Capture class image and get url of the image
# TODO: Get api documentation of the app to capture image and consume it here
image_url = input("Please enter image url: ")
subscription_key = '38af3cd0-be70-4435-a980-7bb408d573d7'
assert subscription_key

face_api_url = 'http://imsyafiq.xyz:8082/azure-face-api/detect'
headers = { 'X-Gravitee-Api-Key': subscription_key }
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}
print(image_url)

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})

if response.status_code != 200 :
	print(response.json())
else:
    #TODO: if valid loop through response and save faceid, and emotions.
    for val in response.json():
        print(val['faceId'])
        print(val['faceAttributes']['emotion'])
        


