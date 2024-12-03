cd /d %~dp0
::call pip install --use-deprecated=legacy-resolver  --no-index --find-links=\\192.168.64.9\������\�������\��ʼ����������װ\3.8pgk -r .\requirements.txt
call pip install  --no-index  -r .\requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
call jupyter contrib nbextension install --user --skip-running-check
pause

