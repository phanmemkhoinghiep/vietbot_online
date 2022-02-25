import json

data = {}
data['mic'] = []
data['mic'].append({
    'type': 'None Respeaker Mic',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': True           
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
    'led_off_color': 0xFFFF99,
    'led_wakeup_mode': 2,
    'led_wakeup_color': 0x33FFFF,    
    'is_active': False        
})
data['mic'].append({
    'type': 'ReSpeaker Core v2.0',
    'led_off_mode': '',
    'led_off_color': '',
    'led_think_mode': '',    
    'led_thing_color': '',            
    'is_active': False        
})
data['volume'] = []
data['volume'].append({
    'value': 75,
    'type': 'event'    
})
data['volume'].append({
    'value': 75,
    'type': 'speak'    
})
data['volume'].append({
    'value': 75,
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
    'porcupine_access_key': 'EhpBuTJẻwrwerwer4IwUtAONg=='
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
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'vi-oh-vi_en_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'vi-o-vi_en_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'alexa_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'americano_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'blueberry_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'bumblebee_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'computer_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'grapefruit_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'grasshopper_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey barista_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey google_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'hey siri_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'jarvis_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True   
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'ok google_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'pico clock_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'picovoice_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'porcupine_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['hotword'].append({
    'type': 'porcupine',
    'file_name': 'terminator_raspberry-pi.ppn',    
    'sensitive': 0.6,        
    'is_active': True    
})
data['continuous_asking'] = []
data['continuous_asking'].append({
    'content': 'hỏi liên tục',
    'is_active': False
})
data['stt_engine'] = []
data['stt_engine'].append({
    'name': 'stt_gg_free',
    'time_out': 6000,
    'is_active': False    
})
data['stt_engine'].append({
    'name': 'stt_gg_cloud',
    'token_file': 'google.json',    
    'time_out': 6000,
    'is_active': True    
})
data['stt_engine'].append({
    'name': 'stt_gg_ass',
    'token': '',
    'token_file': '',    
    'time_out': 6000,
    'is_active': False    
})
data['stt_engine'].append({
    'name': 'stt_viettel',
    'token': 'SythBY7N8AUsdfsdfdsfpxlyXxzdWRNwYE8N',
    'time_out': 4000,
    'is_active': False    
})
data['stt_engine'].append({
    'name': 'stt_fpt',
    'token': '',
    'token_file': '',    
    'time_out': '',
    'is_active': False    
})
data['local_tts'] = []
data['local_tts'].append({
    'name': 'tts_gg_free',
    'token': '8sJJsdfsdfsdfBXC2fRGU',    
    'voice_name': '',    
    'speed': '',
    'pitch': '',
    'is_active': False    
})
data['local_tts'].append({
    'token': 'AIzaSysdfsdfsdfk16b3c',
    'token_file': 'google.json',    
    'name': 'tts_gg_cloud',    
    'voice_name': 'vi-VN-Wavenet-A',
    'profile': 'telephony-class-application',      
    'speed': 1.0,
    'pitch': 0,
    'is_active': False    
})
data['local_tts'].append({
    'token': 'SythBY7NsfsdfsdfdWRNwYE8N',
    'token_file': '',    
    'name': 'tts_viettel',    
    'voice_name': 'hcm-diemmy2',
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})
data['local_tts'].append({
    'token': '8sJJ3sfsdfsdXC2fRGU',
    'token_file': '',    
    'name': 'tts_zalo',
    'voice_name': '1',    
    'speed': 1.0,
    'pitch': '',
    'is_active': False    
})    
data['local_tts'].append({
    'token': '9onFCsfsdfjjDU',
    'name': 'tts_fpt',
    'voice_name': 'ngoclam',
    'speed': 1.0,
    'pitch': '',    
    'is_active': False    
})
data['remote_tts'] = []
data['remote_tts'].append({
    'voice_engine': 'tts_fpt',
    'voice_name': 'ngoclam',
    'voice_speed': 1.0,
    'is_active': True    
})
data['remote_tts'].append({
    'voice_engine': 'tts_zalo',
    'voice_name': '1',
    'voice_speed': 1.0,
    'is_active': False    
})


data['time_playback'] = []
data['time_playback'].append({
    'time_playback': 60,    
    'is_active': True    
})

data['smh_skill'] = []
data['smh_skill'].append({
    'smh_name': 'hass',
    'smh_url':'https://abc.duckdns.org:8123',
    'smh_token1': 'sdfsdfdsf',
    'smh_token2':'',
    'smh_token3':'',
    'is_active': True        
})

data['smh_skill'].append({
    'smh_name': 'vcchome',
    'smh_url':'',
    'smh_token1': '8ed3ac0sdfsdfsdbc5a0e',
    'smh_token2': 'F27F4F2FA8sfdD5EF1EC8',
    'smh_token3': 'eyJhbGsfsdLWtRsfsdfbWfvMFTf28g',
    'is_active': False        
})


data['incrase_volume'] = []
data['incrase_volume'].append({
    'content': 'to lên',
    'is_active': True
})
data['incrase_volume'].append({
    'content': 'to thêm',
    'is_active': True
})
data['incrase_volume'].append({
    'content': 'tăng âm lượng',
    'is_active': True
})
data['decrase_volume'] = []
data['decrase_volume'].append({
    'content': 'bé xuống',
    'is_active': True
})
data['decrase_volume'].append({
    'content': 'bé đi',
    'is_active': True
})
data['decrase_volume'].append({
    'content': 'giảm âm lượng',
    'is_active': True
})
data['pause'] = []
data['pause'].append({
    'content': 'tạm dừng',
    'is_active': True
})
data['continue'] = []
data['continue'].append({
    'content': 'tiếp tục',
    'is_active': True
})
data['reply'] = []
data['reply'].append({
    'content': 'phát lại',
    'is_active': True
})
data['reply'].append({
    'content': 'bật lại',
    'is_active': True
})
data['next'] = []
data['reply'].append({
    'content': 'kế tiếp',
    'is_active': True
})
data['reply'].append({
    'content': 'tiếp theo',
    'is_active': True
})
data['exit'] = []
data['exit'].append({
    'content': 'exit',
    'is_active': True
})
data['exit'].append({
    'content': 'thoát',
    'is_active': True
})
data['exit'].append({
    'content': 'stop',
    'is_active': True
})
with open('config.json', 'w') as outfile:
    json.dump(data, outfile)
