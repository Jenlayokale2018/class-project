
import requests
import json
import pymysql.cursors
import sys

subscription_key = 'add your subscription key here'
assert subscription_key
face_api_url = 'http://imsyafiq.xyz:8082/azure-face-api/detect'

image_url = input("Please enter image url: ")
headers = { 'X-Gravitee-Api-Key': subscription_key }
params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'false',
    'returnFaceAttributes': 'emotion',
}

response = requests.post(face_api_url, params=params, headers=headers, json={"url": image_url})

if response.status_code != 200 :
    sys.exit(response.json())

conn = pymysql.connect(db="image_service", host="127.0.0.1", user="root", password="password", use_unicode=0,charset="utf8")
try:
    for val in response.json():
        emotions = val['faceAttributes']['emotion']
        with conn.cursor() as cursor:
                # Create a new record
                sql = "INSERT INTO `face_emotions` (`face_id`, `emotion`) VALUES (%s, %s)"
                cursor.execute(sql, (val['faceId'], str(emotions)))

                # connection is not autocommit by default. So you must commit to save
                # your changes.
        conn.commit()
    with conn.cursor() as cursor:
            # Read a single record
        sql = "SELECT * FROM `face_emotions`"
        cursor.execute(sql)
        result = cursor.fetchall()
        print(result)
finally:
    conn.close()   
            

