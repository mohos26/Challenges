#include <string>

using namespace std;

bool isBetween(string first, string last, string word)
{
	return first < word && word < last;
}
