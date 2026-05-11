#include <iostream>
using namespace std;
int main() {
	int n;
	cin >> n;
	if (n >= 0) {//判断n是正数 
		if (n > 1000000000 && n < 10) {
			cout << "Wrong";
			return 0;
		}//判断非法情况 
		cout << n;//不改变直接输出 
		return 0;
	}
	else {//n为负数 
		n = -n;//变成正的方便操作 
		if (n > 1000000000 && n < 10) {
			cout << "Wrong";
			return 0;
		}
		int last = n % 10;//取出最后一位 
		int pre = (n % 100 - last) / 10;//取出倒数第二位 
		if (last >= pre) {//哪个大删除哪个 
			cout << -(n / 10);
		}
		else {
			cout << -(n / 100 * 10 + last);
		}
	}

}
