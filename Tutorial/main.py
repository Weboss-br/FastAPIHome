from fastapi import FastAPI

app = FastAPI ()

@app.get('/hello')
def index():
    return {'message' : 'Hello world!'}

#A ordem dos fatores alteram o resultado. Como o próximo resulta do Path, ele interfere caso ('/blog/all') esteja depois 
@app.get('/blog/all')
def get_all_blogs():
    return {'message':'Tudo do site'}

#Teste: http://127.0.0.1:8000/blog/65
@app.get('/blog/{id}')
def get_blog(id: int):
    return {'message' : f'Blog com id {id}!'}