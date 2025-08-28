// https://edabit.com/challenge/WJuKWr5mzLGZTjARZ
// 03.05.2025
// Easy


#include <string>

using namespace std;

string nameShuffle(string str)
{
	return str.substr(str.find(" ") + 1) + " " + str.substr(0, str.find(" "));

}