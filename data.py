'''
A list of dictionaries containing data on website urls.
'''

WEBSITES = [
    {
        "name": "Google",
        "url": "https://www.google.co.uk",
        "domain": "google.co.uk",
        "secure": True,
        "value": 5
    },
    {
        "name": "Facebook",
        "url": "https://developers.facebook.com/blog/post/2018/10/02/facebook-login-update/",
        "domain": "facebook.com",
        "secure": True,
        "value": 4
    },
    {
        "name": "Bing",
        "url": "https://www.bing.com/search?q=athlete&qs=n&form=QBLH&sp=-1&pq=athlete&sc=8-7&sk=&cvid=53830DD7FB2E47B7A5D9CF27F106BC9A",
        "domain": "bing.com",
        "secure": False,
        "value": 3
    },
    {
        "name": "Ask",
        "url": "https://uk.ask.com/web?o=0&l=dir&qo=serpSearchTopBox&q=jupiter",
        "domain": "ask.com",
        "secure": False,
        "value": 1
    },
    {
        "name": "Duck Duck Go",
        "url": "http://duckduckgo.com/?q=plane&t=h_&ia=web",
        "domain": "duckduckgo.com",
        "secure": True,
        "value": 2
    },
    {
        "name": "Vimeo",
        "url": "https://vimeo.com/53812885",
        "domain": "vimeo.com",
        "secure": False,
        "value": 2
    },
    {
        "name": "YouTube",
        "url": "https://www.youtube.com/watch?v=09Cd7NKKvDc",
        "domain": "youtube.com",
        "secure": True,
        "value": 5
    },
    {
        "name": "Daily Motion",
        "url": "http://www.dailymotion.com/search/football",
        "domain": "dailymotion.com",
        "secure": True,
        "value": 1
    }
]


find_data = [x for x in WEBSITES if x["value"] >= 4 ]
amend_data = [x.update(domain = 'www.' + x['domain']) for x in WEBSITES]
# cleanest_data = [ x["secure"] = False if "https://" in x['url'] else True for x in WEBSITES ]


cleanest_data = [x.update(secure=True) if "https://" in x['url'] else x.update(secure = False) for x in WEBSITES if "https://" in x['url']]
total = 0
data_calculation = [total := total + x['value'] for x in WEBSITES][-1]

print(find_data)
print(amend_data)
print(cleanest_data)
print(data_calculation)
print(WEBSITES)