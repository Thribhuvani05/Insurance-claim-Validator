import sys
print("Python version:", sys.version)
print("Python path:", sys.executable)

import api
print("api module imported from:", api.__file__)
print("api module attributes:", dir(api))
print("Has app:", hasattr(api, 'app'))

try:
    print("FastAPI imported:", api.FastAPI)
except:
    print("FastAPI not accessible from api")

try:
    print("app value:", api.app)
except Exception as e:
    print(f"Error accessing app: {e}")
