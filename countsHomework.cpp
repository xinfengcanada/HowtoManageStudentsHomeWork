/*
	Name:  
	Copyright: 
	Author: 吴心锋
	Date: 25/10/21 14:57
	Description: 
	此版本依赖的文件夹目录结构如下所示：
	F:.
└─2021.9-2022.2	//作品文件夹的根目录
    │  
    └─61			//班级 
        ├─第1周
        ├─第2周
        ├─……
        └─第N周 
    └─62
        ├─第1周
        ├─第2周
        ├─……
        └─第N周
    …… 
*/

#include<iostream>
#include<fstream>
#include<string>
#include <regex>
#include <iomanip>
using namespace std;

int main() {
	string homeWorkDir ="F:\\2021.9-2022.2";//作品文件夹的根目录 
	int whichWeek;
	string cmdString1;
	string homeWorkFileName="作品目录汇总.txt";
	string outputFileName = "作品统计结果.cvs";
	string classID;
	string studentsInfoFileName;
	
	ifstream finStu,finHWF;
	ofstream fout;
	string name,str;
	
	const int sumRowNum = 60;//班级人数
	const int sumColNum = 3;//序号，班级，姓名；共3列；
	const int sumColNum2 = 4;//序号，班级，姓名,次数；共4列；
	const int colOfIndex = 0;
	const int colOfClass = 1;
	const int colOfName = 2;
	const int colOfCounter = 3;
	string studentsInfoArray[sumRowNum][sumColNum];
	string tempArray[sumRowNum][sumColNum2];

	int row, col;
	
	cout<<"您要统计哪个班的作品？请选择："<<endl
	    <<"52,53,54,55,"<<endl
		<<"56,57,58,59,"<<endl
		<<"61,62,63,64,"<<endl
		<<"65,66,67,68,"<<endl
		<<"69,70(编程班)"<<endl;
	cin>>classID;
	
    cout<<"您要统计"<<classID<<"班第几周的作品？请选择："<<endl;
    cout<<"1-18之间或99，99代表所有周次。"<<endl;
	cin>>whichWeek;
    
	if((whichWeek>=1)&&(whichWeek<=18))	{
		//homeWorkDir = homeWorkDir+"\\第"+ to_string(whichWeek) +"周\\"+classID; 
		homeWorkDir = homeWorkDir+"\\"+ classID+"\\第"+ to_string(whichWeek) +"周"; 
		homeWorkFileName= classID+"班_第"+to_string(whichWeek)+"周_"+ homeWorkFileName; 
		outputFileName = classID+"班_第"+to_string(whichWeek)+"周_"+ outputFileName;
	}else{
		homeWorkDir = homeWorkDir+"\\"+ classID;
		homeWorkFileName= classID+"班_"+ homeWorkFileName;
		outputFileName = classID+"班_" + outputFileName;
	} 
	
	cmdString1 ="tree /F "+homeWorkDir+" > "+homeWorkDir+"\\"+ homeWorkFileName;
	
	studentsInfoFileName=classID+".txt";
	int counter = 0;
	
	//打开文件
	finStu.open(studentsInfoFileName);//打开学生信息文
	//TODO:读取学生信息文件 存入数组
	while (finStu.peek() != EOF) {
		for (row = 0; row < sumRowNum; row++) {
			for (col = 0; col < sumColNum; col++) {
				finStu >> studentsInfoArray[row][col];
			}
		}
	}
	finStu.close();
	while (getchar()!=113) {//按q键退出 
		system("cls"); 
        //调用cmd生成指定目录（包括子目录）下所有文件名并保存到  homeWorkFileName
		system(cmdString1.c_str());

		//打开文件
		finHWF.open(homeWorkDir+"\\"+homeWorkFileName);//打开学生作品汇总文件
	
		//标题行作成
		tempArray[0][colOfIndex] = "序号";
		tempArray[0][colOfClass] = "班级";
		tempArray[0][colOfName] = "姓名";
		tempArray[0][colOfCounter] = "作品数量";
		//查找比对
		for (row = 1; row < sumRowNum && studentsInfoArray[row][colOfIndex] != ""; row++) {
			counter = 0;
			regex e(studentsInfoArray[row][colOfName]);
			while (getline(finHWF, str)) {
				
				bool match = regex_search(str, e);
				if (match) { counter++; }
			}
			//数组复制并添加“作品数量”列
			for (col = 0; col < sumColNum2; col++) {
				if (col == colOfCounter) {// 添加“作品数量”列
					tempArray[row][col] = to_string(counter);
				}
				else {
					tempArray[row][col] = studentsInfoArray[row][col];//复制其它列 
				}
			}
			
			finHWF.clear();
			//文件读指针移动到文件开头位置
			finHWF.seekg(0, ios::beg);			
		}
		finHWF.close();
		//“作品数量”列升序排列
		for (row = 0; row < sumRowNum && tempArray[row][colOfIndex] != ""; row++) {
			for (int j = row; j < sumRowNum && tempArray[j][colOfIndex] != ""; j++) {
				//string 转化为 int
				char* end;
				int k = static_cast<int>(strtol(tempArray[row][colOfCounter].c_str(), &end, 10));
				int h = static_cast<int>(strtol(tempArray[j][colOfCounter].c_str(), &end, 10));
				if (k > h) {
					swap(tempArray[row][colOfIndex], tempArray[j][colOfIndex]);
					swap(tempArray[row][colOfClass], tempArray[j][colOfClass]);
					swap(tempArray[row][colOfName], tempArray[j][colOfName]);
					swap(tempArray[row][colOfCounter], tempArray[j][colOfCounter]);
				}
			 }
		}
		//重新编序号
		//for (row = 1; row < sumRowNum && tempArray[row][colOfIndex] != ""; row++) {
		//	tempArray[row][colOfIndex] = to_string(row);
		//}
		
		//输出到屏幕
		cout << "          "<<classID<<"班第"<<whichWeek<<"周学生作品统计表          " << endl;//标题行作成
		for (row = 0; row < sumRowNum && tempArray[row][colOfIndex] != ""; row++) {
			for (col = 0; col < sumColNum2; col++) {
				if (col == colOfName) {
					cout << setw(8) << tempArray[row][col] << "\t";
				}
				else {
					cout << setw(4) << tempArray[row][col] << "\t";
				}
			}
			cout << endl;
		}
		//system("pause");
		cout<<endl; 
		cout<<"按 ENTER 键刷新或按 q 键退出……"<<endl; 
	}
	//写入"统计结果.cvs"文件
	fout.open(homeWorkDir + "\\" + outputFileName);
	//outputFileName文件 标题行作成
	fout << "          "<<classID<<"班第"<<whichWeek<<"周学生作品统计表          " << endl;//标题行作成
	for (row = 0; row < sumRowNum && tempArray[row][colOfIndex] != ""; row++) {
		for (col = 0; col < sumColNum2; col++) {
			if (col == colOfName) {
				fout << setw(8) << tempArray[row][col] << "\t";
			}
			else {
				fout << setw(4) << tempArray[row][col] << "\t";
			}
		}
		fout << endl;
	}
	
	fout.close();
	return 0;
}
