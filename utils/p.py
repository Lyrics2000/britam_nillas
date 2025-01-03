from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import logging

logger = logging.getLogger(__name__)

class BaseAPIView(APIView):
    # Base class attributes
    role: str = None
    endpoint: str = None
    has_body: bool = False  # Indicates if the request has a body
    has_params: bool = False  # Indicates if the request has query parameters
    method: str = "GET"  # Default HTTP method

    def process_request(self, request):
        """
        Prepares the request data based on class attributes and method.
        """
        if self.has_body and self.method in ["POST", "PUT", "PATCH"]:
            body = request.data
        else:
            body = None

        if self.has_params and self.method == "GET":
            params = request.query_params
        else:
            params = None

        return body, params

    def authenticate_and_authorize(self, request):
        """
        Example method to handle authentication and authorization.
        """
        # Replace this with actual authentication and role validation logic
        logger.info(f"Validating role: {self.role}")
        return True

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

    def perform_request(self, request):
        """
        Determines the appropriate HTTP method and sends the request.
        """
        body, params = self.process_request(request)
        http_client = HTTPRequest()
        if self.method == "GET":
            return http_client.send_get_request(self.endpoint, params=params)
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
