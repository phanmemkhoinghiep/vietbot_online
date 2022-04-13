import json

data = {}
data['mic'] = []
data['mic'].append({
    'type': 'None Respeaker Mic',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False            
})
data['mic'].append({
    'type': 'ReSpeaker 2-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker 2-Mics Pi HAT with WS281x LED',
    'led_off_mode': 2,
    'led_off_color': 'fffcff',
    'led_wakeup_mode': 2,
    'led_wakeup_color': '128043',  
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker 4-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker Mic Array v2.0',
    'led_off_mode': 1,
    'led_off_color': 'fffcff',
    'led_wakeup_mode': 2,
    'led_wakeup_color': '074a25',    
    'is_active': True        
})
data['volume'] = []
data['volume'].append({
    'value': 50,
    'type': 'event'    
})
data['volume'].append({
    'value': 50,
    'type': 'speak'    
})
data['volume'].append({
    'value': 50,
    'type': 'playback'    
})
data['hotword_engine'] = []
data['hotword_engine'].append({
    'name': 'snowboy',
    'is_active': False
})
data['hotword_engine'].append({
    'name': 'porcupine',
    'is_active': True,
    'porcupine_access_key': 'pJwv7qAbPrw9yXx2D3QeceV39+Rn+KW35JBTeyEal70VOOWoDvm7JQ=='
})
data['hotword'] = []
data['hotword'].append({
    'type': 'snowboy',
    'file_name': 'snowboy.umdl',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'snowboy',
    'file_name': 'subex.umdl',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'vi-ci-ci_en_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'alexa_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'americano_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'blueberry_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'bumblebee_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'computer_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'grapefruit_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'grasshopper_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey barista_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey google_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': False   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'jarvis_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'ok google_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': False    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'pico clock_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'picovoice_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'porcupine_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'terminator_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
data['continuous_asking'] = []
data['continuous_asking'].append({
    'content': 'hỏi liên tục',
    'is_active': True
})
data['local_stt'] = []
data['local_stt'].append({
    'name': 'stt_gg_free',
    'time_out': 6000,
    'is_active': False    
})
data['local_stt'].append({
    'name': 'stt_gg_cloud',
    'token_file': 'google.json',    
    'time_out': 6000,
    'is_active': True    
})
data['local_stt'].append({
    'name': 'stt_gg_ass',
    'token': '',
    'token_file': '',    
    'time_out': 6000,
    'is_active': False    
})
data['local_stt'].append({
    'name': 'stt_viettel',
    'token': 'SythBY7N8AUnddbzfUk15aBx45uFDAebU7twsjBFqq-jxLrWpxlyXxzdWRNwYE8N',
    'time_out': 4000,
    'is_active': False    
})
data['local_stt'].append({
    'name': 'stt_fpt',
    'token': '',
    'token_file': '',    
    'time_out': '',
    'is_active': False    
})
data['local_tts'] = []
data['local_tts'].append({
    'name': 'tts_gg_free',
    'token': '8sJJ39o7qhfS00FoRUUSIlkmBXC2fRGU',    
    'voice_name': '',    
    'speed': '',
    'pitch': '',
    'is_active': False    
})
data['local_tts'].append({
    'token': 'AIzaSyDX37eTZHQALu9y7-smS6hPxhw6_k16b3c',
    'token_file': 'google.json',    
    'name': 'tts_gg_cloud',    
    'voice_name': 'vi-VN-Wavenet-B',
    'profile': 'telephony-class-application',      
    'speed': 1.0,
    'pitch': 0,
    'is_active': True    
})
data['local_tts'].append({
    'token': 'SythBY7N8AUnddbzfUk15aBx45uFDAebU7twsjBFqq-jxLrWpxlyXxzdWRNwYE8N',
    'token_file': '',    
    'name': 'tts_viettel',    
    'voice_name': 'hcm-diemmy2',
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})
data['local_tts'].append({
    'token': '8sJJ39o7qhfS00FoRUUSIlkmBXC2fRGU',
    'token_file': '',    
    'name': 'tts_zalo',
    'voice_name': '1',    
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})    
data['local_tts'].append({
    'token': '9onFCDijHuv61LM4qBZpqWo4A2qzjjDU',
    'name': 'tts_fpt',
    'voice_name': 'ngoclam',
    'speed': 1.0,
    'pitch': '',    
    'is_active': False    
})

data['playback_time'] = []
data['playback_time'].append({
    'playback_time': 30,    
})

data['internet_timeout'] = []
data['internet_timeout'].append({
    'internet_timeout': 5,    
})

data['check_url'] = []
data['check_url'].append({
    'check_url': 'http://www.google.com',
})
data['server'] = []
data['server'].append({
    'server_url': 'http://vietbot.xyz:5000/api',
    'api_type': 'REST',
    'is_active': True        
})
data['server'].append({
    'server_url': 'ws://vietbot.xyz:7000',
    'api_type': 'WS',
    'is_active': False        
})
data['server'].append({
    'server_url': 'grpc://vietbot.xyz:9000',
    'api_type': 'gRPC',
    'is_active': False        
})

data['button_data'] = []
data['button_data'].append({
    'gpio_address': 24,
    'type': 'touch',
    'pulse': True,    
    'function': 'volume_down',
    'is_active': False    
})
data['button_data'].append({
    'gpio_address': 25,
    'type': 'touch',
    'pulse': True,    
    'function': 'volume_up',
    'is_active': False    
})
data['button_data'].append({
    'gpio_address': 22,
    'type': 'touch',    
    'pulse': True,    
    'function': 'toggle_mic',
    'is_active': False    
})
data['button_data'].append({
    'gpio_address': 26,
    'type': 'touch',    
    'pulse': True,    
    'function': 'direct_command',
    'is_active': False    
})


data['smh_skill'] = []
data['smh_skill'].append({
    'smh_name': 'hass',
    'smh_url':'https://tieppm.duckdns.org:8123',
    'smh_token1': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiI2M2I3MGY5NDY5MGE0ODcyOTQ1YTI0NTc0MjFmM2Y2NCIsImlhdCI6MTY0NjIxMjM5OCwiZXhwIjoxOTYxNTcyMzk4fQ.CG1Qz1ApG5bvNT_gD-cyO0XlKZ-4Th_U4jAHql_RNEQ',
    # 'smh_url':'https://hc-21e793e50963b09c0da61a7168ab92f9.vpn1.vccsmart.vn',
    # 'smh_token1':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJkNzY3Y2MxMWQ0MGU0MmE0YTNiMjFkMDljNzIwMTc4MiIsImlhdCI6MTYxMjc0OTA2MiwiZXhwIjoxOTI4MTA5MDYyfQ.2zH2F0iExR7KHHsQf-7amCuZ3ty_-YHsSImJlE3Twjc',
    # 'smh_url':'https://hoangtruong.duckdns.org:8123',
    # 'smh_token1':'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjYmVlMGU5ODk1NDE0NzdlOWIxOWJmOTBkMzFjNzllMiIsImlhdCI6MTY0MjEzNTAwMSwiZXhwIjoxOTU3NDk1MDAxfQ.yFJja3NTZpXjjmcZF8Yw9mEjGTqZEyHEyvmUlvC68VM',
    'smh_token2':'',
    'smh_token3':'',
    'is_active': True        
})


data['smh_skill'].append({
    'smh_name': 'vcchome',
    'smh_url':'',
    'smh_token1': '8ed3ac06-a17b-4aea-b654-e4591ebc5a0e',
    'smh_token2': 'F27F4F2FA85F9C52A9F1ED5EF1EC8',
    'smh_token3': 'eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJxdWFuZ2h1bmdwcjg2QGdtYWlsLmNvbSIsImV4cCI6MTYyMjM2MTMyMSwiaWF0IjoxNjIyMjc0OTIxfQ.gtWei3MlHbgF0Jpq6rM2eHALWtRiJyutsJhF1wpNEwJtrn4Cq_JNoREuKutcpbe4vsYW0AZLLaubWfvMFTf28g',
    'is_active': False        
})

data['location'] = []
data['location'].append({
    'long': 105.804817,
    'lat': 21.028511,
    'is_active': True    
})
data['tts_speaker'] = []
data['tts_speaker'].append({
    'is_active': True
})

with open('config.json', 'w') as outfile:
    json.dump(data, outfile)