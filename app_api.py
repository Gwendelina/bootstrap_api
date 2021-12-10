from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

# Ajout de cette méthode pour gérer l'erreur d'accessibilité 'access-control-allow-origin'
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/contact/{contact_id}")
def contact_details(contact_id: int):
    return {"contact_id": contact_id}

@app.get("/age/{future_age}")
def future_age(future_age: int):
    return {"future_age" : future_age + 10}


