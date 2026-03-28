import json

POLICY_PATH = "policy_docs/health_policy.txt"

_index = None
_policy_chunks = None
_vector_store_available = None

def _initialize_vector_store():
    global _index, _policy_chunks, _vector_store_available
    if _vector_store_available is None:
        try:
            from vector_store import create_vector_store
            _index, _policy_chunks = create_vector_store(POLICY_PATH)
            _vector_store_available = True
        except Exception as e:
            print(f"Warning: Vector store unavailable: {e}")
            _vector_store_available = False
    return _index, _policy_chunks if _vector_store_available else (None, None)

def process_claim(claim_text):
    try:
        from llm_engine import validate_claim
        
        index, policy_chunks = _initialize_vector_store()
        
        # Use default clauses if vector store failed
        if index is None or policy_chunks is None:
            clauses = ["No policy clauses available - using raw claim for analysis"]
        else:
            try:
                from vector_store import retrieve_clauses
                clauses = retrieve_clauses(claim_text, index, policy_chunks)
            except Exception as e:
                print(f"Warning: Could not retrieve clauses: {e}")
                clauses = ["Error retrieving policy clauses"]
        
        result = validate_claim("\n".join(clauses) if clauses else "", claim_text)
        return result
        
    except Exception as e:
        # Return a safe JSON error response
        error_msg = str(e)
        return json.dumps({
            "decision": "PENDING",
            "payable_amount": 0,
            "applied_clauses": [],
            "explanation": f"Error processing claim: {error_msg}",
            "status": "error"
        })
