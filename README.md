# Django-Ecommerce-website-backend__ V 1.0

![Github License](https://img.shields.io/aur/license/android-studio)
![Code Coverage](https://img.shields.io/badge/coverage-80%25-green)
![python Version](https://img.shields.io/pypi/pyversions/Django)

This Project includes developement of backend with RESTfull services for an E commerce website [Spareware.com](https://spareware.herokuapp.com/), Where users can login as a buyer or a seller and the whole Login process is secured with token based authentication system. Sellers can post their products and Buyers can place orders. This simple project is developed to get hands-on practice with some core Computer Science and programming  topics i.e. DBMS, DSA, OOP and clean coding practices.

## Table of content

- [**Getting Started**](#getting-started)
- [API overview ](#API-endpoints)
- [Built With](#built-with)
- [Contributing](#contributing)
- [License](#license)
- [Get Help](#get-help)
- [Contact](#contact)
- [Motivation](#motivation) 

## Getting Started 

You can use the API(s) 

### Install ( for Windows OS  )

#### Clone the repo

```bash
$ git clone https://github.com/Vivek1258/Django-Ecommerce-website-backend.git
```

#### Create the virtualenv
( using python virtualenv )

```bash
$ virtualenv env
$ cd Django-Ecommerce-website-backend
```

#### Install dependencies
```bash
$ pip install -r requirements.txt
```

### Run the API on localhost
```bash
$ python manage.py runserver
```



### API endpoints

###### Since we are using token based authentication, after login,api will return a unique token. 
###### This token will be used to excess all the information about the user by the front end. 


### Buyer Operations 

#### Register Buyer 

##### method : POST

The URL 

``` 
http://127.0.0.1:8000/users/api/register_buyer/
```

Example JSON body : 

Here username, email, and password are only required fields other information can be updated in the buyer profile 

```
{
        "username" : "Buyer1258" , 
        "email" : "bye.yar18@gmail.com",
        "password" : "Buyer@1258",


        "first_name" : "Bye" ,
        "last_name" : "yar",
        "mobile_number" : 1000000000 ,
        "img_link" : "https://sample.com" ,


        "lane_no" : "3" ,
        "landmark" : "Easy Death Hospital",
        "village" : "sample village",
        "district" : "sample district",
        "state" : "sample state",

        "pro_user" : false
}
```

#### Get Buyer Profile

##### method :  GET


The URL 

``` 
http://127.0.0.1:8000/users/api/buyer-profile/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```


#### Update Buyer Profile

##### method : PUT


The URL 

``` 
http://127.0.0.1:8000/users/api/update-buyer-profile/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```

JSON Body :

```
{
        "mobile_number" : 1000000000 ,
        "img_link" : "https://sample.com" ,

        "lane_no" : "3" ,
        "landmark" : "Easy Death Hospital",
        "village" : "sample village",
        "district" : "sample district",
        "state" : "sample state"
 }


```


#### Place Order 

##### method : POST


The URL 

``` 
http://127.0.0.1:8000/users/api/place_order/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```

JSON Body :

```
{
        "order_sat" : "Placed",
        "item_id" : 1
}

```



#### Get list of Order placed 

##### method : GET


The URL 

``` 
http://127.0.0.1:8000/users/api/place_order/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```
 



### Seller Operations


#### Register Seller

##### method : POST

The URL 

``` 
http://127.0.0.1:8000/users/api/register_seller/
```

Example JSON body : 

Here, All the information are required fields sinse we are registering a seller 

```
{
        "username" : "Seller1258" , 
        "first_name" : "Sel" ,
        "last_name" : "ler",
        "email" : "sel.ler18@gmail.com",
        "password" : "Seller@1258",
        "mobile_number" : 1000000000 ,
        "img_link" : "https://sample.com" ,

        "lane_no" : "3" ,
        "landmark" : "Easy Death Hospital",
        "village" : "sample village",
        "district" : "sample district",
        "state" : "sample state",

        "shop_type": "Electronics Goods",
        "official_doc_link" : "https://sample.com"
 }
```


#### Get Seller Profile

##### method :  GET


The URL 

``` 
http://127.0.0.1:8000/users/api/seller-profile/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```



#### Update Seller Profile

##### method : PUT


The URL 

``` 
http://127.0.0.1:8000/users/api/update-seller-profile/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```

JSON Body :

```
{
        "mobile_number" : 1000000000 ,
        "img_link" : "https://sample.com" ,

        "lane_no" : "3" ,
        "landmark" : "Easy Death Hospital",
        "village" : "sample village",
        "district" : "sample district",
        "state" : "sample state",

        "shop_type": "Electronics Goods",
        "official_doc_link" : "https://sample.com"
}


```


#### Post an Item 

##### method : POST


The URL 

``` 
http://127.0.0.1:8000/users/api/add_product/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```

JSON Body :

```
{

            "item_name": "When I met your Mother",
            "item_type": "Book",
            "item_sub_type": "Story",
            "seller": "Raj Sellers",
            "seller_email" : "raja@shop.com",
            "seller_mobile" : 12345678910 ,
            "rating" : 2 ,
            "availability": true,
            "stock" : 20 ,
            "price": 540, 
            "image_link": "https://www.sampleurl.com",
            "description": "some text",
            "specifiation": "some text"

}

```
#### Get list of Uploaded Items  

##### method : GET


The URL 

``` 
http://127.0.0.1:8000/users/api/get_products/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```
 
 
 
 ### Login/Logout/Update Password
 
 
#### User(Buyer/Seller) Login 

##### method : POST

The URL 

``` 
http://127.0.0.1:8000/users/api/login/
```

Example JSON body : 

```
{
        "username" : "Seller1258" , 
        "password" : "Seller@1258"
 }
```

 

#### User(Buyer/Seller) Update Password 

##### method : POST

The URL 

``` 
http://127.0.0.1:8000/users/api/login/
```


Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```
 
 
Example JSON body : 

```
{
        "old_password" : "Seller1258" , 
        "new_password" : "Seller@1258"
 }
```


#### User(Buyer/Seller) Logout

##### method : POST

The URL 

``` 
http://127.0.0.1:8000/users/api/logout/
```

Header should contain Authorization key with value as Token  :

```
"Authorization" : "Token ###############################################"
```


 
## Built With

Python

Django ( For Backend )

Django Rest Framework ( for RESTfull services )

Django Rest Knox ( For User Authentication )


## Contributing


#### Issues
In the case of a bug report, bugfix or suggestions, please feel free to open an issue.

#### Pull request
Pull requests are always welcome, and we will do our best to do reviews as fast as we can.


## License

This project is licensed under the [Apache License](https://github.com/Vivek1258/Django-Ecommerce-website-backend/blob/main/LICENSE)

## Get Help

- If appropriate, [open an issue](https://github.com/Vivek1258/Django-Ecommerce-website-backend/issues) on GitHub

## Contact 

- Contact me on [LinkedIn](https://www.linkedin.com/in/vivek-mankar-182735184/) 
- Email mankarvivek172000@gmail.com

## Motivation

I am a Machine Learning Practitioner. In the path of becoming a Machine Learning Engineer 

I intend to learn Web development to get a Complete understanding of how web applications work.
 





