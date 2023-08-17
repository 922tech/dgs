mkdir $1

cd $1
touch __init__.py
touch main.py
echo -e "import uvicorn\n\nif __name__ == '__main__':\n\tuvicorn.run('server.app:app',host='127.0.0.1', port=5000, reload=True)" > main.py

mkdir server

cd server
touch __init__.py
touch app.py
echo -e "from fastapi import FastAPI\n\n\napp = FastAPI()\n@app.get('/')\n\nasync def index():\n\treturn {'message':'Dev server started successfully!'}" > app.py
touch database.py
mkdir routers
mkdir utils

cd routers
