cd /d %~dp0
call conda remove --name myenv --all
call conda create -n myenv python=3.8
call conda.bat activate myenv
call pip install -r ./requirements.txt
call conda clean -ya
pause

