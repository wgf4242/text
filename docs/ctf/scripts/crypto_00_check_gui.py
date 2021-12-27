"""
@files list:

Crypto_check_gui_html.html
petite-vue.es.js
Crypto_00_check.py
crypto_00_check_gui.py

@ requirements
pip install fastapi base58
"""

import sys

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import JSONResponse

from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="."), name="static")
# app.mount("/", StaticFiles(directory="/"), name="/")
templates = Jinja2Templates(directory=".")

# 避免和vue语法冲突 修改jinja2模版语法标签
templates.env.block_start_string = '(%'  # 修改块开始符号
templates.env.block_end_string = '%)'  # 修改块结束符号
templates.env.variable_start_string = '(('  # 修改变量开始符号
templates.env.variable_end_string = '))'  # 修改变量结束符号
templates.env.comment_start_string = '(#'  # 修改注释开始符号
templates.env.comment_end_string = '#)'  # 修改注释结束符号


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return templates.TemplateResponse("Crypto_check_gui_html.html", {"request": request})


import Crypto_00_check as check


@app.get("/items/{id}", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("Crypto_check_gui_html.html", {"request": request})


def get_list(r):
    blst = ['dec', 'base64', 'unittest']
    lst = [x for x in dir(check) if not str(x).startswith('__') and x not in blst]
    d = {}
    # import inspect
    # all_functions = inspect.getmembers(check, inspect.isfunction)
    for method_name in lst:
        method = getattr(check, method_name)
        d[method_name] = method(r)
    return d


@app.post("/test", response_class=HTMLResponse)
async def decrypt(request: Request):
    r = await request.body()
    res = get_list(r)
    return JSONResponse(content=res)


@app.post("/getInformation")
async def getInformation(info: Request):
    req_info = await info.body()
    # req_info = await info.json()
    return req_info


# from uvicorn import main
import uvicorn

if __name__ == '__main__':
    from pathlib import Path
    import webbrowser

    file = Path(__file__)

    webbrowser.open('http://127.0.0.1:8000')

    # filename = Path(__file__).stem
    # sys.argv = [__file__, f'{filename}:app', '--reload', '--port', '80']
    # sys.exit(main())
    # uvicorn.run(app='maincor:app', host="127.0.0.1", port=8000, reload=True, debug=True)
    # filename = __file__.split('/')[-1].split('.')[0]
    uvicorn.run(app=f'{file.stem}:app', host="127.0.0.1", port=8000, reload=True, debug=True)
