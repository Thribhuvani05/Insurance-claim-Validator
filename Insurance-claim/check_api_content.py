import os

print(f"Reading api.py from: d:\\insurance-claim-validator\\api.py")
with open('d:\\insurance-claim-validator\\api.py', 'r') as f:
    content = f.read()

print(f"File size: {len(content)} bytes")
print(f"First 200 chars: {repr(content[:200])}")
print(f"Full content:")
print("=" * 50)
print(content)
print("=" * 50)
