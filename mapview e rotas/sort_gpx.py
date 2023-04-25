import requests
import re

start_lat = -15.57 
start_lon = -56.03

end_lat = -15.596045470064421
end_lon = -56.09322712851902


body = {"coordinates":[[start_lon, start_lat],[end_lon,end_lat]]}

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': '5b3ce3597851110001cf6248a1421a2fb7894e5787241e5932437192',
    'Content-Type': 'application/json; charset=utf-8'
}
call = requests.post('https://api.openrouteservice.org/v2/directions/driving-car/gpx', json=body, headers=headers)

string_res = call.text
print(string_res)

tag = 'rtept'
reg_str = '</' + tag + '>(.*?)' + '>'
res = re.findall(reg_str, string_res)
print(res)
print('___________________________')
string1 = str(res)
tag1 = '"'
reg_str1 = '"' + '(.*?)' + '"'
res1 = re.findall(reg_str1, string1)
print(res1)