#All
import json
#Lunar, Noted day Skill
import datetime
import math
#Youtube Skill
from urllib.request import urlretrieve
import requests
import urllib
import re
import pafy
#History Skill
import bs4
#Weather Skill
#Music
import os
#Youtube
from fuzzywuzzy import fuzz   
import pafy
#Speed Test
import speedtest
#News
import feedparser
#Random
import random
from urllib.request import urlretrieve
with open('object.json') as object_json:
    obj_data = json.load(object_json)
with open('config.json') as config_json:
    config_data = json.load(config_json)
obj_yesterday=[]
for p in obj_data['yesterday']:
    obj_yesterday.append(p['value'])                             
obj_today=[]
for p in obj_data['today']:    
    obj_today.append(p['value'])                                            
obj_tomorrow=[]
for p in obj_data['tomorrow']:
    obj_tomorrow.append(p['value'])                             
obj_next_day=[]
for p in obj_data['next_day']:    
    obj_next_day.append(p['value'])                                            
obj_this_week=[]
for p in obj_data['this_week']:    
    obj_this_week.append(p['value'])                                            
obj_next_week=[]
for p in obj_data['next_week']:
    obj_next_week.append(p['value'])                             
obj_this_month=[]
for p in obj_data['this_month']:    
    obj_this_month.append(p['value'])                                            
obj_next_month=[]
for p in obj_data['next_month']:    
    obj_next_month.append(p['value'])                                            
#All
# yesterday=(datetime.date.today() - datetime.timedelta(1)).day
# thistime=datetime.datetime.today().strftime('%H:%M:%S')
# thisday=datetime.date.today().day
# tomorrow=(datetime.date.today() + datetime.timedelta(1)).day
# next_day=(datetime.date.today() + datetime.timedelta(2)).day
# month=datetime.date.today().month
# year=datetime.date.today().year
# yesterday_str=f"{(datetime.date.today() - datetime.timedelta(1)):%d}"
# thisday_str=f"{datetime.date.today():%d}"
# tomorrow_str=f"{(datetime.date.today() + datetime.timedelta(1)):%d}"
# next_day_str=f"{(datetime.date.today() + datetime.timedelta(2)):%d}"
# next_5day_str=f"{(datetime.date.today() + datetime.timedelta(5)):%d}"
# month_str=f"{datetime.date.today():%m}"
# year_str=f"{datetime.date.today():%y}"

#Get Time Skill
#News Skill
obj_news=[]
for p in obj_data['news']:    
    obj_news.append(p['value'])                                            
obj_news_name=[]
obj_news_link=[]
for p in obj_data['news_data']:    
    obj_news_name.append(p['name'])                                            
    obj_news_link.append(p['link'])                                            
#Radio Skill
obj_radio=[]
for p in obj_data['radio']:    
    obj_radio.append(p['value'])                                            
obj_radio_name=[]
obj_radio_link=[]
for p in obj_data['radio_data']:    
    obj_radio_name.append(p['name'])                                            
    obj_radio_link.append(p['link'])                                            
#Speed Test Skill 
obj_network_speed=[]
for p in obj_data['network_speed']:    
    obj_network_speed.append(p['value'])                                                
#Noted Day Skill
obj_event=[]
for p in obj_data['event']:
    obj_event.append(p['value'])                             
obj_anniversary=[]
for p in obj_data['anniversary']:
    obj_anniversary.append(p['value'])                             
obj_anniversary_name=[]
obj_anniversary_day=[]
obj_anniversary_month=[]
obj_anniversary_type=[]
for p in obj_data['anniversary_data']:
    obj_anniversary_name.append(p['name'])                             
    obj_anniversary_day.append(p['day'])                            
    obj_anniversary_month.append(p['month'])                            
    obj_anniversary_type.append(p['is_lunar_calendar'])                            
#Weather Skill
# obj_weather=[]
# for p in obj_data['weather']:
    # obj_weather.append(p['value'])                                        
BASE_URL = "https://api.openweathermap.org/data/2.5"
API_KEY = 'ffddba060ff1a735f04ff426f85f070b'
temp_delta=-273.15
#Music Skill
music_compare=100
for p in obj_data['compare_percent']:
    music_compare= p['music_compare']                             
song_path_list =os.listdir('mp3/')    

gpt_token=''
gpt_engine=''
for p in config_data['local_ext_bot']:
    if p['is_active'] and p['name'] == 'chatGPT':        
        import openai
    if p['is_active'] and p['name'] == 'gass':        
        import os.path
        import pathlib2 as pathlib
        import sys
        import logging
        # import click
        import google.auth.transport.grpc
        import google.auth.transport.requests
        import google.oauth2.credentials
        import embedded_assistant_pb2
        import embedded_assistant_pb2_grpc
        from html2text import HTML2Text
        h = HTML2Text()
        try:
            from . import (
                assistant_helpers,
                browser_helpers,
            )
        except (SystemError, ImportError):
            import assistant_helpers
            import browser_helpers
        ASSISTANT_HTML_FILE = 'google-assistant-sdk-screen-out.html'
        ASSISTANT_API_ENDPOINT = 'embeddedassistant.googleapis.com'
        DEFAULT_GRPC_DEADLINE = 60 * 3 + 5
        PLAYING = embedded_assistant_pb2.ScreenOutConfig.PLAYING
        class SampleTextAssistant(object):
            """Sample Assistant that supports text based conversations.
            Args:
              language_code: language for the conversation.
              device_model_id: identifier of the device model.
              device_id: identifier of the registered device instance.
              display: enable visual display of assistant response.
              channel: authorized gRPC channel for connection to the
                Google Assistant API.
              deadline_sec: gRPC deadline in seconds for Google Assistant API call.
            """
            def __init__(self, language_code, device_model_id, device_id,
                         display, channel, deadline_sec):
                self.language_code = language_code
                self.device_model_id = device_model_id
                self.device_id = device_id
                self.conversation_state = None
                # Force reset of first conversation.
                self.is_new_conversation = True
                self.display = display
                self.assistant = embedded_assistant_pb2_grpc.EmbeddedAssistantStub(
                    channel
                )
                self.deadline = deadline_sec

            def __enter__(self):
                return self

            def __exit__(self, etype, e, traceback):
                if e:
                    return False

            def assist(self, text_query):
                """Send a text request to the Assistant and playback the response.
                """
                def iter_assist_requests():
                    config = embedded_assistant_pb2.AssistConfig(
                        audio_out_config=embedded_assistant_pb2.AudioOutConfig(
                            encoding='LINEAR16',
                            sample_rate_hertz=16000,
                            volume_percentage=0,
                        ),
                        dialog_state_in=embedded_assistant_pb2.DialogStateIn(
                            language_code=self.language_code,
                            conversation_state=self.conversation_state,
                            is_new_conversation=self.is_new_conversation,
                        ),
                        device_config=embedded_assistant_pb2.DeviceConfig(
                            device_id=self.device_id,
                            device_model_id=self.device_model_id,
                        ),
                        text_query=text_query,
                    )
                    # Continue current conversation with later requests.
                    self.is_new_conversation = False
                    if self.display:
                        config.screen_out_config.screen_mode = PLAYING
                    req = embedded_assistant_pb2.AssistRequest(config=config)
                    assistant_helpers.log_assist_request_without_audio(req)
                    yield req

                text_response = None
                html_response = None
                for resp in self.assistant.Assist(iter_assist_requests(),
                                                  self.deadline):
                    assistant_helpers.log_assist_response_without_audio(resp)
                    if resp.screen_out.data:
                        html_response = resp.screen_out.data
                    if resp.dialog_state_out.conversation_state:
                        conversation_state = resp.dialog_state_out.conversation_state
                        self.conversation_state = conversation_state
                    if resp.dialog_state_out.supplemental_display_text:
                        text_response = resp.dialog_state_out.supplemental_display_text
                return text_response, html_response
def jdFromDate(dd, mm, yy):
  '''def jdFromDate(dd, mm, yy): Compute the (integral) Julian day number of day dd/mm/yyyy, i.e., the number of days between 1/1/4713 BC (Julian calendar) and dd/mm/yyyy.'''
  a = int((14 - mm) / 12.)
  y = yy + 4800 - a
  m = mm + 12*a - 3
  jd = dd + int((153*m + 2) / 5.) \
        + 365*y + int(y/4.) - int(y/100.) \
        + int(y/400.) - 32045
  if (jd < 2299161):
    jd = dd + int((153*m + 2)/5.) \
          + 365*y + int(y/4.) - 32083
  return jd
def jdToDate(jd):
  '''def jdToDate(jd): Convert a Julian day number to day/month/year. jd is an integer.'''
  if (jd > 2299160):
    ## After 5/10/1582, Gregorian calendar
    a = jd + 32044
    b = int((4*a + 3) / 146097.)
    c = a - int((b*146097) / 4.)
  else:
    b = 0
    c = jd + 32082
  d = int((4*c + 3) / 1461.)
  e = c - int((1461*d) / 4.)
  m = int((5*e + 2) / 153.)
  day = e - int((153*m + 2) / 5.) + 1
  month = m + 3 - 12*int(m / 10.)
  year = b*100 + d - 4800 + int(m / 10.)
  return [day, month, year]
def NewMoon(k):
  '''def NewMoon(k): Compute the time of the k-th new moon after the new moon of 1/1/1900 13:52 UCT (measured as the number of days since 1/1/4713 BC noon UCT, e.g., 2451545.125 is 1/1/2000 15:00 UTC. Returns a floating number, e.g., 2415079.9758617813 for k=2 or 2414961.935157746 for k=-2.'''
  ## Time in Julian centuries from 1900 January 0.5
  T = k / 1236.85
  T2 = T * T
  T3 = T2 * T
  dr = math.pi / 180.
  Jd1 = 2415020.75933 + 29.53058868*k \
          + 0.0001178*T2 - 0.000000155*T3
  Jd1 = Jd1 + 0.00033*math.sin( \
            (166.56 + 132.87*T - 0.009173*T2)*dr)
  ## Mean new moon
  M = 359.2242 + 29.10535608*k \
      - 0.0000333*T2 - 0.00000347*T3
  ## Sun's mean anomaly
  Mpr = 306.0253 + 385.81691806*k \
          + 0.0107306*T2 + 0.00001236*T3
  ## Moon's mean anomaly
  F = 21.2964 + 390.67050646*k - 0.0016528*T2 \
        - 0.00000239*T3
  ## Moon's argument of latitude
  C1 = (0.1734 - 0.000393*T)*math.sin(M*dr) \
        + 0.0021*math.sin(2*dr*M)
  C1 = C1 - 0.4068*math.sin(Mpr*dr) \
        + 0.0161*math.sin(dr*2*Mpr)
  C1 = C1 - 0.0004*math.sin(dr*3*Mpr)
  C1 = C1 + 0.0104*math.sin(dr*2*F) \
        - 0.0051*math.sin(dr*(M + Mpr))
  C1 = C1 - 0.0074*math.sin(dr*(M - Mpr)) \
        + 0.0004*math.sin(dr*(2*F + M))
  C1 = C1 - 0.0004*math.sin(dr*(2*F - M)) \
        - 0.0006*math.sin(dr*(2*F + Mpr))
  C1 = C1 + 0.0010*math.sin(dr*(2*F - Mpr)) \
        + 0.0005*math.sin(dr*(2*Mpr + M))
  if (T < -11):
    deltat= 0.001 + 0.000839*T + 0.0002261*T2 \
                - 0.00000845*T3 - 0.000000081*T*T3
  else:
    deltat= -0.000278 + 0.000265*T + 0.000262*T2
  JdNew = Jd1 + C1 - deltat
  return JdNew
def SunLongitude(jdn):
  '''def SunLongitude(jdn): Compute the longitude of the sun at any time. Parameter: floating number jdn, the number of days since 1/1/4713 BC noon.'''
  T = (jdn - 2451545.0 ) / 36525.
  ## Time in Julian centuries
  ## from 2000-01-01 12:00:00 GMT
  T2 = T * T
  dr = math.pi / 180.  ## degree to radian
  M = 357.52910 + 35999.05030*T \
      - 0.0001559*T2 - 0.00000048*T*T2
  ## mean anomaly, degree
  L0 = 280.46645 + 36000.76983*T + 0.0003032*T2
  ## mean longitude, degree
  DL = (1.914600 - 0.004817*T - 0.000014*T2) \
          * math.sin(dr*M)
  DL += (0.019993 - 0.000101*T) *math.sin(dr*2*M) \
            + 0.000290*math.sin(dr*3*M)
  L = L0 + DL  ## true longitude, degree
  L = L * dr
  L = L - math.pi*2*(int(L / (math.pi*2)))
  #### Normalize to (0, 2*math.pi)
  return L
def getSunLongitude(dayNumber, timeZone):
  '''def getSunLongitude(dayNumber, timeZone):  Compute sun position at midnight of the day with the given Julian day number. The time zone if the time difference between local time and UTC: 7.0 for UTC+7:00. The function returns a number between 0 and 11.  From the day after March equinox and the 1st major term after March equinox, 0 is returned. After that, return 1, 2, 3 ...'''
  return int( \
    SunLongitude(dayNumber - 0.5 - timeZone/24.) \
    / math.pi*6)
def getNewMoonDay(k, timeZone):
  '''def getNewMoonDay(k, timeZone): Compute the day of the k-th new moon in the given time zone. The time zone if the time difference between local time and UTC: 7.0 for UTC+7:00.'''
  return int(NewMoon(k) + 0.5 + timeZone / 24.)
def getLunarMonth11(yy, timeZone):
  '''def getLunarMonth11(yy, timeZone):  Find the day that starts the luner month 11of the given year for the given time zone.'''
  # off = jdFromDate(31, 12, yy) \
  #            - 2415021.076998695
  off = jdFromDate(31, 12, yy) - 2415021.
  k = int(off / 29.530588853)
  nm = getNewMoonDay(k, timeZone)
  sunLong = getSunLongitude(nm, timeZone)
  #### sun longitude at local midnight
  if (sunLong >= 9):
    nm = getNewMoonDay(k - 1, timeZone)
  return nm
def getLeapMonthOffset(a11, timeZone):
  '''def getLeapMonthOffset(a11, timeZone): Find the index of the leap month after the month starting on the day a11.'''
  k = int((a11 - 2415021.076998695) \
              / 29.530588853 + 0.5)
  last = 0
  i = 1  ## start with month following lunar month 11
  arc = getSunLongitude( \
                getNewMoonDay(k + i, timeZone), timeZone)
  while True:
    last = arc
    i += 1
    arc = getSunLongitude( \
                      getNewMoonDay(k + i, timeZone), \
                      timeZone)
    if  not (arc != last and i < 14):
      break
  return i - 1
def S2L(dd, mm, yy, timeZone = 7):
  '''def S2L(dd, mm, yy, timeZone = 7): Convert solar date dd/mm/yyyy to the corresponding lunar date.'''
  dayNumber = jdFromDate(dd, mm, yy)
  k = int((dayNumber - 2415021.076998695) \
                / 29.530588853)
  monthStart = getNewMoonDay(k + 1, timeZone)
  if (monthStart > dayNumber):
    monthStart = getNewMoonDay(k, timeZone)
  # alert(dayNumber + " -> " + monthStart)
  a11 = getLunarMonth11(yy, timeZone)
  b11 = a11
  if (a11 >= monthStart):
    lunarYear = yy
    a11 = getLunarMonth11(yy - 1, timeZone)
  else:
    lunarYear = yy + 1
    b11 = getLunarMonth11(yy + 1, timeZone)
  lunarDay = dayNumber - monthStart + 1
  diff = int((monthStart - a11) / 29.)
  lunarLeap = 0
  lunarMonth = diff + 11
  if (b11 - a11 > 365):
    leapMonthDiff = \
        getLeapMonthOffset(a11, timeZone)
    if (diff >= leapMonthDiff):
      lunarMonth = diff + 10
      if (diff == leapMonthDiff):
        lunarLeap = 1
  if (lunarMonth > 12):
    lunarMonth = lunarMonth - 12
  if (lunarMonth >= 11 and diff < 4):
    lunarYear -= 1
  return \
      [ lunarDay, lunarMonth, lunarYear, lunarLeap ]
def L2S(lunarD, lunarM, lunarY, lunarLeap, tZ = 7):
  '''def L2S(lunarD, lunarM, lunarY, lunarLeap, tZ = 7): Convert a lunar date to the corresponding solar date.'''
  if (lunarM < 11):
    a11 = getLunarMonth11(lunarY - 1, tZ)
    b11 = getLunarMonth11(lunarY, tZ)
  else:
    a11 = getLunarMonth11(lunarY, tZ)
    b11 = getLunarMonth11(lunarY + 1, tZ)
  k = int(0.5 + \
              (a11 - 2415021.076998695) / 29.530588853)
  off = lunarM - 11
  if (off < 0):
    off += 12
  if (b11 - a11 > 365):
    leapOff = getLeapMonthOffset(a11, tZ)
    leapM = leapOff - 2
    if (leapM < 0):
      leapM += 12
    if (lunarLeap != 0 and lunarM != leapM):
      return [0, 0, 0]
    elif (lunarLeap != 0 or off >= leapOff):
      off += 1
  monthStart = getNewMoonDay(k + off, tZ)
  return jdToDate(monthStart + lunarD - 1)
def get_lunar_day(dd):
    lunar_date = S2L(dd, datetime.date.today().month,datetime.date.today().year)
    ngay_am = str(lunar_date[0])
    list_thang = ["tháng Giêng","tháng Hai","tháng Ba","tháng Tư","tháng Năm","tháng Sáu","tháng Bảy","tháng Tám","tháng Chín","tháng Mười","tháng Mười một","tháng Chạp"]
    thang_am = int(str(lunar_date[1]))-1
    thang_am1 = list_thang[thang_am]
    can = ['Canh ', 'Tân ', 'Nhâm ', 'Quý ', 'Giáp ', 'Ất ', 'Bính ', 'Đinh ','Mậu ','Kỷ ']
    chi = ['Thân', 'Dậu', 'Tuất', 'Hợi','Tí','Sửu','Dần', 'Mão', 'Thìn', 'Tị', 'Ngọ', "Mùi"]
    nam = int(str(lunar_date[2]))
    vitri_can = nam % 10
    vitri_chi = nam % 12
    nam_am = str(lunar_date[2])
    # lunar_text2 = 'Ngày: ' + str(lunar_date[0]) + ' - ' + thang_am1  + ' năm '  + can[vitri_can] + chi[vitri_chi] + ' (' +  str(lunar_date[2]) +')'
    ss = int(ngay_am)
    nam_nhuan = int(str(lunar_date[3])) 
    thang_sau = thang_am + 1
    if thang_am <= 12:
        nam_a = nam_am 
    else:
        nam_a = nam_am + 1
        # ny = yy + 1
        a2d = L2S(28,12,datetime.date.today().year,nam_nhuan)
        nd = a2d[0]
        td = a2d[1]
        nmd = a2d[2]
        daa = str(nd)+'-'+str(td)+'-'+str(nmd)
        a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
        ngaytet = a2dnew.day
        thangtet = a2dnew.month
        namtet = a2dnew.year
        nammoi = S2L(ngaytet,thangtet,namtet)
        nam_nhuan = int(str(nammoi[3]))
    next = L2S(1,thang_sau,int(nam_a), nam_nhuan)
    nd = next[0]
    td = next[1]
    nmd = next[2]
    daa = str(nd)+'-'+str(td)+'-'+str(nmd)
    a2dnew = datetime.datetime.strptime(daa, '%d-%m-%Y')
    delta = a2dnew - datetime.datetime.today()
    days_left = delta.days
    thang_am = list_thang[thang_am]
    ngay_am =str(lunar_date[0])
    if ss == 15:
        return ngay_am,thang_am,nam_am,'là rằm '+ ngay_am +' '+ thang_am1 + 'năm ' + can[vitri_can] +' '+ chi[vitri_chi]+' ' + nam_am
    elif ss == 1:
        return ngay_am,thang_am,nam_am,'là mùng một '+ ngay_am +' '+ thang_am1 + 'năm ' + can[vitri_can] +' '+ chi[vitri_chi]+ ' ' + nam_am
    elif ss>1 and ss<15:
        days_left = 15 - ss
        if ss <11:
            return ngay_am,thang_am,nam_am,'là mùng ' + ngay_am +' '+ thang_am1 + ' năm ' + can[vitri_can] +' '+ chi[vitri_chi] +' '+ nam_am + ". Còn " + str(days_left) + " ngày nữa là đến rằm"
        else: 
            return ngay_am,thang_am,nam_am,'là '+ ngay_am +' '+ thang_am1 + ' năm ' + can[vitri_can] +' '+ chi[vitri_chi] +' '+ nam_am + ". Còn " + str(days_left) + " ngày nữa là đến rằm"
    elif ss>15 and ss<31:
        return ngay_am,thang_am,nam_am,'là ' + ngay_am +' '+ thang_am + ' năm ' + str(can[vitri_can])+' ' + str(chi[vitri_chi])+ ' ' + str(nam_am)
    else:
        return ngay_am,thang_am,nam_am,'là ' + str(ngay_am)+' ' + str(thang_am) + ' năm ' + str(can[vitri_can])+' ' + str(chi[vitri_chi])+ ' ' + str(nam_am)
def lunar_calendar_process(data):
    if any(item in data for item in obj_yesterday):
        return 'hôm qua '+ get_lunar_day((datetime.date.today() - datetime.timedelta(1)).day)[3]
    elif any(item in data for item in obj_today):
        return 'hôm nay '+ get_lunar_day(datetime.date.today().day)[3]
    elif any(item in data for item in obj_tomorrow):
        return 'ngày mai '+ get_lunar_day((datetime.date.today() + datetime.timedelta(1)).day)[3]
    elif any(item in data for item in obj_next_day):
        return 'ngày kia '+ get_lunar_day((datetime.date.today() + datetime.timedelta(2)).day)[3]
    else:
        return 'Yêu cầu tra cứu lịch âm cần ngày cụ thể là một trong các ngày '+ random.choice(obj_yesterday)+ ' '+random.choice(obj_today)+ ' '+random.choice(obj_tomorrow)+ ' '+random.choice(obj_next_day)
def anniversary_process(data):
    lunar_yesterday = str(get_lunar_day((datetime.date.today() - datetime.timedelta(1)).day)[0])
    lunar_today=str(get_lunar_day(datetime.date.today().day)[0])
    lunar_tomorrow=str(get_lunar_day((datetime.date.today() + datetime.timedelta(1)).day)[0])
    lunar_next_day=str(get_lunar_day((datetime.date.today() + datetime.timedelta(2)).day)[0])
    lunar_month=str(get_lunar_day(datetime.date.today().day)[1])    
    index=None
    lunar_index=None
    day_type=''
    if any(item in data for item in obj_yesterday):
        day_type='Hôm qua'
        for i in range(len(obj_anniversary_day)):
            if obj_anniversary_type[i]:
                if obj_anniversary_day[i]==lunar_yesterday and obj_anniversary_month[i] ==lunar_month:
                    lunar_index =i
                    break
        for i in range(len(obj_anniversary_day)):
            if obj_anniversary_type[i]==False:
                if obj_anniversary_day[i]==f"{(datetime.date.today() - datetime.timedelta(1)):%d}" and obj_anniversary_month[i] ==f"{datetime.date.today():%m}":
                    index =i
                    break
    elif any(item in data for item in obj_today):
        day_type='Hôm nay'
        for i in range(len(obj_anniversary_day)):
            if obj_anniversary_type[i]:
                if obj_anniversary_day[i]==lunar_today and obj_anniversary_month[i] ==lunar_month:
                    lunar_index =i
                    break
        for i in range(len(obj_anniversary_day)):
            if obj_anniversary_type[i]==False:
                if obj_anniversary_day[i]==f"{datetime.date.today():%d}" and obj_anniversary_month[i] ==f"{datetime.date.today():%m}":
                    index=i
                    break
    elif any(item in data for item in obj_tomorrow):
        day_type='Ngày mai'
        for i in range(len(obj_anniversary_day)):
            if obj_anniversary_type[i]:
                if obj_anniversary_day[i]==lunar_tomorrow and obj_anniversary_month[i] ==lunar_month:
                    lunar_index =i
                    break
        for i in range(len(obj_anniversary_day)):
            if obj_anniversary_type[i]==False:
                if obj_anniversary_day[i]==f"{(datetime.date.today() + datetime.timedelta(1)):%d}" and obj_anniversary_month[i] ==f"{datetime.date.today():%m}":
                    index =i
                    break
    elif any(item in data for item in obj_next_day):
        day_type='Ngày kia'
        for i in range(len(obj_anniversary_day)):
            if obj_anniversary_type[i]:
                if obj_anniversary_day[i]==lunar_next_day and obj_anniversary_month[i] ==lunar_month:
                    lunar_index =i                               
                    break
        for i in range(len(obj_anniversary_day)):
            if obj_anniversary_type[i]==False:
                if obj_anniversary_day[i]==f"{(datetime.date.today() + datetime.timedelta(2)):%d}" and obj_anniversary_month[i] ==f"{datetime.date.today():%m}":
                    index =i    
                    break
    if index is None and lunar_index is None:
        return day_type+ ' không trùng với ngày lễ ngày kỉ niệm hoặc sự kiện gì'
    elif index is None and lunar_index is not None:
        return day_type+ ' là '+ obj_anniversary_name[lunar_index]
    elif index is not None and lunar_index is None:
        return day_type+ 'là '+ obj_anniversary_name[index]
    elif index is not None and lunar_index is not None:
        return day_type+ ' dương lịch là '+obj_anniversary_name[index] +' âm lịch là '+obj_anniversary_name[lunar_index]
def history_process(data):
    url = "https://lichngaytot.com/ajax/NgayNayNamXuaAjax"
    headers = {'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8'}
    if any(item in data for item in obj_yesterday):
        payload = {'ngayxem': f"{(datetime.date.today() - datetime.timedelta(1)):%d}"+'-'+f"{datetime.date.today():%m}"+'-'+f"{datetime.date.today():%y}"}
    elif any(item in data for item in obj_today):
        payload = {'ngayxem': f"{datetime.date.today():%d}"+'-'+f"{datetime.date.today():%m}"+'-'+f"{datetime.date.today():%y}"}
    elif any(item in data for item in obj_tomorrow):
        payload = {'ngayxem': f"{(datetime.date.today() + datetime.timedelta(1)):%d}"+'-'+f"{datetime.date.today():%m}"+'-'+f"{datetime.date.today():%y}"}
    elif any(item in data for item in obj_next_day):
        payload = {'ngayxem': f"{(datetime.date.today() + datetime.timedelta(2)):%d}"+'-'+f"{datetime.date.today():%m}"+'-'+f"{datetime.date.today():%y}"}
    try:
        response = requests.post(url, headers=headers, data= payload)
        soup = bs4.BeautifulSoup(response.text,'html.parser')
        text = soup.get_text()
        text=text.replace('\n',' ')   
        return text
    except:
        return 'Không tra cứu được kết quả ngày này năm xưa'
def zingmp3_process(data):
    mp3_link=None
    title=''
    artists=''
    # print("Tìm bài hát: "+data+"...")
    try:
        resp = requests.get('http://ac.mp3.zing.vn/complete/desktop?type=song&query='+urllib.parse.quote(data))
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        songID = obj["data"][1]['song'][0]['id']
        songUrl= "https://mp3.zing.vn/bai-hat/"+songID+".html"
        # print(songUrl)
        resp = requests.get(songUrl)
        # print(resp.text)
        key = re.findall('data-xml="\/media\/get-source\?type=audio&key=([a-zA-Z0-9]{20,35})', resp.text)
        # key = re.findall('data-xml="\/media\/get-source\?type=video&key=([a-zA-Z0-9]{20,35})', resp.text)
        songApiUrl = "https://mp3.zing.vn/xhr/media/get-source?type=audio&key="+key[0]
        resp = requests.get(songApiUrl)
        resultJson = json.dumps(resp.json())
        obj = json.loads(resultJson)
        # print(str(obj))
        mp3_link = obj["data"]["source"]["128"]
        title=obj["data"]["title"]
        artists=obj["data"]["artists"][0]["name"]
        # print(title)
        # print(artists)        
        # print(mp3_link)
    except (IndexError, ValueError):
        title='Lỗi khi tìm bài hát trên zingmp3'        
    return title,artists,mp3_link
def youtube_process(data):
    title=''
    value=''
    data = data.lower()
    try:
        query_string = urllib.parse.urlencode({"search_query" : data})
        html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
        list_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
        url = "http://www.youtube.com/watch?v="+list_results[0]
        # getting video
        video = pafy.new(url) 
        title=video.title
        # getting all the available streams
        streams = video.allstreams      
        # selecting one stream
        stream = streams[1]      
        # getting https url of stream
        value = stream.url_https
    except (IndexError, ValueError):
        title='Lỗi khi tìm bài hát trên youtube'        
    return title, str(value)
def music_process(data):
    result=None
    song_path=None
    song_link=None
    music_compare_result=[]
    try:
        for i in range(len(song_path_list)):
            match_ratio=fuzz.token_sort_ratio(data, song_path_list[i].replace('.mp3','').lower())
            music_compare_result.append(match_ratio)
    except:
        result='Lỗi khi tìm bài hát trên thẻ nhớ'        
    if max(music_compare_result) > music_compare:
        song_path=song_path_list[music_compare_result.index(max(music_compare_result))] 
        result=song_path.split('.mp3')[0].upper()
        return result,'mp3/'+song_path,song_link
    else:
        zing_result=zingmp3_process(data)
        if zing_result[2] is not None: #ZingMp3 Link 
            #+data.upper()
            result=zing_result[0] +' '+zing_result[1]            
            song_link=zing_result[2]
        else:
            youtube_result=youtube_process(data)
            result=youtube_result[0]            
            song_link=youtube_result[1]
        return result,song_path,song_link
def radio_process(data):
    result=None
    song_path=None
    song_link=None
    if any(item in data for item in obj_radio_name):         #Check News Source
        for i in range(len(obj_radio_name)):
            if obj_radio_name[i] in data:
                result=obj_radio_name[i]
                song_link=obj_radio_link[i]                
    else:
        result='Lỗi khi tìm kiếm kênh Radio'
    return result,song_path,song_link
def network_speed_process():
    result=''
    try:
        external_ip = urllib.request.urlopen('https://ident.me').read().decode('utf8')
        url = 'http://ip-api.com/json/'+external_ip
        response = requests.get(url) 
        isp_name = response.json()['org']
        st = speedtest.Speedtest()
        download = round(st.download()/1024000,2)
        upload= round(st.upload()/1024000,2)
        servernames = []
        st.get_servers(servernames)
        ping_result =st.results.ping        
        result= 'Địa chỉ WAN là ' +str(external_ip)+' thuộc nhà mạng '+str(isp_name)+ ', tốc độ download '+str(download) +' Mbps, tốc độ upload  '+str(upload) +' Mbps, thời gian ping '+str(ping_result)+' giây'
    except (IndexError, ValueError):
        result='Lỗi khi kiểm tra thông tin đường truyền'
    return result
def news_process(data):
    result=''
    list_result=[]
    if any(item in data for item in obj_news_name):         #Check News Source
        news_source=None
        for i in range(len(obj_news_name)):
            if obj_news_name[i] in data:
                newsFeed = feedparser.parse(obj_news_link[i])           
                news_source=obj_news_name[i]
        for j in range(1,3): 
            entry = newsFeed.entries[j]
            # print (entry.published)
            clean = re.compile('<.*?>')
            clean_content= re.sub(clean, '', entry.summary)
            list_result.append(', '+clean_content+', ')        
        result= 'Tin tức hôm nay từ ' +news_source+' '.join(list_result)
    else:
        result= 'Tên nguồn tin không đúng'
    return result
def time_process(opt):

    if opt =='TIME':
        return 'Bây giờ là ' + datetime.datetime.today().strftime('%H') +' giờ '+datetime.datetime.today().strftime('%M') +' phút '+datetime.datetime.today().strftime('%S') +' giây'
    elif opt=='DAY':
        return 'Hôm nay là ngày ' + f"{datetime.date.today():%d}"
    elif opt=='MONTH':
        return 'Tháng này là tháng ' + f"{datetime.date.today():%m}"    
    elif opt=='YEAR':
        return 'Năm nay là năm ' + str(datetime.date.today().year)    

def gass_process(path1,path2,data):
    api_endpoint = ASSISTANT_API_ENDPOINT
    lang = None
    display = True
    credentials=path1
    device_config =path2
    grpc_deadline = DEFAULT_GRPC_DEADLINE
# def main(api_endpoint, credentials,
         # device_model_id, device_id, lang, display, verbose,
         # grpc_deadline, *args, **kwargs):
    # Setup logging.
    # logging.basicConfig(level=logging.DEBUG if verbose else logging.INFO)
    # Load OAuth 2.0 credentials.
    try:
        with open(credentials, 'r') as f:
            credentials = google.oauth2.credentials.Credentials(token=None,
                                                                **json.load(f))
            http_request = google.auth.transport.requests.Request()
            credentials.refresh(http_request)
    except Exception as e:
        logging.error('Error loading credentials: %s', e)
        logging.error('Run google-oauthlib-tool to initialize '
                      'new OAuth 2.0 credentials.')
        return
    # Create an authorized gRPC channel.
    grpc_channel = google.auth.transport.grpc.secure_authorized_channel(
        credentials, http_request, api_endpoint)
    logging.info('Connecting to %s', api_endpoint)
    try:
        with open(device_config) as f:
            device = json.load(f)
            device_id = device['id']
            device_model_id = device['model_id']
            # logging.info("Using device model %s and device id %s",
                         # device_model_id,
                         # device_id)
    except Exception as e:
        logging.warning('Device config not found: %s' % e)
        sys.exit(-1)
    with SampleTextAssistant(lang, device_model_id, device_id, display,
                             grpc_channel, grpc_deadline) as assistant:
        response_text, response_html = assistant.assist(text_query=data)
        if response_text:
            if 'Sau đây là kết quả' in response_text:
                return ''
            elif 'Sau đây là một kết quả' in response_text:
                return ''
            elif 'Lệnh tìm kiếm cho ra kết quả sau đây' in response_text:
                return ''            
            elif 'Đây là kết quả hàng đầu' in response_text:
                return ''
            elif 'Sau đây là một số kết quả từ quá trình tìm kiếm' in response_text:
                return ''                
            else:
                return response_text
        if response_html is not None:            
            html_content=os.linesep.join(h.handle(response_html.decode("utf-8")).split(os.linesep)[:15]).split('[')[0].replace("weather.com", "").replace('\n', ' ').replace(':', ' ')
            if 'Sau đây là kết quả' in html_content:
                return ''
            elif 'Sau đây là một kết quả' in html_content:
                return ''
            elif 'Lệnh tìm kiếm cho ra kết quả sau đây' in html_content:
                return ''            
            elif 'Đây là kết quả hàng đầu' in html_content:
                return ''            
            elif 'Sau đây là một số kết quả từ quá trình tìm kiếm' in html_content:
                return ''                            
            elif 'Thử nói' in html_content:
                html_content=html_content.split('Thử nói')[0]
                return html_content
            else:
                return html_content
        # if response_text is None and response_html is None:
                # html_content ='Câu trả lời không thể hiển thị dưới dạng giọng nói được'

def chatgpt_process(token,engine,data):
    openai.api_key = token
    completion = openai.Completion.create(
      engine=engine,
      prompt=data,
      temperature=0.5,
      max_tokens=512,
      top_p=1.0,
      # frequency_penalty=abs(0.1),
      presence_penalty=2.0
    )
    # print the completion
    return completion['choices'][0]['text'].strip()

if __name__ == '__main__':
    print(lunar_calendar_process('ngày mai âm lịch'))
