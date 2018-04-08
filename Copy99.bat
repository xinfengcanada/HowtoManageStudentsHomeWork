@ECHO OFF
rem Author:ITDAMAO
rem Feature:Copy99.bat copys dir
rem Created Time£º2018-04-02 13:20
rem Last Modified Time:2018-04-08 10:39
rem inputfile:01ListofClasses.txt

setlocal EnableDelayedExpansion
for /f "tokens=* delims=" %%i in (01ListofClasses.txt) do (
set className=%%i
xcopy 99CollectionofHomeworkforCopy .\!className!\  /e /s
)
