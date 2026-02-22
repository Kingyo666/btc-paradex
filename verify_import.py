import sys
import os
import traceback

print("Applying Windows DLL Fix...")
# Windows DLL Fix for pywin32
if sys.platform == "win32":
    try:
        import site
        # Add pywin32_system32 to DLL search path
        site_packages = site.getsitepackages()
        for p in site_packages:
            dll_path = os.path.join(p, "pywin32_system32")
            if os.path.exists(dll_path):
                # Python 3.8+ specific
                if hasattr(os, "add_dll_directory"):
                    os.add_dll_directory(dll_path)
                # Fallback for older python or some envs
                os.environ["PATH"] = dll_path + os.pathsep + os.environ["PATH"]
                print(f"Added DLL path: {dll_path}")
                break
    except Exception as e:
        print(f"DLL Fix failed: {e}")

print("Attempting import...")
try:
    import paradex_py
    print("Import successful!")
    print(f"Location: {paradex_py.__file__}")
except ImportError as e:
    print(f"Import failed: {e}")
    traceback.print_exc()
except Exception as e:
    print(f"An error occurred: {e}")
    traceback.print_exc()
