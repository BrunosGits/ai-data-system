from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "AI Data System running"}

@app.post("/ask")
def ask(question: str):
    return {
        "question": question,
        "answer": f"Simulated response for: {question}"
    }
