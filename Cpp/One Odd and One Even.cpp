// https://edabit.com/challenge/NJjHSoaf9MbrTMGkf
// 05.05.2025
// Easy


bool oneOddOneEven(int n)
{
	int first_part;
	int second_part;

	first_part = n / 10;
	second_part = n % 10;

	if (first_part % 2 + second_part % 2 == 1)
		return true;
	return false;
}
