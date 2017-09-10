import matplotlib.pyplot as plt
import numpy as np
time = [2,6,11,11,5,7,100,12,10,120]
replies = [2,12,25,43,3,16,123,44,1,19]
retweets = [10,30,275,51,40,33,807,23,6,133]
likes = [31,29,423,29,97,191,3400,18,31,481]
ranks = [1,2,3,4,5,6,7,8,9,10]
plt.bar(ranks,time, align='center',color='green',label="No of likes")
plt.xlabel('The number at which it appeared on timeline')
plt.ylabel('Green = minutes, Red = Replies, cyan = likes ,yellow = retweets')
plt.show()
#plt.xticks(x, labels)
plt.bar(ranks,replies,align = 'center',color='red')
plt.xlabel('The number at which it appeared on timeline')
plt.ylabel('Green = minutes, Red = Replies, cyan = likes ,yellow = retweets')
plt.show()
plt.bar(ranks,retweets,align = 'center',color = 'yellow')
plt.xlabel('The number at which it appeared on timeline')
plt.ylabel('Green = minutes, Red = Replies, cyan = likes ,yellow = retweets')
plt.show()
plt.bar(ranks,likes,align ='center',color = 'cyan')
plt.xlabel('The number at which it appeared on timeline')
plt.ylabel('Green = minutes, Red = Replies, cyan = likes ,yellow = retweets')
plt.show()
