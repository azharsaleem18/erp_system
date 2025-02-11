import logging
from rest_framework.views import exception_handler
from rest_framework.exceptions import APIException
from django.http import Http404
from django.core.exceptions import PermissionDenied

# Initialize Logger
logger = logging.getLogger(__name__)

def custom_exception_handler(exc, context):
    """
    A professional exception handler for enterprise-level Django projects.
    It logs errors, handles custom messages, and ensures secure API responses.
    """
    # Call DRF's default exception handler to get the standard error response
    response = exception_handler(exc, context)

    # Extract view information
    view = context.get("view", None)
    request = context.get("request", None)

    # Log the error for monitoring & debugging
    logger.error(
        f"Error in view: {view.__class__.__name__ if view else 'Unknown'} | "
        f"Method: {request.method if request else 'Unknown'} | "
        f"Path: {request.get_full_path() if request else 'Unknown'} | "
        f"Exception: {str(exc)}"
    )

    # If response exists, add status code
    if response is not None:
        response.data["status_code"] = response.status_code

        # Customize error messages for common exceptions
        if isinstance(exc, Http404):
            response.data["message"] = "The requested resource was not found."
        elif isinstance(exc, PermissionDenied):
            response.data["message"] = "You do not have permission to perform this action."
        elif isinstance(exc, APIException):
            response.data["message"] = response.data.get("detail", "An API error occurred.")
        else:
            response.data["message"] = "An unexpected error occurred."

    return response
