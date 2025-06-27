# https://edabit.com/challenge/NYEaXXCnSj9jteNWA
# 03.06.2025
# hard


def ave_spd(up_time, up_spd, down_spd):
	up_spd /= 60
	down_spd /= 60
	distance = up_spd * up_time
	down_time = distance * down_spd**-1
	total_time = up_time + down_time
	return int(((up_time * up_spd + down_time * down_spd) / total_time) * 60)

# i5tizal
def ave_spd2(up_time, up_spd, down_spd):
	return int(((up_time * (up_spd / 60) + (((up_spd / 60) * up_time) * (down_spd / 60)**-1) * (down_spd / 60)) / (up_time + (((up_spd / 60) * up_time) * (down_spd / 60)**-1))) * 60)
