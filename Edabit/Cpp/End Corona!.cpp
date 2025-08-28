// https://edabit.com/challenge/i7AmWM4SHE6GBAEoT
// 05.05.2025
// Easy


#include <cmath>

int endCorona(int recovers, int newCases, int activeCases)
{
	return activeCases / (recovers - newCases) + !!(activeCases % (recovers - newCases));
}

int endCorona2(int recovers, int newCases, int activeCases)
{
	return std::ceil((double)activeCases / (recovers - newCases));
}
