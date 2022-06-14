import json

config = {}
config['mic'] = []
config['mic'].append({
    'type': 'None Respeaker Mic',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False            
})
config['mic'].append({
    'type': 'ReSpeaker 2-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
config['mic'].append({
    'type': 'ReSpeaker 2-Mics Pi HAT with WS281x LED',
    'led_off_mode': 2,
    'led_off_color': 'fffcff',
    'led_wakeup_mode': 2,
    'led_wakeup_color': '128043',  
    'is_active': False        
})
config['mic'].append({
    'type': 'ReSpeaker 4-Mics Pi HAT',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
config['mic'].append({
    'type': 'ReSpeaker Mic Array v2.0',
    'led_off_mode': 1,
    'led_off_color': 'fffcff',
    'led_wakeup_mode': 2,
    'led_wakeup_color': '074a25',    
    'is_active': True        
})
config['volume'] = []
config['volume'].append({
    'value': 50,
    'type': 'event'    
})
config['volume'].append({
    'value': 50,
    'type': 'speak'    
})
config['volume'].append({
    'value': 50,
    'type': 'playback'    
})
config['hotword_engine'] = []
config['hotword_engine'].append({
    'name': 'snowboy',
    'is_active': False
})
config['hotword_engine'].append({
    'name': 'porcupine',
    'is_active': True,
    'porcupine_access_key': 'pJwv7qAadasdx2D3QecdasdOOWoDvm7JQ=='
})
config['hotword'] = []
config['hotword'].append({
    'type': 'snowboy',
    'file_name': 'snowboy.umdl',    
    'sensitive': 0.6,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'snowboy',
    'file_name': 'subex.umdl',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'vi-ci-ci_en_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'alexa_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'americano_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'blueberry_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'bumblebee_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'computer_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'grapefruit_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'grasshopper_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey barista_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey google_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': False   
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True   
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'jarvis_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True   
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'ok google_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': False    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'pico clock_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'picovoice_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'porcupine_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['hotword'].append({
    'type': 'porcupine',
    'file_name': 'terminator_raspberry-pi.ppn',    
    'sensitive': 0.4,        
    'is_active': True    
})
config['continuous_asking'] = []
config['continuous_asking'].append({
    'content': 'hỏi liên tục',
    'is_active': True
})
config['local_stt'] = []
config['local_stt'].append({
    'name': 'stt_gg_free',
    'time_out': 6000,
    'is_active': False    
})
config['local_stt'].append({
    'name': 'stt_gg_cloud',
    'token_file': 'google.json',    
    'time_out': 6000,
    'is_active': True    
})
config['local_stt'].append({
    'name': 'stt_gg_ass',
    'token': '',
    'token_file': '',    
    'time_out': 6000,
    'is_active': False    
})
config['local_stt'].append({
    'name': 'stt_viettel',
    'token': 'SythBY7N8AUndsdfsdfWpxlyXxzdWRNwYE8N',
    'time_out': 4000,
    'is_active': False    
})
config['local_stt'].append({
    'name': 'stt_fpt',
    'token': '',
    'token_file': '',    
    'time_out': '',
    'is_active': False    
})
config['local_tts'] = []
config['local_tts'].append({
    'name': 'tts_gg_free',
    'token': '8sJJ39sdfsdfSIlkmBXC2fRGU',    
    'voice_name': '',    
    'speed': '',
    'pitch': '',
    're_use': True,
    'is_active': False    
})
config['local_tts'].append({
    'token': 'AIzaSyDsdfsdf_k16b3c',
    'token_file': 'google.json',    
    'name': 'tts_gg_cloud',    
    'voice_name': 'vi-VN-Wavenet-B',
    'profile': 'telephony-class-application',      
    'speed': 1.0,
    'pitch': 0,
    're_use': True,
    'is_active': False    
})
config['local_tts'].append({
    'token': 'dfgdfgdfgARWDFSc',
    'name': 'tts_gg_cloud_free',    
    'voice_name': 'vi-VN-Wavenet-B',
    'profile': 'telephony-class-application',      
    'speed': 1.0,
    'pitch': 0,
    're_use': True,
    'is_active': False   
})
config['local_tts'].append({
    'token': 'SythBY7N8AUsfsdfq-jxLrWsdfsdRNwYE8N',
    'token_file': '',    
    'name': 'tts_viettel',    
    'voice_name': 'hcm-diemmy2',
    'speed': 1.0,
    'pitch': '',
    're_use': True,
    'is_active': False    
})
config['local_tts'].append({
    'token': '8sJJsdfsdffRGU',
    'token_file': '',    
    'name': 'tts_zalo',
    'voice_name': '1',    
    'speed': 1.0,
    'pitch': '',
    're_use': True,
    'is_active': False    
})    
config['local_tts'].append({
    'token': '9onFsfsdfqzjjDU',
    'name': 'tts_fpt',
    'voice_name': 'ngoclam',
    'speed': 1.0,
    'pitch': '',    
    're_use': True,
    'is_active': False   
})

config['playback_time'] = []
config['playback_time'].append({
    'playback_time': 30,    
})

config['internet_timeout'] = []
config['internet_timeout'].append({
    'internet_timeout': 5,    
})

config['check_url'] = []
config['check_url'].append({
    'check_url': 'http://www.google.com',
})
config['server'] = []
config['server'].append({
    'server_url': 'http://vietbot.xyz:5000/api',
    'api_type': 'REST',
    'is_active': True        
})
config['server'].append({
    'server_url': 'ws://vietbot.xyz:7000',
    'api_type': 'WS',
    'is_active': False        
})
config['server'].append({
    'server_url': 'grpc://vietbot.xyz:9000',
    'api_type': 'gRPC',
    'is_active': False        
})

config['button_config'] = []
config['button_config'].append({
    'gpio_address': 24,
    'type': 'touch',
    'pulse': True,    
    'function': 'volume_down',
    'is_active': False    
})
config['button_config'].append({
    'gpio_address': 25,
    'type': 'touch',
    'pulse': True,    
    'function': 'volume_up',
    'is_active': False    
})
config['button_config'].append({
    'gpio_address': 22,
    'type': 'touch',    
    'pulse': True,    
    'function': 'toggle_mic',
    'is_active': False    
})
config['button_config'].append({
    'gpio_address': 26,
    'type': 'touch',    
    'pulse': True,    
    'function': 'direct_command',
    'is_active': False    
})
config['smh_skill'] = []
config['smh_skill'].append({
    'smh_name': 'hass',
    'smh_url':'https://dasdasd.duckdns.org:8123',
    'smh_token1': 'eyJ0eXAiOiJKVsfddfxOTYxNTcyMzk4fQ.CG1Qz1ApsdfsdfU4jAHql_RNEQ',
    'smh_token2':'',
    'smh_token3':'',
    'is_active': True        
})
config['location'] = []
config['location'].append({
    'long': 105.804817,
    'lat': 21.028511,
    'is_active': True    
})
config['tts_speaker'] = []
config['tts_speaker'].append({
    'is_active': True
})
config['hanet'] = []
config['hanet'].append({
    'agent_annoucement': 'Phát hiện người nhà hoặc nhân viên tên là',    
    'partner_annoucement': 'Phát hiện khách hoặc nhân viên tên là',    
    'stranger_annoucement': 'Phát hiện người lạ hoặc không nhận diện đủ gương mặt',    
    'is_active': False
})
with open('config.json', 'w') as outfile:
    json.dump(config, outfile)
