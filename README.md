# SimpleHeaderFormatter
A very simple tool to output raw http request headers as a string to be used as a dictionary for python requests. Extremely simple program, but can save a lot of time when web scraping with headers!

**Usage:**

from ConvertToDictionary import HeaderConvert

print(HeaderConvert('''RAW_HEADERS'''))


**Example:**

```python
from ConvertToDictionary import HeaderConvert

print(HeaderConvert('''sec-ch-ua: "Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'''))
```

OUTPUT: 
```python
{'sec-ch-ua': '"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'}
```

Then copy and paste your output into your python code, as your headers dictionary!
