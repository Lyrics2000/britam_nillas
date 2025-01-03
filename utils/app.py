import requests
import base64
import xml.dom.minidom as minidom
import logging
import xml.etree.ElementTree as ET

from django.http import JsonResponse
from config.settings import UAT_ENV
logger = logging.getLogger(__name__)





class SoapClient:
    def __init__(self,url):
        self.url = url
     
        self.headers = {
            # "Authorization": self._get_auth_header(),
            "Content-Type": "text/xml;charset=UTF-8"
        }



    def _get_auth_header(self):
        auth_string = f"{self.username}:{self.password}"
        encoded_auth = base64.b64encode(auth_string.encode('utf-8')).decode('utf-8')
        return "Basic " + encoded_auth

    def _make_request(self,endpoint, action, payload,request):
        if request == "POST":
            try:
                response = requests.post(f"{self.url}{endpoint}", headers=self.headers, data=payload,verify=False)
                # if response.status_code == 200:

                logger.info(f"Request failed with status code: {response.status_code} {response.text}")
                print(f"Request failed with status code: {response.status_code} {response.text}")
                return response
                # else:
                #     print(f"Request failed with status code: {response.status_code}")
                #     return None
            except requests.exceptions.RequestException as e:
                logger.error(f"Connection Error: {e}")
                print("Connection Error:", e)
                return None
        else:
            try:
                response = requests.get(self.url, headers=self.headers,verify=False)
                # if response.status_code == 200:
                logger.info(f"Request failed with status code: {response.status_code} {response.text}")
                print(f"Request failed with status code: {response.status_code} {response.text}")
                #     return None
                return response
                # else:
                #     print(f"Request failed with status code: {response.status_code}")
                #     return None
            except requests.exceptions.RequestException as e:
                logger.error(f"Connection Error: {e}")
                print("Connection Error:", e)
                return None
            

    def getPersonDetails(self,data):
        payload = f"""<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:get="http://get_person_details_request.britam_ws.ws.britam.airasintersoft.com">
   <soapenv:Header/>
   <soapenv:Body>
      <get:GetPersonDetailsRequest>
         <get:MSG>
            <get:HEADER>
               <get:SITENO>4</get:SITENO>
               <get:SYSTEM_ID>SP100</get:SYSTEM_ID>
               <get:CLUSTER_NAME>GLOBAL_BUSINESS</get:CLUSTER_NAME>
               <get:SERVICE_METHOD>GET_PERSON_DETAILS</get:SERVICE_METHOD>
               <get:VERSION_NO>1.0</get:VERSION_NO>
               <get:USER_NAME>MPESA</get:USER_NAME>
               <!--Optional:-->
               <get:PASSWORD></get:PASSWORD>
               <!--Optional:-->
               <get:LANGUAGE>ENG</get:LANGUAGE>
               <get:PROCESS_STATUS>0</get:PROCESS_STATUS>
            </get:HEADER>
            <get:BODY>
               <get:SITE_AGENTNO>{data['SITE_AGENTNO']}</get:SITE_AGENTNO>
               <get:CMDB_ID>{data['CMDB_ID']}</get:CMDB_ID>
               <get:TITLE>{data['TITLE']}</get:TITLE>
               <get:FIRST_NAME>{data['FIRST_NAME']}</get:FIRST_NAME>
               <get:SURNAME>{data['SURNAME']}</get:SURNAME>
               <get:SEX>{data['SEX']}</get:SEX>
               <get:DOB>{data['DOB']}</get:DOB>
               <get:OCCUPATION>{data['OCCUPATION']}</get:OCCUPATION>
               <get:SMOKER>{data['SMOKER']}</get:SMOKER>
               <get:NATION_NO>{data['NATION_NO']}</get:NATION_NO>
               <get:NI_NUMBER>{data['NI_NUMBER']}</get:NI_NUMBER>
               <get:BIRTH_CERT_NO>{data['BIRTH_CERT_NO']}</get:BIRTH_CERT_NO>
               <get:ADDRESS_NO>{data['ADDRESS_NO']}</get:ADDRESS_NO>
               <get:PERNO>{data['PERNO']}</get:PERNO>
            </get:BODY>
         </get:MSG>
      </get:GetPersonDetailsRequest>
   </soapenv:Body>
</soapenv:Envelope>"""
        
        return self._make_request("/britam_ws/services/britam_ws_service","GetPersonDetailsRequest", payload,"POST")



    

    




