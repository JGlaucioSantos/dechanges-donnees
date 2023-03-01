from datetime import datetime

from fastapi import status
from fastapi.exceptions import HTTPException
from fastapi.requests import Request

from settings.configs import  config


async def not_found(request: Request, ext: HTTPException):
    """
    Returns a page 404
    """
    year: str = datetime.now().strftime("%Y")
    context: dict = {
        "request": request,
        "year": year
    }

    return config.TEMPLATES.TemplateResponse("error/404.html", context=context, status_code=status.HTTP_404_NOT_FOUND)


async def server_error(request: Request, ext: HTTPException):
    """
    Returns a page 500
    """

    year: str = datetime.now().strftime("%Y")
    context: dict = {
        "request": request,
        "year": year
    }

    return config.TEMPLATES.TemplateResponse("error/500.html", context=context, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


exception_handlers = {
    404: not_found,
    500: server_error
}