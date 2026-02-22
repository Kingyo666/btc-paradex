import sys
import os
import site

print("Python Executable:", sys.executable)
print("Site Packages:")
for p in site.getsitepackages():
    print(f"  {p}")
    pywin32_path = os.path.join(p, "pywin32_system32")
    if os.path.exists(pywin32_path):
        print(f"  FOUND explicit pywin32_system32 at: {pywin32_path}")
        try:
            items = os.listdir(pywin32_path)
            preview = items[:5]
            print(f"  Contents ({len(items)}): {preview}...")
        except Exception as e:
            print(f"  Error listing: {e}")

print("PATH environment variable:")
for p in os.environ["PATH"].split(os.pathsep):
    if "Python" in p or "site-packages" in p:
        print(f"  {p}")
