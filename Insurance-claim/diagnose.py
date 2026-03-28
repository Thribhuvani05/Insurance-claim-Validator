#!/usr/bin/env python3
import os
import sys
import shutil

os.chdir('d:\\insurance-claim-validator')

# Step 1: Check and report file content
print("=" * 60)
print("Step 1: Checking api.py file content")
print("=" * 60)
with open('api.py', 'rb') as f:
    content = f.read()
print(f"File size: {len(content)} bytes")
if len(content) > 0:
    print(f"First 100 bytes: {content[:100]}")
else:
    print("FILE IS EMPTY!")

# Step 2: Clear cache
print("\n" + "=" * 60)
print("Step 2: Clearing__pycache__")
print("=" * 60)
try:
    shutil.rmtree('__pycache__')
    print("✓ Cache cleared")
except Exception as e:
    print(f"Cache clear error: {e}")

# Step 3: Clear module cache
print("\n" + "=" * 60)
print("Step 3: Clearing Python module cache")
print("=" * 60)
for mod in list(sys.modules.keys()):
    if 'api' in mod or 'claim_validator' in mod or 'vector_store' in mod or 'llm_engine' in mod:
        del sys.modules[mod]
        print(f"✓ Deleted {mod}")

# Step 4: Try to import
print("\n" + "=" * 60)
print("Step 4: Attempting to import api")
print("=" * 60)
try:
    import api
    print("✓ Import successful")
    print(f"Module file: {api.__file__}")
    print(f"Module attributes: {dir(api)}")
    if hasattr(api, 'app'):
        print(f"✓ app exists: {api.app}")
    else:
        print("✗ app attribute NOT FOUND")
except Exception as e:
    print(f"✗ Import failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("DONE")
print("=" * 60)
