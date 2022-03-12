#coding=utf-8
# http://flash.weather.com.cn/wmaps/xml/beijing.xml
# http://flash.weather.com.cn/wmaps/xml/china.xml

from urllib import request
import urllib.parse
from xml.dom.minidom import parse
import xml.dom.minidom
import time
from lxml import etree
import requests

day = time.strftime('%Y-%m-%d',time.localtime(time.time()))

def get_china():
    province_info = request.urlopen('http://flash.weather.com.cn/wmaps/xml/china.xml')
    DOMTree = xml.dom.minidom.parse(province_info)
    province_data = DOMTree.documentElement
    # 获取所有标签为<city>的信息，即全部的省
    provinces = province_data.getElementsByTagName("city")
    provinces_area_list = []
    for province in provinces:
        china_city = {}
        # 获取省的拼音
        china_city['prov_py'] = province.getAttribute("pyName")
        # 获取省的名称
        china_city['prov_name'] = province.getAttribute("quName")
        china_city['cityname'] = province.getAttribute("cityname")
        china_city['state1'] = province.getAttribute("state1")
        china_city['state2'] = province.getAttribute("state2")
        china_city['prov_t_high'] = province.getAttribute("tem2")
        china_city['prov_t_low'] = province.getAttribute("tem1")
        china_city['prov_state'] = province.getAttribute("stateDetailed")
        china_city['prov_windstate'] = province.getAttribute("windState")
        provinces_area_list.append(china_city['prov_py'])

    return provinces_area_list
# provinces_area_list --> 输入格式 eg.['shenzhen]
def get_wh(provinces_area_list):
    for xxs in provinces_area_list:
        try:
            province_info_area = request.urlopen('http://flash.weather.com.cn/wmaps/xml/%s.xml'%(xxs))
            DOMTree_area = xml.dom.minidom.parse(province_info_area)
            province_data_area = DOMTree_area.documentElement
            provinces_area = province_data_area.getElementsByTagName("city")
            for province in provinces_area:
                # 获取市
                ccity = {}
                ccity['cityname'] = province.getAttribute("cityname")
                ccity['cityX'] = province.getAttribute("cityX")
                ccity['cityY'] = province.getAttribute("cityY")
                ccity['pyName'] = province.getAttribute("pyName")
                ccity['stateDetailed'] = province.getAttribute("stateDetailed")
                ccity['tem1'] = province.getAttribute("tem1")
                ccity['tem2'] = province.getAttribute("tem2")
                ccity['windState'] = province.getAttribute("windState")
                ccity['windDir'] = province.getAttribute("windDir")
                ccity['windPower'] = province.getAttribute("windPower")
                ccity['humidity'] = province.getAttribute("humidity")
                ccity['time'] = str(day) + ' '+ str(province.getAttribute("time"))
                return(ccity)
        except Exception as e:
            print(xxs)

def get_wh_mes(area):
    # 'stateDetailed': '多云', 'tem1': '25', 'tem2': '16', 'windState': '微风转东风微风级', 'windDir': '西南风', 'windPower': '2级',
    message = get_wh(area)
    whe = message['stateDetailed']
    temp_high = message['tem1']
    temp_low = message['tem2']
    change = message['windState']
    wind_idr = message['windDir']
    wind_power = message['windPower']
    return whe ,temp_high ,temp_low ,change ,wind_idr ,wind_power

# 举例
# a = mes(['shenzhen'])
# print(a)
# --> output : ('多云', '25', '16', '微风转东风微风级', '西南风', '2级')



