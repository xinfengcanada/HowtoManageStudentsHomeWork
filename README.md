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
├── 01ListofClasses.txt		# archive the name of class by row,sorted by number. eg.1-C5G6 standing for class 5 grade 6
├── 02ListofStudents
│   └── C5G6.txt		# archive students' name in C5G6 by row,eg.SanZhang
├── 03ListofHomework
│   └── default.md		# a removable file placeholder,the same as below
├── 99CollectionofHomeworkforCopy
│   ├── Lesson1			# save students'homework of Lesson 1 here,and so on
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
│   ├── Unit1Summary
│   │   └── default.md
│   ├── Unit2Summary
│   │   └── default.md
│   ├── Unit3Summary
│   │   └── default.md
│   ├── MiddleofTerm
│   │   └── default.md
│   ├── EndofTerm
│   │   └── default.md
│   └── Temp			# save sth temporarily
│       └── default.md
├── Copy99.bat			# copy 99CollectionofHomeworkforCopy to the directory whose filename are in 01ListofClasses.txt
├── ListStatus.bat		# create a txt file to list the status about everyone's homework in his class.
└── README.md
```
### 建立工作目录
下面的文件夹及文件是必须存在的：
```
├── 01ListofClasses.txt
├── 02ListofStudents
├── 03ListofHomework
├── 99CollectionofHomeworkforCopy
├── Copy99.bat
└── ListStatus.bat
```
### 建立课时目录
在文件夹`99CollectionofHomeworkforCopy`下，手动创建需要的课时文件夹，例如：
```
./99CollectionofHomeworkforCopy/
├── Lesson1
├── Lesson2
├── Lesson3
├── Lesson4
├── Lesson5
├── Lesson6
├── Lesson7
├── Lesson8
├── Lesson9
├── MiddleofTerm
├── EndofTerm
├── Unit1Summary
├── Unit2Summary
├── Unit3Summary
└── ...
```
每个课时文件夹用于存放学生作业文件。

:heavy_exclamation_mark:温馨提示
- `ListStatus.bat` 运行时，是依据学生姓名进行查找的，所以作业文件的文件名必须包含该学生的姓名

双击运行`Copy99.bat`,创建每个班级的存放作业的文件夹。

### 班级名单作成
将各班级名单逐行追加到`01ListofClasses.txt`文件中，并保存。

```
1-C5G6
2-C6G6
3-C2G5
...
```
上述示列中，每行为一个班级，数字代表老师个人课表上的上课次序;C5G6即指Class 5 Grade 6(六（5）班）;之间用一个短横线隔开。
### 学生名单作成
将每个班的学生名单逐行添加到相应班级的文件中，并保存。

如文件02ListofStudents\C5G6.txt用于存放六（5）班所有学生的名字。

一行一个学生，对于同名学生，建议在名字前加上“大”或“小”以示区分。

如同一个班有两个学生都叫“王鑫”，可以用“大王鑫”和“小王鑫”加以区分。

```
张三
李四
大王鑫
小王鑫
John
欧阳汝阳
...
```
### 生成统计名单
打开cmd窗口，进入`ListStatus.bat`所在的目录。
如果`ListStatus.bat`文件在E盘，可以输入如下命令：
```
cd E: /d
```
如果你要生成六（5）班第1课学生提交作业情况的文件，可以输入如下命令：
```
ListStatus Lesson1 C5G6
```
按`Enter`确定输入，很快你会得到一个`Lesson1-C5G6.txt`文件。打开`03ListofHomework\Lesson1-C5G6.txt`文件看看吧。
