// https://edabit.com/challenge/7iT6DbY3GsHnLBPq4
// 05.05.2025
// Easy


#include <vector>

using namespace std;

vector<int> noOdds(vector<int> arr)
{
	vector<int>	res;

	for (int n: arr)
		if (!(n % 2))
			res.push_back(n);
	return res;
}
