import logging
from django.shortcuts import render
from utils.logging import log_api_request
from rest_framework.views import APIView
from rest_framework.response import Response
from .Middleware import MicrosoftValidation
from rest_framework import status
from utils.HTTPRequest import HTTPRequest
logger = logging.getLogger(__name__)
# A utility function to handle logging
def log_view_request(view_name, request, message, level="INFO"):
    log_data = {
        "view": view_name,
        "method": request.method,
        "path": request.path,
        "query_params": request.query_params,
        "data": request.data,
        "message": message,
    }
    log_api_request(level,request.path,request.data,"",0,f"{view_name} - {message}")
    # pass
class BaseAPIView(APIView):
    role: str = None
    endpoint: str = None
    has_body: bool = True
    has_params: bool = True
    base_url:str = ""
    method: str = "GET"  # Default HTTP method



    def perform_request(self, request):
        """
        Determines the appropriate HTTP method and sends the request.
        """
        body, params = self.process_request(request)
        logger.info(f"Body: {body}, Params:{params}")
        logger.info(f"HasBody: {self.has_body}")
        http_client = HTTPRequest(self.base_url)
        if self.method == "GET":            
            return http_client.send_get_request(f"{self.endpoint}",body=body,params=params)
        elif self.method == "POST":
            return http_client.send_post_request(f"{self.endpoint}", data=body)
        elif self.method == "PUT":
            return http_client.send_put_request(f"{self.endpoint}", data=body)
        elif self.method == "PATCH":
            return http_client.send_patch_request(f"{self.endpoint}", data=body)
        elif self.method == "DELETE":
            return http_client.send_delete_request(f"{self.endpoint}", params=params)
        elif self.method == "SEND_AS_GET":
            return http_client.send_get_request(f"{self.endpoint}",body=body,params=params)
        
        

        else:
            raise ValueError(f"Unsupported HTTP method: {self.method}")

    def process_request(self, request):
        """
        Prepares the request data based on class attributes and method.
        Handles scenarios where a GET request may have a body, params, both, or neither.
        """
        body = request.data if self.has_body else None
        params = request.query_params.dict() if self.has_params else None

        return body, params
    


    
    def authenticate_and_authorize(self, request):
        view_name = self.__class__.__name__
        app = MicrosoftValidation(request).verify()
        if app.status_code == 401:
            log_view_request(view_name, request, "Unauthorized access attempt", level="warning")
            return None, Response({"message": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED)

        roles = app.json().get("data", {}).get("roles", [])
        if self.role not in roles:
            log_view_request(view_name, request, "Access denied: Insufficient roles", level="warning")
            return None, Response({"message": "Access Denied: Insufficient Roles"}, status=status.HTTP_403_FORBIDDEN)

        log_view_request(view_name, request, "Authentication and authorization successful")
        return app, None

    def handle_request(self, request):
        """
        Core method that handles incoming requests.
        """
        if not self.authenticate_and_authorize(request):
            return Response(
                {"status": "Failed", "message": "Unauthorized access"},
                status=status.HTTP_403_FORBIDDEN,
            )

        response = self.perform_request(request)
        return self.handle_response(request, response)
    
    def handle_response(self, request, response):
        """Handles the response returned by HTTPRequest.
        """
        if response is None:
            return Response(
                {"status": "Failed", "message": "Connection issue with the server"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
        try:
            return Response(response.json(), status=response.status_code)
        except Exception:
            return Response(
                {"status": "Failed", "message": "Invalid response format"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def get(self, request):
        """
        Handles GET requests.
        """
        return self.handle_request(request)

    def post(self, request):
        """
        Handles POST requests.
        """
        return self.handle_request(request)

    def put(self, request):
        """
        Handles PUT requests.
        """
        return self.handle_request(request)

    def patch(self, request):
        """
        Handles PATCH requests.
        """
        return self.handle_request(request)

    def delete(self, request):
        """
        Handles DELETE requests.
        """
        return self.handle_request(request)

from django.conf import settings

class CreateMemberApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_MEMBER
    endpoint = "uw_member/createMember"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class CreateNomineeApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_NOMINEE
    endpoint = "uw_nominee/createNominee"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class CreateFinancialInfoApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_FINANCIAL_INFO
    endpoint = "uw_mbrFinInfo/createMbrFinInfo"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class CreateMemberLifeStyleApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_MEMBER_LIFESTYLE
    endpoint = "uw_memLifeStyle/saveMbrLifeStyle"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class ProductSearchApiView(BaseAPIView):
    role = settings.API_NILAS_PRODUCT_SEARCH
    endpoint = "uw_product/getProductsByAge"
    method = "GET"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class CreateQuoteApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_QUOTE
    endpoint = "uw_quotes/createQuotes"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class SaveApplicationApiView(BaseAPIView):
    role = settings.API_NILAS_SAVE_APPLICATION
    endpoint = "uw_case/createCase"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class PayoutDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_PAYOUT_DETAILS
    endpoint = "uw_PayOutMode/savePayOutMode"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class CreatePaymentDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_PAYMENT_DETAILS
    endpoint = "uw_polPremium/createPolPremium"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class GetAllPlanApiView(BaseAPIView):
    role = settings.API_NILAS_GET_ALL_PLAN
    endpoint = "uw_product/getAllPlanByAge"
    method = "SEND_AS_GET"
    has_body =True
    base_url = "http://10.10.3.237:9099/"

class GetAllProductByPlanNoApiView(BaseAPIView):
    role = settings.API_NILAS_GET_ALL_PRODUCT_BY_PLAN_NO
    endpoint = "uw_product/getAllProductByPlanNo"
    method = "GET"
    has_body =  True
    base_url = "http://10.10.3.237:9099/"

class GetFrequencyApiView(BaseAPIView):
    role = settings.API_NILAS_GET_FREQUENCY
    endpoint = "PASService/rest/services/queries/GetFrequencyDetails"
    method = "GET"
    has_params = True
    base_url = "http://10.10.3.236:8012/"

class GetDurationsApiView(BaseAPIView):
    role = settings.API_NILAS_GET_DURATIONS
    endpoint = "PASService/rest/services/queries/GetDurationDetails"
    method = "GET"
    has_params = True
    base_url = "http://10.10.3.236:8012/"

class CustomerSearchApiView(BaseAPIView):
    role = settings.API_NILAS_CUSTOMER_SEARCH
    endpoint = "profinch-insurance/customerSearch"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:7701/"

class GetPremiumLimitsApiView(BaseAPIView):
    role = settings.API_NILAS_GET_PREMIUM_LIMITS
    endpoint = "uw_product/getPremiumLimits"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class CreatePayoutModeApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_PAYOUT_MODE
    endpoint = "uw_PayOutMode/savePayOutMode"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class IdentificationDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_IDENTIFICATION_DETAILS
    endpoint = "uw_member/identificationDetails"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class DocumentsUploadApiView(BaseAPIView):
    role = settings.API_NILAS_DOCUMENTS_UPLOAD
    endpoint = "documents/upload"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class PayerDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_PAYER_DETAILS
    endpoint = "uw_member/payerDetails"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class InitialPaymentDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_INITIAL_PAYMENT_DETAILS
    endpoint = "uw_PayOutMode/initialPaymentDetails"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class PaymentDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_PAYMENT_DETAILS
    endpoint = "uw_polPremium/paymentDetails"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class GenerateApplicationIdApiView(BaseAPIView):
    role = settings.API_NILAS_GENERATE_APPLICATION_ID
    endpoint = "uw_random/generateApplicationId"
    method = "GET"
    has_params = True
    base_url = "http://10.10.3.237:9099/"

class InsuredDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_INSURED_DETAILS
    endpoint = "uw_case/insuredDetails"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class UpdateFinancialInfoApiView(BaseAPIView):
    role = settings.API_NILAS_UPDATE_FINANCIAL_INFO
    endpoint = "uw_mbrFinInfo/updateFinancialInfo"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class SubmitMedicalsApiView(BaseAPIView):
    role = settings.API_NILAS_SUBMIT_MEDICALS
    endpoint = "uw_case/submitMedicals"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class SubmitAdditionalMedicalsApiView(BaseAPIView):
    role = settings.API_NILAS_SUBMIT_ADDITIONAL_MEDICALS
    endpoint = "medicalService/submitAdditionalMedicals"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class BeneficiaryDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_BENEFICIARY_DETAILS
    endpoint = "uw_case/beneficiaryDetails"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"


class NomineeDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_NOMINEE_DETAILS
    endpoint = "uw_case/nomineeDetails"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"

class SubSequentPaymentApiView(BaseAPIView):
    role = settings.API_NILAS_SUBSEQUENT_PAYMENT
    endpoint = "uw_PayOutMode/subSequentPayment"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"


class FinalSubmissionCaseApplicationApiView(BaseAPIView):
    role = settings.API_NILAS_FINAL_SUBMISSION_CASE_APPLICATION
    endpoint = "uw_case/finalSubmissionCaseApplication"
    method = "POST"
    has_body = True
    base_url = "http://10.10.3.237:9099/"



class AsCodeRelationshipsApiView(BaseAPIView):
    role = settings.API_NILAS_AS_CODE_RELATIONSHIPS
    endpoint = "PASService/rest/services/v1/codes"
    method = "GET"
    has_body = False
    has_params = True
    base_url = "http://10.10.3.236:8012/"



class AsCodeBritamOccupationApiView(BaseAPIView):
    role = settings.API_NILAS_AS_CODE_BRITAM_OCCUPATION
    endpoint = "PASService/rest/services/v1/codes"
    method = "GET"
    has_body = False
    has_params = True
    base_url = "http://10.10.3.236:8012/"


class AsCodeClientPrefixApiView(BaseAPIView):
    role = settings.API_NILAS_AS_CODE_CLIENT_PREFIX
    endpoint = "PASService/rest/services/v1/codes"
    method = "GET"
    has_body = False
    has_params = True
    base_url = "http://10.10.3.236:8012/"


class AsCodeMaritalStatusApiView(BaseAPIView):
    role = settings.API_NILAS_AS_CODE_MARITAL_STATUS
    endpoint = "PASService/rest/services/v1/codes"
    method = "GET"
    has_body = False
    has_params = True
    base_url = "http://10.10.3.236:8012/"


