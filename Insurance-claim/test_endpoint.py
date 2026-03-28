import requests
import json

# Test the POST /validate-claim endpoint
url = "http://127.0.0.1:8000/validate-claim"

test_data = {
    "claim_text": "I had a hospital stay for 5 days due to pneumonia. Room rent was $6000, ICU charges were $2000."
}

print("Testing POST /validate-claim endpoint...")
print(f"URL: {url}")
print(f"Request: {json.dumps(test_data, indent=2)}")
print("-" * 50)

try:
    response = requests.post(url, json=test_data)
    print(f"Status Code: {response.status_code}")
    print(f"Response:")
    print(json.dumps(response.json(), indent=2))
    
    if response.status_code == 200:
        print("\n✅ SUCCESS: API returned HTTP 200 with valid JSON response!")
    else:
        print(f"\n❌ FAIL: Unexpected status code {response.status_code}")
        
except Exception as e:
    print(f"❌ Error testing API: {e}")
