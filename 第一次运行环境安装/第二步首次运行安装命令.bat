cd /d %~dp0
call pip install --use-deprecated=legacy-resolver  --no-index --find-links=\\192.168.64.9\技术部\计算软件\初始运行依赖安装\3.8pgk -r .\requirements.txt
call pip install  --no-index  -r .\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
call jupyter contrib nbextension install --user --skip-running-check
pause

