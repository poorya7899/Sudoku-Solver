#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

int map[9][9][2];
char letter[9] = {'A','B','C','D','E','F','G','H','I'};
void printmap(){
	for(int i=0 ; i<9 ; i++){
		for(int j = 0 ; j<9 ; j++){
//			cout<<map[i][j][0];
			if(map[i][j][1]==0){
				cout<<letter[i]<<j+1<<"="<<map[i][j][0]<<",";
			}
		}
		cout<<endl;
	}
	cout<<"--------------------------"<<endl;
}

bool eval(int index){
	int i , j;
	i = index / 9;
	j = index % 9;
	for(int p=0 ; p < j ; p++){
		if(map[i][p][0] == map[i][j][0]){
			return false;
		}
	}
	for(int p=j+1 ; p < 9 ; p++){
		if(map[i][p][0] == map[i][j][0]){
			return false;
		}
	}
	for(int p=0 ; p < i ; p++){
		if(map[p][j][0] == map[i][j][0]){
			return false;
		}
	}
	for(int p=i+1 ; p < 9 ; p++){
		if(map[p][j][0] == map[i][j][0]){
			return false;
		}
	}
	int start_r = i / 3;
	int start_c = j / 3;
	start_r *= 3;
	start_c *= 3;
	for(int p=0 ; p < 3 ; p++){
		for(int q=0 ; q<3 ; q++){
			if(start_r+p!=i || start_c+q!=j){
				if(map[start_r+p][start_c+q][0]==map[i][j][0]){
					return false;
				}
			}
		}
	}
	
	return true;
}

void build(int index){
	int i , j;
	i = index / 9;
	j = index % 9;
	if(index == 81){
		printmap();
	}
	else if(map[i][j][1] == 0){
		for(int n=1 ; n<= 9 ; n++){
			map[i][j][0] = n;
			if(eval(index)){
				build(index+1);
			}	
		}
		map[i][j][0] = 0;
	}
	else{
		index++;
		build(index);
	}
	
}

int main(){
	memset(map,0,sizeof(map));
	fstream file;
	string s;
	int i=0;
	file.open("sudoku.txt");
	while(file>>s){
		for(int j=0 ; j<9 ; j++){
			if(s[j] != '0'){
				map[i][j][0] = s[j]-'0';
				map[i][j][1] = 1;
			}
		}
		i++;
	}
	build(0);
}
