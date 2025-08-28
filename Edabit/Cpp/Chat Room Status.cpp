// https://edabit.com/challenge/afAqP8Whz7cF8bzyE
// 03.05.2025
// Easy


#include <string>
#include <vector>

using namespace std;

string chatroomStatus(vector<string> users)
{
	string	res;
	int len = sizeof(users) / sizeof(users[0]);

	if (len == 0)
		return "no one online";
	else if (len == 1)
		return users[0] + " online";
	else if (len == 2)
		return users[0] + " and " + users[1] + " online";
	return users[0] + ", " + users[1] + " and " + to_string(len -2) + "more online";
}
