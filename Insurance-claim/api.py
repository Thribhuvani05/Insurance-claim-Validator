from fastapi import FastAPI
from pydantic import BaseModel
from claim_validator import process_claim
import json

app = FastAPI(title="Insurance Claim Validator")

class ClaimRequest(BaseModel):
    claim_text: str

@app.post("/validate-claim")
def validate_claim(request: ClaimRequest):
    try:
        result = process_claim(request.claim_text)
        # If result is a string (JSON), parse it to return as object
        if isinstance(result, str):
            try:
                return {"result": json.loads(result)}
            except:
                return {"result": result}
        return {"result": result}
    except Exception as e:
        # Graceful error handling - return 200 with error details
        error_msg = str(e)
        return {
            "result": {
                "decision": "PENDING",
                "payable_amount": 0,
                "applied_clauses": [],
                "explanation": f"Error processing claim: {error_msg}",
                "status": "error"
            }
        }
