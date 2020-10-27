#include <string>
#include <vector>
#include <algorithm>
using namespace std;
bool compare(int i, int j){
    return j<i;
}

string solution(string s) {
    string answer = "";
    sort(s.begin(),s.end(),compare);
    
    return s;
}


#include <string>
#include <vector>
#include <sstream>
using namespace std;

int solution(string s) {
    int answer = 0;
    stringstream ssInt(s);
    ssInt >> answer;
    
    return answer;
}