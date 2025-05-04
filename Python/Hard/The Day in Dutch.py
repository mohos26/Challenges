# https://edabit.com/challenge/eomsubuQLmwASWbMB
# 04.05.2025
# Hard


from datetime import datetime


d = {
	"Monday": "maandag",
	"Tuesday": "dinsdag",
	"Wednesday": "woensdag",
	"Thursday": "donderdag",
	"Friday": "vrijdag",
	"Saturday": "zaterdag",
	"Sunday": "zondag",
}

def weekday_dutch(date):
	return d[datetime(*map(int, date.split()[::-1])).strftime("%A")]
