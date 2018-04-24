@ECHO OFF
rem Author:ITDAMAO
rem Feature:CreatDir.bat 创建工作目录
rem Created Time：2018-04-02 13:20
rem Last Modified Time:2018-04-23 13:50


setlocal EnableDelayedExpansion
rem 创建文件A1班级清单.txt
if exist .\A1班级清单.txt (echo 当前目录下已有A1班级清单.txt存在) else (
echo 当前目录下不存在A1班级清单.txt,即将创建
echo # 以#开头行是注释行,脚本不会读取>>A1班级清单.txt
echo.>>A1班级清单.txt)

rem 创建文件A2课时清单.txt
if exist .\A2课时清单.txt (echo 当前目录下已有A2课时清单.txt存在) else (
echo 当前目录下不存在A2课时清单.txt,即将创建
echo # 以#开头行是注释行,脚本不会读取>>A2课时清单.txt
echo.>>A2课时清单.txt)

rem 创建文件：各班级学生清单
set listOfStu=A3各班级学生清单
if exist .\!listOfStu! (echo 该目录已存在) else (
mkdir .\!listOfStu!
)
for /f "eol=#" %%h in (A1班级清单.txt) do (
set cName=%%h
echo !cName!
if exist .\!listOfStu!\!cName!.txt (echo !listOfStu! 目录下已有 !cName!.txt存在) else (
echo # 以#开头行是注释行,脚本不会读取>>.\!listOfStu!\!cName!.txt
echo.>>.\!listOfStu!\!cName!.txt)
)

rem 创建文件夹：各班级作业统计
set countOfStu=A4各班级作业统计
if exist .\!countOfStu! (echo 该目录已存在) else (
mkdir .\!countOfStu!
)

rem 为每个班级创建用于收集学生作业的目录
for /f "eol=#" %%i in (A1班级清单.txt) do (
set className=%%i
for /f  "eol=#" %%j in (A2课时清单.txt) do (
set lessonName=%%j
mkdir .\!className!\!lessonName!\

rem 在每个课时目录下生成用于统计该课时学生作业情况的bat
echo @ECHO OFF>.\!className!\!lessonName!\Listme.bat
echo rem 作者:IT达摩>>.\!className!\!lessonName!\Listme.bat
echo rem 功能:统计本课时学生交作业的情况>>.\!className!\!lessonName!\Listme.bat
echo rem 创建时间：2018-04-23 13:43>>.\!className!\!lessonName!\Listme.bat
echo rem 最后修改时间:%Date:~0,4%-%Date:~5,2%-%Date:~8,2%>>.\!className!\!lessonName!\Listme.bat
echo cd /d %~dp0 >>.\!className!\!lessonName!\Listme.bat
echo ListStatus !lessonName! !className! >>.\!className!\!lessonName!\Listme.bat
)
)
