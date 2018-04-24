@ECHO OFF
rem 作者:IT达摩
rem 功能:统计学生交作业的情况
rem 命令说明：
rem 统计学生作业 %1 %2,%1,%2两个必选参数.
rem %1代表课时,如"Lesson1",%2代表班级,如"1-65"即六（5）班
rem 创建时间：2018-03-30 08:20
rem 最后修改时间:2018-04-16 11:20
rem 输入文件:A3各班级学生清单\1-65.txt
rem 临时文件:result.txt,title_row.txt,sort_result.txt,treeList.txt
rem 输出文件:A4各班级作业统计\Lesson1_1-65_统计.txt

setlocal EnableDelayedExpansion
rem 已交学生序号
set yesnum=""
rem 未交学生序号
set nonum=""
rem 学生总数
set totalnum=0

rem 设置文件名
set filename=%1_%2_统计
tree /f .\%2\%1 >A4各班级作业统计\treeList.txt
for /f "eol=#" %%i in (A3各班级学生清单\%2.txt) do (
set str=%%i

rem 在该目录和所有子目录中搜索包含!str!的每个文件，而不考虑字母的大小写
findstr  !str! A4各班级作业统计\treeList.txt
rem 返回值为1=未找到时，格式化输出。
IF  !ERRORLEVEL! NEQ 0 (
set /a nocount+=1
set /a nonum=!nocount!
if !nonum! lss 10 (set nonum=0!nonum!)
ECHO !nonum!	未交	%2	!str!>>noresult.txt)

rem 返回值为0=找到时，格式化输出。
IF  !ERRORLEVEL! EQU 0 (
set /a yescount+=1
set /a yesnum=!yescount! 
if !yesnum! lss 10 (set yesnum=0!yesnum!)
ECHO !yesnum!	已交	%2	!str!>>yesresult.txt)
)
rem 对生成的result.txt文件进行排序
sort  noresult.txt > sort_result.txt
echo.>>sort_result.txt
sort  yesresult.txt >> sort_result.txt

rem 文件头部作成
@echo 班    级	%2> title_row.txt
set /a totalnum=!nocount!+!yescount!
@echo 共    计	!totalnum!人>> title_row.txt
@echo 课    时	%1>> title_row.txt
@echo 作成时间	%Date:~0,4%-%Date:~5,2%-%Date:~8,2%>> title_row.txt
@echo.>> title_row.txt
@echo 序号	状态	班级	姓名>> title_row.txt

rem 合并文件
copy title_row.txt+sort_result.txt A4各班级作业统计\%filename%.txt
rem 删除临时文件:sort_result.txt,title_row.txt
del noresult.txt
del yesresult.txt
del sort_result.txt 
del title_row.txt
del A4各班级作业统计\treeList.txt