#!/usr/bin/python3
# Requires PyAudio.
# -*- coding: utf-8 -*-
from termcolor import colored
token=''
with open('config.json') as config_json:
    config_data = json.load(config_json)
for p in config_data['stt_engine']:
    if p['name'] == 'stt_fpt':
        token=p['token']

def main():
#   print ('FPT')
    r = sr.Recognizer()
    import random
#   print ('FPT1')
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    with open('tmp/record.wav', "wb") as f:
        f.write(audio.get_wav_data())
    data = ""
    try:
        import requests
        url = 'https://api.fpt.ai/hmi/asr/general'
        payload = open('tmp/record.wav', 'rb').read()
        headers = {'api-key': token}
        response = requests.post(url=url, data=payload, headers=headers)
        txt = response.json()
#       print (txt)
        import json
        for element in txt['hypotheses']:
            data = element['utterance'] 
#   print(response.json())
#       data = r.recognize_google(audio, language = "vi-VN")
        print(colored('[BOT-STT-FPT]: '+data,'green'))
    except sr.UnknownValueError:    
        print('Sao bạn không nói gì')
        data ='ĐƯỢC RỒI'
        pass
    except sr.RequestError as e:
        print('èo èo'+ e)
        pass
    return data


if __name__ == '__main__':
    main()
# [END speech_transcribe_streaming_mic]
