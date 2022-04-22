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
obj['yesterday'] = []
obj['yesterday'].append({
    'value': 'hôm qua'
})
obj['today'] = []
obj['today'].append({
    'value': 'hôm nay'
})
obj['today'].append({
    'value': 'ngày này'
})
obj['tomorrow'] = []
obj['tomorrow'].append({
    'value': 'ngày mai'
})
obj['next_day'] = []
obj['next_day'].append({
    'value': 'ngày kia'
})
obj['next_day'].append({
    'value': 'ngày mốt'
})
obj['next_week'] = []
obj['next_week'].append({
    'value': 'tuần tới'
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
obj['location'] = []
obj['location'].append({
    'value': 'địa điểm'
})
obj['location'].append({
    'value': 'khu vực'
})
obj['location'].append({
    'value': 'ở'
})
obj['location'].append({
    'value': 'tại'
})
obj['event'] = []
obj['event'].append({
    'value': 'sự kiện'
})
obj['anniversary'] = []
obj['anniversary'].append({
    'value': 'kỉ niệm'
})
obj['anniversary'].append({
    'value': 'ngày giỗ'
})
obj['anniversary_data'] = []
obj['anniversary_data'].append({
    'name':'ngày cưới',
    'day': '10',
    'month': '04',
    'is_lunar_calendar': False
})
obj['anniversary_data'].append({
    'name':'hội Bình Đà',
    'day': '01',
    'month': '03',
    'is_lunar_calendar': True
})
obj['anniversary_data'].append({
    'name':'sinh nhật Beo',
    'day': '11',
    'month': '12',
    'is_lunar_calendar': False
})
obj['lunar_day'] = []
obj['lunar_day'].append({
    'value': 'ngày âm'
})
obj['lunar_day'].append({
    'value': 'lịch âm'
})
obj['lunar_day'].append({
    'value': 'mùng mấy'
})
obj['lunar_day'].append({
    'value': 'mồng mấy'
})
obj['lunar_day'].append({
    'value': 'âm lịch'
})
obj['history'] = []
obj['history'].append({
    'value': 'lịch sử'
})
obj['history'].append({
    'value': 'năm xưa'
})
obj['event'] = []
obj['event'].append({
    'value': 'sự kiện'
})
obj['name_is'] = []
obj['name_is'].append({
    'value': 'tên là'
})
obj['name_is'].append({
    'value': 'có tên'
})
obj['name_is'].append({
    'value': 'với tên'
})
obj['end_of_request'] = []
obj['end_of_request'].append({
    'value': 'nhé'    
})
obj['end_of_request'].append({
    'value': 'ngay'    
})
obj['end_of_request'].append({
    'value': 'em nhé'    
})
obj['end_of_request'].append({
    'value': 'ngay nhé'    
})
obj['end_of_request'].append({
    'value': 'ngay nào'    
})
obj['end_of_request'].append({
    'value': 'cho anh'    
})
obj['end_of_request'].append({
    'value': 'cho anh nhé'    
})
obj['end_of_request'].append({
    'value': 'được không'    
})
obj['location_data'] = []

obj['location_data'].append({
    "name": "Ninh Bình",
    "coord": {
        "lon": 105.833328,
        "lat": 20.25
    }
})
obj['location_data'].append({
    "name": "Hà Nội",
    "coord": {
        "lon": 105.883331,
        "lat": 21.116671
    }
})
obj['location_data'].append({
    "name": "Thủ Đô",
    "coord": {
        "lon": 105.841171,
        "lat": 21.0245
    }
})
obj['compare_percent'] = []
obj['compare_percent'].append({
    'music_compare': 80,
    'smarthome_compare': 80
})

with open('object.json', 'w') as outfile:
    json.dump(obj, outfile)
