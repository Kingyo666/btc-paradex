"""测试 DLL 加载"""
import sys
import os

print("=" * 60)
print("Python 环境信息")
print("=" * 60)
print(f"Python 版本: {sys.version}")
print(f"Python 路径: {sys.executable}")
print(f"架构: {'64位' if sys.maxsize > 2**32 else '32位'}")
print()

print("=" * 60)
print("测试导入")
print("=" * 60)

try:
    print("1. 测试 win32api...")
    import win32api
    print("   ✅ win32api 导入成功")
except Exception as e:
    print(f"   ❌ win32api 导入失败: {e}")

try:
    print("2. 测试 crypto_cpp_py...")
    import crypto_cpp_py
    print("   ✅ crypto_cpp_py 导入成功")
except Exception as e:
    print(f"   ❌ crypto_cpp_py 导入失败: {e}")

try:
    print("3. 测试 starknet_py...")
    from starknet_py.hash.address import compute_address
    print("   ✅ starknet_py 导入成功")
except Exception as e:
    print(f"   ❌ starknet_py 导入失败: {e}")

try:
    print("4. 测试 paradex_py...")
    from paradex_py import ParadexSubkey
    print("   ✅ paradex_py 导入成功")
except Exception as e:
    print(f"   ❌ paradex_py 导入失败: {e}")
    import traceback
    traceback.print_exc()

print()
print("=" * 60)
print("DLL 路径检查")
print("=" * 60)

dll_files = [
    r"C:\Python310\pythoncom310.dll",
    r"C:\Python310\pywintypes310.dll",
]

for dll in dll_files:
    exists = os.path.exists(dll)
    print(f"{'✅' if exists else '❌'} {dll}")

import site
site_packages = site.getsitepackages()
for sp in site_packages:
    pywin32_path = os.path.join(sp, "pywin32_system32")
    if os.path.exists(pywin32_path):
        print(f"✅ pywin32_system32: {pywin32_path}")
        dlls = [f for f in os.listdir(pywin32_path) if f.endswith('.dll')]
        print(f"   包含 {len(dlls)} 个 DLL 文件")

print()
print("测试完成！")
