@ECHO OFF
rem 作者:IT达摩
rem 功能:统计学生交作业的情况
rem 命令说明：
rem 统计学生作业 %1 %2,%1,%2两个必选参数.
rem %1代表课时,如"Lesson1",%2代表班级,如"C5G6"即六（5）班
rem 创建时间：2018-03-30 08:20
rem 最后修改时间:2018-04-10 16:55
rem 输入文件:03各班级学生清单\C5G6.txt
rem 临时文件:result.txt,title_row.txt,sort_result.txt
rem 输出文件:04各班级作业统计\Lesson1-C5G6.txt

setlocal EnableDelayedExpansion
rem 已交学生序号
set yesnum=0
rem 未交学生序号
set nonum=0
rem 设置文件名
set filename=%1-%2-统计

for /f "eol=#" %%i in (03各班级学生清单\%2.txt) do (
set a=%%i
rem 在该目录和所有子目录中搜索包含!a!的每个文件，而不考虑字母的大小写
findstr /s /i "\<!a!\>" .\%2\%1

rem 返回值为1=未找到时，格式化输出。
IF  ERRORLEVEL 1 IF NOT ERRORLEVEL 2 set /a nonum+=1 & @ECHO 未交	!nonum!	%2	!a!>>result.txt
rem 返回值为0=找到时，格式化输出。
IF  ERRORLEVEL 0 IF NOT ERRORLEVEL 1 set /a yesnum+=1 & @ECHO 已交	!yesnum!	%2	!a!>>result.txt
)
rem 对生成的result.txt文件进行排序
sort result.txt > sort_result.txt
rem 删除临时文件:result.txt
del result.txt
rem 文件头部作成
@echo 班    级	%2> title_row.txt
@echo 作成时间	%Date:~0,4%-%Date:~5,2%-%Date:~8,2%>> title_row.txt
@echo.>> title_row.txt
@echo 状态	序号	班级	姓名>> title_row.txt

rem 合并文件
copy title_row.txt+sort_result.txt 04各班级作业统计\%filename%.txt
rem 删除临时文件:sort_result.txt,title_row.txt
del sort_result.txt title_row.txt
