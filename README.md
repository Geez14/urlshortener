**Website is live**

**link :** [pythonanywhere](https://mxtylish.pythonanywhere.com)

A Web Application to shorten the long urls into short urls
* Add API support
* maximum request speed: 271-100 rps
* minimum request speed: 70-45

### Documentation

* python:
``` python
import requests

payload = {"url":"https://www.xyz.com"}

response = request(
            url = "localhost:8000/create/api_key=xxxxxxxxxx",
            json=payload
          )
if (response.status_code == 200):
  data = response.content
  data = json.loads(data)
  print(data)
  # output
  """

  response_json_content
  {"url": "https://www.xyz.com" , "shorturl" : "localhost:8000/xyzpqrs"}

  """
```

Future Implementation:
  * Add Good frontend and multiple routing for the frontend, example:
      1. Add multiple pages so the user can be redirected if the Url is bad or short url genration is successfull
      2. Make custom url
      3. Get statistic for the custom url
