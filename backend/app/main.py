from fastapi import FastAPI

app = FastAPI(
    title="UniMind AI",
    description="AI-powered document assistant",
    version="0.1.0",
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "project": "unimind-ai",
    }