from __future__ import print_function
import urllib
import time
import boto3
import json
import requests
from urllib.request import urlopen
transcribe = boto3.client('transcribe')
job_name = "enter_Your_Job_name"
job_uri = "Upload_your_s3_bucket_name"
transcribe.start_transcription_job(
    TranscriptionJobName=job_name,
    Media={'MediaFileUri': job_uri},
    MediaFormat='mp4',
    LanguageCode='en-US'
)
while True:
    status = transcribe.get_transcription_job(TranscriptionJobName=job_name)
    if status['TranscriptionJob']['TranscriptionJobStatus'] in ['COMPLETED', 'FAILED']:
        break
        print("Not ready yet...")
        time.sleep(5)
print(status)
print('job are created...')
# TranscriptFileUri

url = status['TranscriptionJob']['Transcript']['TranscriptFileUri'];
r = requests.get(url, stream = True)
with open("jsohgnn.json", "wb") as Pypdf:
    for chunk in r.iter_content(chunk_size = 1024):
        if chunk:
            Pypdf.write(chunk)
