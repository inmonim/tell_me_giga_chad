from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from module.giga_pt import text_request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/respond", response_class=HTMLResponse)
async def respond(request: Request, user_question: str = Form(...)):
    response = text_request(user_question).choices[0].message.content
    return templates.TemplateResponse("respond.html", {"request": request, "response": response})