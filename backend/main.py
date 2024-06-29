from typing import Union

from fastapi import FastAPI

app = FastAPI(title='WorkoutAPI')

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

if __name__ == 'main':

    import uvicorn

    uvicorn.run('main:app', host='0.0.0.0', port=8000, reload=True, log_level='info')