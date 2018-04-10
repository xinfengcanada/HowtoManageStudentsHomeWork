@ECHO OFF
rem Author:ITDAMAO
rem Feature:CreatDir.bat 创建工作目录
rem Created Time：2018-04-02 13:20
rem Last Modified Time:2018-04-10 10:51


setlocal EnableDelayedExpansion
rem 创建文件01班级清单.txt
echo 创建文件01班级清单.txt
if exist .\01班级清单.txt (echo 当前目录下已有01班级清单.txt存在) else (
echo 当前目录下不存在01班级清单.txt,即将创建
echo # 以#开头行是注释行,脚本不会读取>>01班级清单.txt
echo. >>01班级清单.txt
echo # 99-default作为缺省项,由程序自动创建>>01班级清单.txt
echo 99-default>>01班级清单.txt
echo. >>01班级清单.txt)

rem 创建文件02课时清单.txt
echo 创建文件02课时清单.txt
if exist .\02课时清单.txt (echo 当前目录下已有02课时清单.txt存在) else (
echo 当前目录下不存在02课时清单.txt,即将创建
echo # 以#开头行是注释行,脚本不会读取>>02课时清单.txt
echo. >>02课时清单.txt
echo # default作为缺省项,由程序自动创建>>02课时清单.txt
echo default>>02课时清单.txt
echo. >>02课时清单.txt)

rem 创建文件：各班级学生清单
echo 创建文件：各班级学生清单
set listOfStu=03各班级学生清单
if exist .\!listOfStu! (echo 该目录已存在) else (
mkdir .\!listOfStu!
)
for /f "eol=#" %%h in (01班级清单.txt) do (
set cName=%%h
echo !cName!
if exist .\!listOfStu!\!cName!.txt (echo !listOfStu! 目录下已有 !cName!.txt存在) else (
echo # 以#开头行是注释行,脚本不会读取>>.\!listOfStu!\!cName!.txt
echo. >>.\!listOfStu!\!cName!.txt
echo # 99-学生 作为缺省项,由程序自动创建>>.\!listOfStu!\!cName!.txt
echo 99-学生>>.\!listOfStu!\!cName!.txt
echo. >>.\!listOfStu!\!cName!.txt)
)

rem 创建文件夹：各班级作业统计
echo 创建文件夹：04各班级作业统计
set countOfStu=04各班级作业统计
if exist .\!countOfStu! (echo 该目录已存在) else (
mkdir .\!countOfStu!
)

rem 为每个班级创建用于收集学生作业的目录
echo 为每个班级创建用于收集学生作业的目录
for /f "eol=#" %%i in (01班级清单.txt) do (
set className=%%i
echo !className!
for /f  "eol=#" %%j in (02课时清单.txt) do (
set lessonName=%%j
mkdir .\!className!\!lessonName!\)

)
pause
