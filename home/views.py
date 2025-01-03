from django.shortcuts import render
from utils.logging import log_api_request
from rest_framework.views import APIView
from rest_framework.response import Response
from .Middleware import MicrosoftValidation
from rest_framework import status
from utils.HTTPRequest import HTTPRequest

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
    method: str = "GET"  # Default HTTP method



    def perform_request(self, request):
        """
        Determines the appropriate HTTP method and sends the request.
        """
        body, params = self.process_request(request)
        http_client = HTTPRequest()
        if self.method == "GET":
            return http_client.send_get_request(self.endpoint,body=body,params=params)
        elif self.method == "POST":
            return http_client.send_post_request(self.endpoint, data=body)
        elif self.method == "PUT":
            return http_client.send_put_request(self.endpoint, data=body)
        elif self.method == "PATCH":
            return http_client.send_patch_request(self.endpoint, data=body)
        elif self.method == "DELETE":
            return http_client.send_delete_request(self.endpoint, params=params)
        
        else:
            raise ValueError(f"Unsupported HTTP method: {self.method}")

    def process_request(self, request):
        """
        Prepares the request data based on class attributes and method.
        Handles scenarios where a GET request may have a body, params, both, or neither.
        """
        body = request.data if self.has_body else None
        params = request.query_params if self.has_params else None

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

class CreateNomineeApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_NOMINEE
    endpoint = "uw_nominee/createNominee"
    method = "POST"
    has_body = True

class CreateFinancialInfoApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_FINANCIAL_INFO
    endpoint = "uw_mbrFinInfo/createMbrFinInfo"
    method = "POST"
    has_body = True

class CreateMemberLifeStyleApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_MEMBER_LIFESTYLE
    endpoint = "uw_memLifeStyle/saveMbrLifeStyle"
    method = "POST"
    has_body = True

class ProductSearchApiView(BaseAPIView):
    role = settings.API_NILAS_PRODUCT_SEARCH
    endpoint = "uw_product/getProductsByAge"
    method = "GET"
    has_params = True

class CreateQuoteApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_QUOTE
    endpoint = "uw_quotes/createQuotes"
    method = "POST"
    has_body = True

class SaveApplicationApiView(BaseAPIView):
    role = settings.API_NILAS_SAVE_APPLICATION
    endpoint = "uw_case/createCase"
    method = "POST"
    has_body = True

class PayoutDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_PAYOUT_DETAILS
    endpoint = "uw_PayOutMode/savePayOutMode"
    method = "POST"
    has_body = True

class CreatePaymentDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_PAYMENT_DETAILS
    endpoint = "uw_polPremium/createPolPremium"
    method = "POST"
    has_body = True

class GetAllPlanApiView(BaseAPIView):
    role = settings.API_NILAS_GET_ALL_PLAN
    endpoint = "uw_product/getAllPlanByAge"
    method = "GET"
    has_params = True

class GetAllProductByPlanNoApiView(BaseAPIView):
    role = settings.API_NILAS_GET_ALL_PRODUCT_BY_PLAN_NO
    endpoint = "uw_product/getAllProductByPlanNo"
    method = "GET"
    has_params = True

class GetFrequencyApiView(BaseAPIView):
    role = settings.API_NILAS_GET_FREQUENCY
    endpoint = "PASService/rest/services/queries/GetFrequencyDetails"
    method = "GET"
    has_params = True

class GetDurationsApiView(BaseAPIView):
    role = settings.API_NILAS_GET_DURATIONS
    endpoint = "PASService/rest/services/queries/GetDurationDetails"
    method = "GET"
    has_params = True

class CustomerSearchApiView(BaseAPIView):
    role = settings.API_NILAS_CUSTOMER_SEARCH
    endpoint = "profinch-insurance/customerSearch"
    method = "POST"
    has_body = True

class GetPremiumLimitsApiView(BaseAPIView):
    role = settings.API_NILAS_GET_PREMIUM_LIMITS
    endpoint = "uw_product/getPremiumLimits"
    method = "POST"
    has_body = True

class CreatePayoutModeApiView(BaseAPIView):
    role = settings.API_NILAS_CREATE_PAYOUT_MODE
    endpoint = "uw_PayOutMode/savePayOutMode"
    method = "POST"
    has_body = True

class IdentificationDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_IDENTIFICATION_DETAILS
    endpoint = "uw_member/identificationDetails"
    method = "POST"
    has_body = True

class DocumentsUploadApiView(BaseAPIView):
    role = settings.API_NILAS_DOCUMENTS_UPLOAD
    endpoint = "documents/upload"
    method = "POST"
    has_body = True

class PayerDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_PAYER_DETAILS
    endpoint = "uw_member/payerDetails"
    method = "POST"
    has_body = True

class InitialPaymentDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_INITIAL_PAYMENT_DETAILS
    endpoint = "uw_PayOutMode/initialPaymentDetails"
    method = "POST"
    has_body = True

class PaymentDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_PAYMENT_DETAILS
    endpoint = "uw_polPremium/paymentDetails"
    method = "POST"
    has_body = True

class GenerateApplicationIdApiView(BaseAPIView):
    role = settings.API_NILAS_GENERATE_APPLICATION_ID
    endpoint = "uw_random/generateApplicationId"
    method = "GET"
    has_params = True

class InsuredDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_INSURED_DETAILS
    endpoint = "uw_case/insuredDetails"
    method = "POST"
    has_body = True

class UpdateFinancialInfoApiView(BaseAPIView):
    role = settings.API_NILAS_UPDATE_FINANCIAL_INFO
    endpoint = "uw_mbrFinInfo/updateFinancialInfo"
    method = "POST"
    has_body = True

class SubmitMedicalsApiView(BaseAPIView):
    role = settings.API_NILAS_SUBMIT_MEDICALS
    endpoint = "uw_case/submitMedicals"
    method = "POST"
    has_body = True

class SubmitAdditionalMedicalsApiView(BaseAPIView):
    role = settings.API_NILAS_SUBMIT_ADDITIONAL_MEDICALS
    endpoint = "medicalService/submitAdditionalMedicals"
    method = "POST"
    has_body = True

class BeneficiaryDetailsApiView(BaseAPIView):
    role = settings.API_NILAS_BENEFICIARY_DETAILS
    endpoint = "uw_case/beneficiaryDetails"
    method = "POST"
    has_body = True
