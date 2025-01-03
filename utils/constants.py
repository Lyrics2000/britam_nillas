from config.settings import (
    DEV_ENV
)
api_nilas_BASEURL = "https://api-client.britam.com/api"
class Constants:
    DEV_PAYBILL = 174379
    PROD_PAYBILL = ""
    IS_DEV_PAYBILL = True
    IS_PROD_PAYBILL = True
    MPESA_CALLBACK = "http://10.10.4.109:8000/api/v1/mpesa-callback/"
    
    IGAS_URL = "http://127.0.0.1:8082"
    MPESA_URL = "http://172.28.1.36:8077/api/v1"
    BASE_URL = "https://brtgw.britam.com" if DEV_ENV else "http://172.18.0.37:31011"
    

