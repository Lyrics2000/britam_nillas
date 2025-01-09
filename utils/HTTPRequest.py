import requests

from config.settings import (
                             USERNAME,
                             PASSWORD)
import logging
import json
from requests.auth import HTTPBasicAuth
logger = logging.getLogger(__name__)


import json

class HTTPRequest:
    def __init__(self,base_url):
        self.base_url = base_url

    def is_connection_live(self):
        try:
            response = requests.get(self.base_url,verify=False)
            js_data  =  response.text
      
            return True
        except requests.exceptions.RequestException as e:
            logger.error(f"The http error is {e}")
            return False
 
    def send_get_with_body(self,url,data):
        logger.info("The url is {endpoint}")

        logger.info(f"The data sent is {data}")
        if not self.is_connection_live():
            logger.info("Connection is not live.")
            print("Connection is not live.")
            return None
        payload =  None
       

        url = url

        payload = json.dumps(data)
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("GET", url, headers=headers, data=payload,verify=False,auth=HTTPBasicAuth(USERNAME, PASSWORD))

        return response


    def send_get_request(self, url,body=None, params=None, headers=None):
        logger.info(f"The url is {url}")

        logger.info(f"The data sent is {body}")
        if not self.is_connection_live():
            logger.info("Connection is not live.")
            print("Connection is not live.")
            return None
        payload =  None

        if body:
            payload = json.dumps(body)

        logger.info(f"The payload is : {payload} ")

        url1 = self.base_url + url
        logger.info(f"The get url is {url1}")
        response = requests.get(url1, params=params,data =  payload, headers=headers,verify=False,auth=HTTPBasicAuth(USERNAME, PASSWORD))
        try:
            logger.info(f"the post response is {response.json()}")
        except:
            logger.info(f"the post response is {response.text}")
        return response
    
    

    def send_post_request(self, url, params=None, data=None):
        logger.info("The url is {endpoint}")
        if not self.is_connection_live():
            logger.info("Connection is not live.")
            print("Connection is not live.")
            return None
        logger.info(f"the request data is {data}")
        headers = {
            
            "content-type": "application/json"
        }
        url = self.base_url + url
        
        print("the url is ", url)
        logger.info(f"the data us {data}")
        payload = json.dumps(data)
        headers = {
        'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload,verify=False,auth=HTTPBasicAuth(USERNAME, PASSWORD))

        try:
            logger.info(f"the post response is {response.json()}")
        except:
            logger.info(f"the post response is {response.text}")
        return response

      