# from fastapi import FastAPI
import sys
import uvicorn


if __name__ == "__main__":
    sys.path.append("server")
    uvicorn.run('server.app:app',host='127.0.0.1',port=5000, reload=True,log_level='info')




