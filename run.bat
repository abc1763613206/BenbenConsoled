@echo off
cls
echo 正在启动Redis缓存
cd redis
start redis-server.exe
cd ..

echo 正在启动代理池......
cd proxy_pool/Run
start py main.py

cd ../..
echo 正在启动服务......
start py MainBenben.py

echo Done!