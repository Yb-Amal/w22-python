import requests

resp = requests.get("http://playback.com")

# if resp.status_code == 200:
#     isUp = True
# else:
#     isUp = False

# print(isUp)

urls = ['http://google.com' , 'http://netflix.com' , 'http://yahoo.com' , 'http://bleacherreport.com']

for link in urls:
    resp = requests.get(link)
    if resp.status_code == 200:
        print(f"{link} is down")
