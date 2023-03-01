
from datetime import datetime

from fastapi import FastAPI, Response
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles

from settings.configs import  config
from settings.authentication import Auth, Encryption, AllowsAccess

from error import exception_handlers

app = FastAPI(docs_url=None, redoc_url=None, exception_handlers=exception_handlers)
app.mount("/statics", StaticFiles(directory="statics"), name="statics")
year: str = datetime.now().strftime("%Y")


@app.get("/", name="index")
async def index(request: Request, response: Response):
    
    context: dict = {
        "check_auth": Auth.exists_auth(request),
        "year": year,
        "request": request
    }

    response = config.TEMPLATES.TemplateResponse("index.html", context=context)
    return response

@app.post("/", name="index")
async def index(request: Request, response: Response):
    context: dict = {
                "check_auth": Auth.exists_auth(request),
                "year": year,
                "request": request
            }
    form = await request.form()
    
    if form.get("password", None) and form.get("email", None):
        password: str =  Encryption.encryption_password(form.get("password"))
        email: str = form.get("email", None)

        if AllowsAccess.allows_access(email, password):
            response = config.TEMPLATES.TemplateResponse("index.html", context=context)
            Auth.apply_auth(request, response)
            return response
        
        else:
            response = config.TEMPLATES.TemplateResponse("login.html", context=context)
            return response
    
    elif form.get("logout", None):
        response = config.TEMPLATES.TemplateResponse("index.html", context=context)
        Auth.remove_auth(request, response)
        return response
    
    else:
        response = config.TEMPLATES.TemplateResponse("login.html", context=context)
        return response

@app.get("/login", name="login")
async def index(request: Request, response: Response):

    context: dict = {
        "check_auth": Auth.exists_auth(request),
        "year": year,
        "request": request
    }

    response = config.TEMPLATES.TemplateResponse("login.html", context=context)
    return response

@app.get("/logout", name="logout")
async def index(request: Request, response: Response):

    context: dict = {
        "check_auth": Auth.exists_auth(request),
        "year": year,
        "request": request
    }

    response = config.TEMPLATES.TemplateResponse("logout.html", context=context)
    return response

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        app="app:app",
        host="0.0.0.0",
        port=8080,
        log_level="info",
        reload=True
    )