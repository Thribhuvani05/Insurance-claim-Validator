# LLM-Based Insurance Claim Validation System

## Overview
This project automates insurance claim validation using Retrieval-Augmented Generation (RAG).

## Tech Stack
- FastAPI
- Sentence Transformers
- FAISS
- OpenAI GPT-4

## Features
- Semantic policy clause retrieval
- Explainable claim decisions
- Robust error handling and fallbacks

## How to Run

```bash
conda activate insurance_llm
cd insurance-claim-validator
pip install -r requirements.txt
python -m uvicorn api:app --reload


Sample Input
{
  "claim_text": "Hospitalization for 4 days, room rent ₹8000/day"
}


