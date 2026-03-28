try:
    import api
    print("Success - api imported")
    print(f"Has app: {hasattr(api, 'app')}")
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
    import traceback
    traceback.print_exc()
