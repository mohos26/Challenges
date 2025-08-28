// https://edabit.com/challenge/BuEQZjDxHfoAbQ5BX
// 07.05.2025
// Easy


#include <vector>
#include <cmath>

using namespace std;

int profit(vector<float> prices, int inv)
{
	return (rint((prices[1] - prices[0]) * inv));
}
