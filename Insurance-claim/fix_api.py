#!/usr/bin/env python3
import os

api_content = """from fastapi import FastAPI
from pydantic import BaseModel
from claim_validator import process_claim

app = FastAPI(title="Insurance Claim Validator")

class ClaimRequest(BaseModel):
    claim_text: str

@app.post("/validate-claim")
def validate_claim(request: ClaimRequest):
    return {"result": process_claim(request.claim_text)}
"""

filepath = "d:/insurance-claim-validator/api.py"
with open(filepath, 'w') as f:
    f.write(api_content)

print(f"✓ api.py written successfully ({len(api_content)} bytes)")
