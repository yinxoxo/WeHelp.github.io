from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse
from starlette.middleware.sessions import SessionMiddleware

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="secret")

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/")
def get_home(request: Request):
    # 檢查登入狀態，如果已登入，可以直接重定向到會員頁面
    if request.session.get("signed_in"):
        return RedirectResponse(url="/member", status_code=303)
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/signin")
async def signin(
    request: Request,
    username: str = Form(None),
    password: str = Form(None),
    remember_me: bool = Form(False),
):
    if not username or not password:
        return RedirectResponse(url="/error?message=請輸入帳號、密碼", status_code=303)
    if username == "test" and password == "test":
        # 設置用戶登入狀態
        request.session["signed_in"] = True
        response = RedirectResponse(url="/member", status_code=303)
        response.set_cookie(key="remember_me", value=str(remember_me), httponly=True)
        return response
    else:
        return RedirectResponse(
            url="/error?message=帳號或密碼輸入錯誤", status_code=303
        )


@app.get("/signout")
def signout(request: Request):
    # 清除用戶登入狀態
    request.session.pop("signed_in", None)
    return RedirectResponse(url="/", status_code=303)


@app.get("/member")
def member(request: Request):
    # 檢查用戶是否登入
    if request.session.get("signed_in"):
        return templates.TemplateResponse("member.html", {"request": request})
    else:
        # 如果未登入，重定向到首頁
        return RedirectResponse(url="/", status_code=303)


@app.get("/error")
def error(request: Request, message: str = None):
    return templates.TemplateResponse(
        "error.html", {"request": request, "message": message}
    )
