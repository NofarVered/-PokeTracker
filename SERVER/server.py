from fastapi import FastAPI
# from fastapi.staticfiles import StaticFiles
# from fastapi.responses import FileResponse
import uvicorn


app = FastAPI()


# app.mount("/fronted", StaticFiles(directory="fronted"), name="fronted")


@app.get('/')
def root():
    # return FileResponse('./fronted/index.html')
    return "Hello Pokemon"


if __name__ == "__main__":
    uvicorn.run("server:app", host="0.0.0.0", port=8080, reload=True)
