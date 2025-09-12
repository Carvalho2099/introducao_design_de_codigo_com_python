from .http_bad_request import HttpBadRequestError
from .http_unprocessable_entity import HttpUnprocessableEntityError
from typing import Dict

def handle_error(error: Exception) -> Dict:
    if isinstance(error, (HttpBadRequestError, HttpUnprocessableEntityError)):
        return {
            "status": error.status_code, 
            "boody": {
                "errors": [{
                    "title": error.name,
                    "detail": error.message
                }]
            }
        }
    
    return {
        "status": 500,
        "boody": {
            "errors": [{
                "title": "Internal Server Error",
                "detail": str(error)
            }]
        }
    }