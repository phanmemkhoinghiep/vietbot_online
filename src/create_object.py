import json

obj = {}

obj['moment'] = []
obj['moment'].append({
    'value': 'bây giờ'
})
obj['moment'].append({
    'value': 'lúc này'
})
obj['moment'].append({
    'value': 'hiện tại'
})
obj['time_now'] = []
obj['time_now'].append({
    'value': 'mấy giờ'
})
obj['today'] = []
obj['today'].append({
    'value': 'hôm nay'
})
obj['this_month'] = []
obj['this_month'].append({
    'value': 'tháng này'
})
obj['this_year'] = []
obj['this_year'].append({
    'value': 'năm'
})
obj['weather'] = []
obj['weather'].append({
    'value': 'thời tiết'
})
obj['news'] = []
obj['news'].append({
    'value': 'tin tức'
})
obj['news'].append({
    'value': 'báo'
})
obj['news'].append({
    'value': 'thời sự'
})
obj['news_data'] = []
obj['news_data'].append({       
    'name': 'lao động',
    'link': 'https://laodong.vn/rss/home.rss'    
})
obj['news_data'].append({       
    'name': 'việt nam net',
    'link': 'https://vietnamnet.vn/rss/thoi-su-chinh-tri.rss'    
})
obj['news_data'].append({       
    'name': 'thanh niên',
    'link': 'https://thanhnien.vn/rss/home.rss'    
})
obj['music'] = []
obj['music'].append({
    'value': 'nhạc'
})
obj['music'].append({
    'value': 'bài'
})
obj['network_speed'] = []
obj['network_speed'].append({
    'value': 'đường truyền'
})
obj['network_speed'].append({
    'value': 'tốc độ mạng'
})

obj['all'] = []
obj['all'].append({
    'value': 'tất cả'
})
obj['all'].append({
    'value': 'hết cả'
})
obj['all'].append({
    'value': 'toàn bộ'
})
obj['single'] = []
obj['single'].append({
    'value': 'duy nhất'
})
obj['single'].append({
    'value': 'chỉ một'
})
obj['single'].append({
    'value': 'riêng mỗi'
})
obj['single'].append({
    'value': 'duy mỗi'
})
obj['single'].append({
    'value': 'mỗi một'
})
obj['single'].append({
    'value': 'duy nhất'
})
obj['light'] = []
obj['light'].append({
    'value': 'đèn'
})
obj['light'].append({
    'value': 'bóng điện'
})
obj['light'].append({
    'value': 'đèn điện'
})
obj['switch'] = []
obj['switch'].append({
    'value': 'công tắc'
})
obj['socket'] = []
obj['socket'].append({
    'value': 'ổ cắm'
})
obj['socket'].append({
    'value': 'ổ điện'
})
obj['fan'] = []
obj['fan'].append({
    'value': 'quạt'
})
obj['door'] = []
obj['door'].append({
    'value': 'cửa'
})    
obj['door'].append({
    'value': 'cổng'
})
obj['occupancy'] = []
obj['occupancy'].append({
    'value': 'pir'
})
obj['occupancy'].append({
    'value': 'chuyển động'
})
obj['curtain'] = []
obj['curtain'].append({
    'value': 'rèm'
})
obj['curtain'].append({
    'value': 'mành'
})
obj['curtain'].append({
    'value': 'màn'
})
obj['cover'] = []
obj['cover'].append({
    'value': 'cửa cuốn'    
})
obj['gate'] = []
obj['gate'].append({
    'value': 'cổng'    
})
obj['temperature'] = []
obj['temperature'].append({
    'value': 'nhiệt độ'    
})
obj['humidity'] = []
obj['humidity'].append({
    'value': 'độ ẩm'    
})
obj['script'] = []
obj['script'].append({
    'value': 'kịch bản'    
})
obj['automation'] = []
obj['automation'].append({
    'value': 'tự động'    
})
obj['unit'] = []
obj['unit'].append({
    'code': 'clients',    
    'name': 'kết nối'    
})
obj['unit'].append({
    'code': '%',    
    'name': 'phần trăm'    
})
obj['unit'].append({
    'code': 'MiB',    
    'name': 'mê bai'    
})
obj['unit'].append({
    'code': '°C',    
    'name': 'độ xê'    
})
obj['unit'].append({
    'code': 'min',    
    'name': 'phút'    
})
obj['unit'].append({
    'code': 's',    
    'name': 'giây'    
})
obj['unit'].append({
    'code': 'km/h',    
    'name': 'ki lô mét trên giờ'    
})
obj['unit'].append({
    'code': 'Hz',    
    'name': 'héc'    
})
obj['unit'].append({
    'code': 'V',    
    'name': 'vôn'    
})
obj['unit'].append({
    'code': 'A',    
    'name': 'am pe'    
})
obj['unit'].append({
    'code': 'kW',    
    'name': 'ki lô oát'    
})
obj['unit'].append({
    'code': 'Wh',    
    'name': 'oát giờ'    
})
obj['unit'].append({
    'code': 'kWh',    
    'name': 'kilo oát giờ'    
})
obj['unit'].append({
    'code': 'L',    
    'name': 'lít'    
})
obj['state'] = []
obj['state'].append({
    'value': 'trạng thái'
})
obj['state'].append({
    'value': 'thông số'
})
obj['radio'] = []
obj['radio'].append({
    'value': 'radio'
})
obj['radio'].append({
    'value': 'phát thanh'
})
obj['radio'].append({
    'value': 'đài'
})
obj['radio_data'] = []
obj['radio_data'].append({
    'name': 'vov1',
    'link': 'https://str.vov.gov.vn/vovlive/vov1vov5Vietnamese.sdp_aac/playlist.m3u8'        
})
obj['radio_data'].append({
    'name': 'vov2',
    'link': 'https://str.vov.gov.vn/vovlive/vov2.sdp_aac/playlist.m3u8'            
})
obj['radio_data'].append({
    'name': 'vov3',
    'link': 'https://str.vov.gov.vn/vovlive/vov3.sdp_aac/playlist.m3u8'   
})
obj['radio_data'].append({
    'name': 'vov giao thông hà nội',
    'link': 'https://str.vov.gov.vn/vovlive/vovGTHN.sdp_aac/playlist.m3u8'   
})
obj['radio_data'].append({
    'name': 'vov giao thông sài gòn',
    'link': 'https://str.vov.gov.vn/vovlive/vovGTHCM.sdp_aac/playlist.m3u8'    
})
obj['vov_hcm'] = []
obj['vov_hcm'].append({
    'value': 'vov giao thông sài gòn'
})
obj['compare_percent'] = []
obj['compare_percent'].append({
    'music_compare': 80,
    'smarthome_compare': 80
})

with open('object.json', 'w') as outfile:
    json.dump(obj, outfile)