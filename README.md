# Ecommerce-backend-with-django-and-mongodb

![Github License](https://img.shields.io/aur/license/android-studio)
![Code Coverage](https://img.shields.io/badge/coverage-80%25-green)
![python Version](https://img.shields.io/pypi/pyversions/Djongo)

This Project includes developement of backend with RESTfull services for an E commerce website [Spareware.com](https://spareware.herokuapp.com/), Where users can login as a buyer or a seller and the whole Login process is secured with token based authentication system. Sellers can post their products and Buyers can place orders. This simple project is developed to get hands-on practice with some core Computer Science and programming  topics i.e. DBMS, DSA, OOP and clean coding practices.

## Table of content

- [**Getting Started**](#getting-started)
- [API overview ](#api-overview)
- [Built With](#built-with)
- [Features](#features)
- [Flow Diagram](#flow-diagram)
- [SandBox](#sandbox)
- [Contributing](#contributing)
- [License](#license)
- [Get Help](#get-help)
- [Motivation](#motivation) 

## Getting Started 

You can use the API(s) 

### API endpoints

#### Buyer Login


Using the URL 

``` 
https://aoc001-intellisearch.herokuapp.com/iSearch/{input_data}
```

this can be done with python Request 

```
import requests

data = {
        "search_text": "Biden",
        "url": "https://www.nbcnews.com/",
        "context": "",
        "data_format": "json",
        "case_match": True,
        "base_match": True,
        "lemmatized_match": True,
        "context_match": False
       }

response = requests.post( "https://aoc001-intellisearch.herokuapp.com/iSearch/" , json = data)

print(response.text)
```


OR install the setup on your local machine 
 
### Install ( for Ubuntu based Linux distribution )

#### Clone the repo

```bash
$ git clone https://github.com/aivatanproducts/aoc001-intelliSearch.git
```

#### Create the virtualenv
```bash
$ mkvirtualenv intellisearch
```

#### Install dependencies
```bash
$ pip install -r requirements.txt
```

### Run the API on localhost
```bash
$ python3 api.py
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with inotify reloader

```


## API overview

The API is  RESTFUL and returns the output in the JSON or XML format 

You can directly call API using Python  (or any  other programming language ) 

### API inputs :

```
{
  "search_text": "string",
  "url": "string",
  "context": "string",
  "data_format": "string",
  "case_match": true,
  "base_match": false,
  "lemmatized_match": false,
  "context_match": false
}
```





 search_text: string,
              key Word for searching 
              
 url	:        string,
              Url of the site to be searched and extracted. If left blank our default list of sites will be scrapped,
              default: https://www.bbc.com/news
        
 context :    string,
              Context string helps us get more relevant data,

 data_format :string,
              Format of the data returned,
              default: Json,
              Available: Json and xml
               
 case_match	: boolean,
              For searching through case match,
              default: true
  
 base_match	: boolean,
              For searching through the base match,
              default: false
             
 lemmatized_match	: boolean,
              For searching through lemmatized match,
              default: false
  
 context_match	: boolean,
              involvels context searching,
              default: false
              
              
### API Outputs/Returns  :

  API returns the scraped data in the provided format
  
  Example Json Output
  
```
  {
  "status": "OK",
  "statusCode": 200,
  "inputs": {
    "searchtext": "Bidenzcxfghjkl",
    "url": "https://www.nbcnews.com/",
    "context": "",
    "data_format": "json",
    "case_match": true,
    "base_match": true,
    "lemmatized_match": true,
    "context_match": false
  },
  "output": {
    "case_match": {
      "p": [],
      "li": [],
      "h1": [],
      "h2": [],
      "h3": [],
      "h4": [],
      "td": [],
      "em": [],
      "a": [],
      "div": [],
      "span": []
    },
    "base_match": {
      "p": [],
      "li": [],
      "h1": [],
      "h2": [],
      "h3": [],
      "h4": [],
      "td": [],
      "em": [],
      "a": [],
      "div": [],
      "span": []
    },
    "lemmatized_match": {
      "p": [],
      "li": [],
      "h1": [],
      "h2": [],
      "h3": [],
      "h4": [],
      "td": [],
      "em": [],
      "a": [],
      "div": [],
      "span": []
    }
  },
  "Context-matched": {},
  "Entities:": {}
}

```
  
  
  
## Built With

Python

flask

NLP


## Features


Api provides the following featured framework
- Natural Language Processing(NLP) and Understanding(NLU) - Relevance in matching content
- Named entity recognition(NER) functions - To identify related entities
- web scrapping techniques to extract that relevant data
- post-processing data - packaging and format marshaling


## Flow Diagram


<img src="https://github.com/aivatanproducts/aoc001-intelliSearch/blob/master/Images/intelliSearchFlow.png" alt="drawing" width="500" hight = "1000"/>


## SandBox

Please feel free to play with the API in our sandbox 

sandbox link: https://aoc001-intellisearch.herokuapp.com/


## Contributing


#### Issues
In the case of a bug report, bugfix or suggestions, please feel free to open an issue.

#### Pull request
Pull requests are always welcome, and we will do our best to do reviews as fast as we can.


## License

This project is licensed under the [GPL License](https://github.com/aivatanproducts/aoc001-intelliSearch/blob/master/LICENSE)


## Get Help
- Contact us on admin@aivatan.cf
- If appropriate, [open an issue](https://github.com/aivatanproducts/aoc001-intelliSearch/issues) on GitHub

## Motivation
longing to learn and use the cutting edge machine learning technologies 
drives us to build and optimize the modern search techniques.



