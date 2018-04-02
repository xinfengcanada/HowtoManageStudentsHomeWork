@ECHO OFF
rem 作者:IT达摩
rem 功能:CopyDir.bat批量复制文件夹
rem CopyDir %1
rem 参数：%1 复制源，不能以“\”结尾

rem 创建时间：2018-04-02 13:20
rem 最后修改时间:2018-04-02 14:39
rem 输入文件:班级名单.txt

setlocal EnableDelayedExpansion
for /f "tokens=* delims=" %%i in (班级名单.txt) do (
set className=%%i
xcopy %1 .\!className!\ /s /e
)