@echo off
cls
echo ��������Redis����
cd redis
start redis-server.exe
cd ..

echo �������������......
cd proxy_pool/Run
start py main.py

cd ../..
echo ������������......
start py MainBenben.py

echo Done!