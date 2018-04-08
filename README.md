# HowtoManageStudentsHomeWork

## 适用于什么情境？
作为一名信息技术老师，您可能会身处这样的困境中：

- 班级多

担任很多个班级的信息技术课程
- 学生多

每个班级学生人数众多
- 任务重

忙于很多事务，时间很有限

**如何快速统计每个班每节课哪些同学提交了作业，哪些同学没有？**
## 优势
针对以上情况，这个项目提供了一种解决方案。

不用安装任何软件，不需任何特殊的编程语言——所需的就是MS-DOS

每次统计学生交作业情况时，只需运行一个命令，就这么简单。
## 快速指导
此项目是基于Windows操作系统，简单易用，0门槛。 
### 项目结构
项目结构是约定好的，不要搞创新。:smile:

学生名单、班级名单、学生作业统计目录等都放要在默认位置，

文件夹名或文件名不要改动，命令及其参数也要遵守约定。
```
.
├── 01ListofClasses.txt
├── 02ListofStudents
│   └── C5G6.txt
├── 03ListofHomework
│   └── default.md
├── 99CollectionofHomeworkforCopy
│   ├── EndofTerm
│   │   └── default.md
│   ├── Lesson1
│   │   └── default.md
│   ├── Lesson10
│   │   └── default.md
│   ├── Lesson11
│   │   └── default.md
│   ├── Lesson12
│   │   └── default.md
│   ├── Lesson13
│   │   └── default.md
│   ├── Lesson14
│   │   └── default.md
│   ├── Lesson15
│   │   └── default.md
│   ├── Lesson16
│   │   └── default.md
│   ├── Lesson17
│   │   └── default.md
│   ├── Lesson18
│   │   └── default.md
│   ├── Lesson2
│   │   └── default.md
│   ├── Lesson3
│   │   └── default.md
│   ├── Lesson4
│   │   └── default.md
│   ├── Lesson5
│   │   └── default.md
│   ├── Lesson6
│   │   └── default.md
│   ├── Lesson7
│   │   └── default.md
│   ├── Lesson8
│   │   └── default.md
│   ├── Lesson9
│   │   └── default.md
│   ├── MiddleofTerm
│   │   └── default.md
│   ├── Unit1Summary
│   │   └── default.md
│   ├── Unit2Summary
│   │   └── default.md
│   └── Unit3Summary
│       └── default.md
├── Copy99.bat
├── ListStatus.bat
├── README.md
```
26 directories, 30 files
### 建立工作目录
下面的目录结构必须存在的：
### 准备学生名单
### 生成统计名单
