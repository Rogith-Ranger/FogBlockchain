import requests 
import time


API_ENDPOINT = "http://127.0.0.1:5000/square/2"
t1_start = time.time() 
r = requests.post(url = API_ENDPOINT) 
print("Time Taken to process the request:",time.time()-t1_start)
t2_start = time.time() 
print(2**2)
print("Time Taken to process the request:",time.time()-t2_start)
print(r.text)
