import openai
import os
import json

def _set_api_key():
    api_key = os.getenv('OPENAI_API_KEY') or "PASTE_YOUR_API_KEY_HERE"
    if api_key == "PASTE_YOUR_API_KEY_HERE":
        # Don't fail - just warn that it won't work
        print("WARNING: OpenAI API key not set. Set OPENAI_API_KEY environment variable.")
    openai.api_key = api_key

def validate_claim(policy_clauses, claim_text):
    _set_api_key()  # Set key before first use
    
    # Check if API key is not properly configured
    if openai.api_key == "PASTE_YOUR_API_KEY_HERE":
        return json.dumps({
            "decision": "PENDING",
            "payable_amount": 0,
            "applied_clauses": [],
            "explanation": "API key not configured. Please set OPENAI_API_KEY environment variable.",
            "status": "error"
        })
    
    try:
        prompt = f"""
You are an expert insurance claim analyst.

Policy Clauses:
{policy_clauses}

Claim Details:
{claim_text}

Return JSON with:
decision, payable_amount, applied_clauses, explanation
"""

        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.2
        )

        return response["choices"][0]["message"]["content"]
    
    except Exception as e:
        # Handle any error gracefully - network, API errors, malformed response, etc.
        error_msg = str(e)
        return json.dumps({
            "decision": "PENDING",
            "payable_amount": 0,
            "applied_clauses": [],
            "explanation": f"Unable to process claim: {error_msg}",
            "status": "error"
        })
