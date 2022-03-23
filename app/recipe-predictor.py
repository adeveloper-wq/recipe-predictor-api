from transformers import pipeline
from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/{satzanfang}")
async def root(satzanfang: str):
	chef = pipeline('text-generation',model='ml_model/', tokenizer='dbmdz/german-gpt2')
	result = chef(satzanfang, max_length=200)[0]['generated_text']
	return {"Rezept": result}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)