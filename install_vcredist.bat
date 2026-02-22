@echo off
echo 正在下载 Microsoft Visual C++ Redistributable...
curl -L -o vc_redist.x64.exe https://aka.ms/vs/17/release/vc_redist.x64.exe
echo.
echo 开始安装...
vc_redist.x64.exe /install /quiet /norestart
echo.
echo 安装完成！请重新运行 scalper.py
pause
