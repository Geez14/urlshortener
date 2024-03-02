import requests
import json
from time import time


#-----------Data--------

payload = {'url': 'https://www.google.com'}
print("payloadsize: ", len(payload['url'])+3+50)
url = payload['url']
listOfresponses = []

#-------Settings--------
count = 3
prev_time = 0
next_time = 0
max_rps = 0
min_rps = 99999999

#-------------------------JOB--------------------------
init_time = time()
while count > 0 :
    next_time = time()
    rps = (1/(next_time-prev_time))
    rpm = (60/(next_time-prev_time))
    prev_time = next_time

    if rps > max_rps:
        max_rps = rps
        print(f"\nmax_rps: {max_rps}")

    if rps < min_rps and rps != 0:
        min_rps = rps
        print(f"\nmin_rps: {min_rps}")
        
    payload['url'] = url+str(count)+"y"
    response = requests.get(url = f"https://mxtylish.pythonanywhere.com/create/api_key=1234567890", json=payload)
    listOfresponses.append(response)
    print("number of request per second : ", rps, count, end="\r")
    print("number of request per min: ", rpm,end ="\r")
    count -= 1
#-------------------------ENDJOB-----------------------
    

print("Total Time Taken: ",(time()-init_time))
for response in listOfresponses:
    if (response.status_code == 200):
        data = response.content
        data = json.loads(data)
        print(data)