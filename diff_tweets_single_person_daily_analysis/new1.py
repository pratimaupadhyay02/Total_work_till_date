import re
str = open('modi50.txt', 'r').read()
#exampleString = "Jessica is 15 years old, and Daniel is 27 years old.Edward is 97 years old, and his grandfather, Oscar, is 102."
#replies = re.findall(r'\d{1,6} replies',str)
#str1 = ''.join(replies)
#replies1 = re.findall(r'\d{1,6}',str1)
retweets = re.findall(r"retweet_count=\d{1,6}|'retweet_count': \d{1,6}",str)
str2 = ''.join(retweets)
retweets2 = re.findall(r'\d{1,6}',str2)
days = re.findall(r"'created_at':\s'[A-Z][a-z][a-z]\s[A-z][a-z][a-z]\s\d{1,2}",str)
#2016', 'favourites_count
dates = re.findall(r"\d{1,4}', 'favourites_count",str)
strdates = ''.join(dates)
year = re.findall(r'\d{1,4}',strdates)
#print year
for x in year:
	year.remove('2009')
print len(retweets2)
#print len(dates)
print len(year)
print year

strday = ''.join(days)
#print strday
date = re.findall(r"[A-Z][a-z][a-z]\s[A-z][a-z][a-z]\s\d{1,2}",strday)
strdate = ''.join(date)
finaldate = re.findall('[A-z][a-z][a-z]\s\d{1,2}',strdate)
strdates = ''.join(finaldate)
#mat=re.match(r'(\d{4})[,]\s(\d{2})[,]\s(\d{2})[,]\s(\d{2})[,]\s(\d{2})[,]\s(\d{2})',str)
#print finaldate
augdays = re.findall(r'Aug\s\d{1,2}',strdates)
juldays = re.findall(r'Jul\s\d{1,2}',strdates)
jundays = re.findall(r'Jun\s\d{1,2}',strdates)
maydays = re.findall(r'May\s\d{1,2}',strdates)
aprdays = re.findall(r'Apr\s\d{1,2}',strdates)
jandays = re.findall(r'Jan\s\d{1,2}',strdates)
febdays = re.findall(r'Feb\s\d{1,2}',strdates)
mardays = re.findall(r'Mar\s\d{1,2}',strdates)
sepdays = re.findall(r'Sep\s\d{1,2}',strdates)
octdays = re.findall(r'Oct\s\d{1,2}',strdates)
novdays = re.findall(r'Nov\s\d{1,2}',strdates)
decdays = re.findall(r'Dec\s\d{1,2}',strdates)
#print aprdays
augdays = ''.join(augdays)
juldays = ''.join(juldays)
jundays = ''.join(jundays)
maydays = ''.join(maydays)
aprdays = ''.join(aprdays)
jandays = ''.join(jandays)
febdays = ''.join(febdays)
mardays = ''.join(mardays)
sepdays = ''.join(sepdays)
octdays = ''.join(octdays)
novdays = ''.join(novdays)
decdays = ''.join(decdays)

#print augdays
augdays1 = re.findall(r'\d{1,2}',augdays)
juldays1 = re.findall(r'\d{1,2}',juldays)
jundays1 = re.findall(r'\d{1,2}',jundays)
maydays1 = re.findall(r'\d{1,2}',maydays)
aprdays1 = re.findall(r'\d{1,2}',aprdays)
jandays1 = re.findall(r'\d{1,2}',jandays)
febdays1 = re.findall(r'\d{1,2}',febdays)
mardays1 = re.findall(r'\d{1,2}',mardays)
sepdays1 = re.findall(r'\d{1,2}',sepdays)
octdays1 = re.findall(r'\d{1,2}',octdays)
novdays1 = re.findall(r'\d{1,2}',novdays)
decdays1 = re.findall(r'\d{1,2}',decdays)
augdates = [int(numeric_string) for numeric_string in augdays1]
juldates = [int(numeric_string) for numeric_string in juldays1]
jundates = [int(numeric_string) for numeric_string in jundays1]
maydates = [int(numeric_string) for numeric_string in maydays1]
aprdates = [int(numeric_string) for numeric_string in aprdays1]
jandates = [int(numeric_string) for numeric_string in jandays1]
febdates = [int(numeric_string) for numeric_string in febdays1]
mardates = [int(numeric_string) for numeric_string in mardays1]
#sepdates = [int(numeric_string) for numeric_string in sepdays1]
#octdates = [int(numeric_string) for numeric_string in octdays1]
#novdates = [int(numeric_string) for numeric_string in novdays1]
#decdates = [int(numeric_string) for numeric_string in decdays1]
print augdates
finaldate1 = []
for i in augdates:
	finaldate.append(16-i)
for i in juldates:
	if(13-i > 0):
		finaldate1.append(30+13-i)
	elif(13-i < 0):
		finaldate1.append(30 - abs(13-i))
for i in jundates:
	if(13-i > 0):
		finaldate1.append(30*2+13-i)
	elif(13-i < 0):
		finaldate1.append(30*2 -abs(13-i))
for i in maydates:
	if(13-i > 0):
		finaldate1.append(30*3+13-i)
	elif(13-i < 0):
		finaldate1.append(30*3-abs(13-i))
for i in aprdates:
	if(13-i > 0):
		finaldate1.append(30*4+13-i)
	elif(13-i < 0):
		finaldate1.append(30*4-abs(13-i))
		finaldate1.append(30 - abs(13-i))
for i in mardates:
	if(13-i > 0):
		finaldate1.append(30*5+13-i)
	elif(13-i < 0):
		finaldate1.append(30*5 -abs(13-i))
for i in febdates:
	if(13-i > 0):
		finaldate1.append(30*6+13-i)
	elif(13-i < 0):
		finaldate1.append(30*6-abs(13-i))
for i in jandates:
	if(13-i > 0):
		finaldate1.append(30*7+13-i)
	elif(13-i < 0):
		finaldate1.append(30*7-abs(13-i))
		
print finaldate1




#print year
#print dmo
#days1 = re.findall(r'\d{1,2}',strday)
#intdays = [int(numeric_string) for numeric_string in days1]
likes = re.findall(r"favorite_count=\d{1,6}|'favorite_count': \d{1,6}",str)
str3 = ''.join(likes)
likes2 = re.findall(r'\d{1,6}',str3)
#time = re.findall(r'\d{1,2} hours ago',str)
#str4 = ''.join(time)
#time2 = re.findall(r'\d{1,2}',str4)
#print days
#print days1
#print intdays
#print retweets
#print days
#print likes
#print retweets2
#print likes2
intretweets = [int(numeric_string) for numeric_string in retweets2]
intlikes = [int(numeric_string) for numeric_string in likes2]
#print intretweets
#print intlikes

'''
intnewdays = [abs(11-i)*24 for i in intdays]
for i in intdays:
	if((11-i)  > 0):
		j = (11-i)*24
		intnewdays.append(j)
	else:
		j = abs(11-31)*24+(31-i)*24
		intnewdays.append(j)

		
#print intnewdays
intnewdays = intnewdays[0:5]
#print intnewdays
#time = re.findall(r'[A-Z][a-z]*\s\d{1,2}',str)
#retweets = re.findall(r'[A-Z][a-z]*',exampleString)
intreplies = [int(numeric_string) for numeric_string in replies1]

inttime = [int(numeric_string) for numeric_string in time2]
inttime=inttime+intnewdays
print inttime
print(intreplies)
print(intretweets)
print(intlikes)

print(inttime)


intreplies1 = intreplies[0:7]
intretweets2=intretweets[0:7]
intlikes2=intlikes[0:7] 
inttime1=inttime[0:7]

print(len(intreplies1))
print(len(intretweets2))
print(len(intlikes2))
print(len(inttime1))
print(intreplies1)
print(intretweets2)
print(intlikes2)
print(inttime1)

import matplotlib.pyplot as plt
x=inttime1
#labels=['','feb','mar','apr']
y=intlikes2
plt.bar(x,y, align='center',color='green',label="No of likes")
#plt.xticks(x, labels)
plt.xlabel('Number of hours ago tweet was posted')
plt.ylabel('Features(Likes, Retweets, Replies')

plt.title('Histogram depicting the relationship between popularity of media features and time')
plt.bar(x,intretweets2,color='yellow',label = "No of retweets")
plt.bar(x,intreplies1,color='blue',label = "No of replies")
plt.show()
import numpy
#a = numpy.array([[1,2],[3,4],[5,6]])
numpy.savetxt("pc.csv",zip(inttime,intreplies,intlikes,intretweets), delimiter=',', header="Time,Replies,Likes,Retweets", comments="")
'''

