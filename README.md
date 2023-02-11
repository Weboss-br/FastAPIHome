# FastAPIHome
Trabalhos e testes em FastAPI em casa

Primeiro ativamos o venv
    python -m venv .venv 
Depois executamos ele:
    .venv/scripts/activate

Caso seja a primeira vez que utilize o Venv, provavelmente vai dar um erro. 

Abra o Powershell e modo Admin e execute o seguinte comando: Set-ExecutionPolicy -Executionpolicy AllSigned
Opção A. 

Lição - 10:

Path parameters:  "{id}"

@app.get('/blog/{id}')
def index(id):
	return("message": f"Blog with id {id}"}
#Teste o resultado assim: http://127.0.0.1:8000/blog/65
#Deverá aparecer o num 65

Predefined values

Query parameters