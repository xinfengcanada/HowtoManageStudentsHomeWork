@ECHO OFF
rem 作者:IT达摩
rem 功能:统计学生交作业的情况
rem 命令说明：
rem listStatus %1 %2,%1,%2两个必选参数.
rem %1代表课时,如"Lesson1",%2代表班级,如"C5G6"即六（5）班
rem 创建时间：2018-03-30 08:20
rem 最后修改时间:2018-04-02 16:55
rem 输入文件:02ListofStudents\C5G6.txt
rem 临时文件:result.txt,title_row.txt,sort_result.txt
rem 输出文件:03ListofHomework\Lesson1-C5G6.txt

rem ListStatus.bat与输入输出文件之间的层次关系：
rem │ ListStatus.bat
rem │  
rem ├─03ListofHomework
rem │     Lesson1-C5G6.txt 
rem │      
rem ├─02ListofStudents
rem │      C5G6.txt
rem ├─1-C5G6
rem │      ├─Lesson1
rem │            myfile1-SanZhang.png
setlocal EnableDelayedExpansion
rem 已交学生序号
set yesnum=0
rem 未交学生序号
set nonum=0
rem 设置文件名
set filename=%1-%2-统计

for /f "tokens=* delims=" %%i in (02ListofStudents\%2.txt) do (
set a=%%i
rem 在该目录和所有子目录中搜索包含!a!的每个文件，而不考虑字母的大小写
findstr /s /i "/<!a!/>" ??%2\%1

rem 返回值为1=未找到时，格式化输出。
IF  ERRORLEVEL 1 IF NOT ERRORLEVEL 2 set /a nonum+=1 & @ECHO NO	!nonum!	%2	

!a!>>result.txt
rem 返回值为0=找到时，格式化输出。
IF  ERRORLEVEL 0 IF NOT ERRORLEVEL 1 set /a yesnum+=1 & @ECHO YES	!yesnum!	

%2	!a!>>result.txt
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
copy title_row.txt+sort_result.txt 03ListofHomework\%filename%.txt
rem 删除临时文件:sort_result.txt,title_row.txt
del sort_result.txt title_row.txt
