from fastapi import FastAPI

app = FastAPI(
    title="AI Backend",
    description="Backend built with FastAPI, LangChain and LangGraph",
    version="1.0.0"
)

@app.get("/")
def health():
    return {
        "status" : "UP",
        "service": "AI Backend"
    }