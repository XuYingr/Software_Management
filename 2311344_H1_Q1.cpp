#include<iostream>
#include<vector>
#include<unordered_map>
#include<string>
#include<sstream>
#include<algorithm>
#include<limits>
using namespace std;

string trim(const string& str) {
	size_t first = str.find_first_not_of(" \t\r\n");
	if (string::npos == first) {
		return str;
	}
	size_t last = str.find_last_not_of(" \t\r\n");
	return str.substr(first, (last - first + 1));
}

std::unordered_map<string, vector<string>> parsePreferences(const vector<string>& lines) {//定义一个parsePreferences,输入字符串数组，返回unordered_map 
	unordered_map<string, vector<string>>preferences;
	for (const auto& line : lines) {//遍历输入的每一行偏好列表 
		stringstream ss(line);//将字符串转换为字符串流，便于按分隔符解析
		string name;
		getline(ss, name, ':'); //将字符串里的名字以：为分隔符，存储到name里面
		name = trim(name);
		string prefs;
		getline(ss, prefs);//剩余的存储到prefs里面
		stringstream ss2(prefs);
		string pref;
		while (getline(ss2, pref, '>')) {//分解剩下的偏好项并加入vector中 
			preferences[name].push_back(trim(pref));
		}
	}
	return preferences;
}
vector<pair<string, string>> findStableMatching(const std::unordered_map<string, vector<string>>& malePrefs, const std::unordered_map<string, vector<string>>& femalePrefs) {//返回匹配结果，每个匹配是一个对，存储键对的动态数组 
	std::unordered_map<string, string> engagement;//当前匹配,键为女性名字
	std::unordered_map<string, int> maleProposalIndex;//每个男性的求婚进度
	std::unordered_map<string, int> maleToIndex; // Map to store index of each male in the males vector

	vector<string>males;
	//初始化男女性列表 
	int index = 0;
	for (const auto& entry : malePrefs) {
		males.push_back(entry.first);
		maleProposalIndex[entry.first] = 0;
		maleToIndex[entry.first] = index++;
	}

    // Precompute female preference rankings for O(1) lookup
    std::unordered_map<string, std::unordered_map<string, int>> femalePrefRank;
    for (const auto& entry : femalePrefs) {
        const string& female = entry.first;
        const vector<string>& prefs = entry.second;
        for (int i = 0; i < prefs.size(); ++i) {
            femalePrefRank[female][prefs[i]] = i;
        }
    }

	//所有男性未匹配 
	vector<bool>freeMale(males.size(), true);
	int freeCount = males.size();
	while (freeCount > 0) {//只要还有自由男人就循环 
		for (int i = 0; i < males.size(); i++) {
			if (freeMale[i]) {
				string male = males[i];
				string female = malePrefs.at(male)[maleProposalIndex[male]];//返回当前男人的偏好列表里找到当前男性求婚进度对应的女性
				maleProposalIndex[male]++;
				if (engagement.find(female) == engagement.end()) {
					//到迭代器末尾，没找到对象 
					engagement[female] = male;
					freeMale[i] = false;
					freeCount--;
				}
				else {//有对象比较 
					string currentMale = engagement[female];
                    // Use precomputed ranks for O(1) comparison
                    int currentMaleIndex = femalePrefRank[female][currentMale];
                    int proposingMaleIndex = femalePrefRank[female][male];
					
					if (proposingMaleIndex < currentMaleIndex) {
						engagement[female] = male;
						freeMale[i] = false;
						//freeMale[find(males.begin(), males.end(), currentMale) - males.begin()] = true;//释放当前男生 
						freeMale[maleToIndex[currentMale]] = true;
                        // freeCount++; // REMOVER: This was incorrect. The number of free men doesn't change here.
                        // One male (i) gets engaged (-1 free), and one male (currentMale) gets freed (+1 free).
                        // Net change is 0. So freeCount should NOT be incremented.
					}
					// IMPORTANT FIX: If the proposing male is rejected (proposingMaleIndex > currentMaleIndex),
					// he remains free. We do NOT need to do anything here because freeMale[i] is already true.
				}
			}
		}
	}
	vector<pair<string, string>> matches;
	for (const auto& entry : engagement) {
		matches.push_back({ entry.second,entry.first });
	}
	sort(matches.begin(), matches.end());
	return matches;
}
int main() {
	int n;
	cin >> n;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');//输入人数 
	vector<string> maleLines(n);
	vector<string> femaleLines(n);//两个动态数组，分别记录n个男女生信息 
	for (int i = 0; i < n; i++) {
		getline(cin, maleLines[i]);
	}
	for (int i = 0; i < n; i++) {
		getline(cin, femaleLines[i]);
	}
	auto malePrefs = parsePreferences(maleLines);
	auto femalePrefs = parsePreferences(femaleLines);//调用函数解析出男女生姓名和偏好列表，类型为unordered——map 
	vector<pair<string, string>> matches = findStableMatching(malePrefs, femalePrefs);
	for (const auto& match : matches) {
		cout << "(" << match.first << "," << match.second << ")" << endl;
	}
	return 0;

}
