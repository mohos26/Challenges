// https://edabit.com/challenge/K7LELsNXXqpGd3yYW
// Very Easy
// 21.04.2025


#include <vector>
#include <string>

std::vector<int> hashPlusCount(std::string str) {
	int h = 0, p = 0;

	for (int i = 0; i < str.length(); i++)
	{
		if (str[i] == '#')
		h++;
		else
		p++;
	}
	return {h, p};
}
