from fastapi import FastAPI
import uvicorn

from modules.geoutils import geocode


app = FastAPI()

host = app.host


@app.get('/')
async def root():
    return {
        "status": "ok",
        "message": f"For more information go to ../docs"
    }
    
    
@app.get("/coords/{address}")
async def coords(address:str):
    result = await geocode(address)
    if result:
        return {
        "status": "ok",
        "coordinates": result
        }
    return {
        "status": "error",
        "message": f"Can\'t geocode coordinates from given address: {address}"
        }
    
if __name__ == '__main__':
    uvicorn.run(app, host="0.0.0.0", port=8000)