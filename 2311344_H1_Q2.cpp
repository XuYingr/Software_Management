#include<iostream>
using namespace std;
int main() {
	int n, m, a, b;//n.m.a.b
	cin >> n >> m >> a >> b;//输入 
	if (n < 1 || m < 1 || a>1000 || b>1000) {
		cout << "Wrong";
		return 0;
	}//非法输入 
	int costA = n * a;//计算全部购买单程票 
	int	costB = (n / m) * b + (n % m) * a;//计算混买情况 
	int costC = ((n / m) + 1) * b;//计算当n%m不为0时全部购买优惠票 
	int costD;
	if (costB <= costC) {
		costD = costB;
	}
	else {
		costD = costC;
	}//比较购买优惠票时是混买合算还是全部购买优惠票合算
	if (costA <= costD) {
		cout << costA;
	}
	else {
		cout << costD;
	}//比较 
	return 0;
}


