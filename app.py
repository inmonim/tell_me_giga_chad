from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles

from db import session
from model import Log

from module.giga_pt import text_request

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/respond", response_class=HTMLResponse)
async def respond(request: Request, user_question: str = Form(...)):
    response = text_request(user_question)
    answer = response.choices[0].message.content
    token = response.usage.completion_tokens
    with session() as db:
        log = Log(question=user_question, token=int(token), answer=answer)
        db.add(log)
        db.commit()
        
    return RedirectResponse(url=f"/result?response={answer}", status_code=303)
    
@app.get("/result", response_class=HTMLResponse)
async def show_result(request: Request, response: str):
    return templates.TemplateResponse("respond.html", {"request": request, "response": response})