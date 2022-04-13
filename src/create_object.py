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
    'value': 'thời sự'
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
obj['compare_percent'] = []
obj['compare_percent'].append({
    'music_compare': 80,
    'smarthome_compare': 80
})

with open('object.json', 'w') as outfile:
    json.dump(obj, outfile)