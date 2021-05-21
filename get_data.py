# -*- coding: utf-8 -*-
"""
Created on Sun Feb  7 13:48:39 2021

@author: Dell
"""

#from flask import Flask

#app=Flask(__name__)
#@app.route('/v1/api/resources')
import json    
import requests
urls=['https://jsonplaceholder.typicode.com/posts',
    'https://jsonplaceholder.typicode.com/comments',
    'https://jsonplaceholder.typicode.com/albums',
    'https://jsonplaceholder.typicode.com/photos',
    'https://jsonplaceholder.typicode.com/todos',
    'https://jsonplaceholder.typicode.com/users'
    ]

for url in urls:
    data=requests.get(url).json()
    last_name=url.split('/')[-1]
    filename=last_name+'.json'
    with open(filename,'w') as f:
        json.dump(data,f,indent=2)
    
