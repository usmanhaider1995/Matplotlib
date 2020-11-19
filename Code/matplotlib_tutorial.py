import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# change figure size
plt.figure(figsize=(5,3) ,dpi=100)


# GAS PRICE DATA



# Basic graph
x=[1,2,3,4]
y=[9,8,7,6]

plt.plot(x,y, color='orange' ,linestyle='-',label='2-x', linewidth=4, marker='^', markersize=20, markeredgecolor='blue')
# Short hand notation
plt.plot(x,y,'b.-',label='2-x')

#Line number 2

x2= np.arange(0,4.5,0.5)
plt.plot(x2[:6],x2[:6]**2, 'r',label='x^2')
plt.plot(x2[5:],x2[5:]**2, 'b--')

# Adding title to graph
plt.title('Our first Graph!',fontdict={'fontname': 'Comic Sans MS'})
plt.xlabel('Snowfall',fontdict={'fontname': 'Comic Sans MS'})
plt.ylabel('Rainfall',fontdict={'fontname': 'Comic Sans MS'})

plt.xticks([0,1,2,3,4])
plt.yticks([0,9,8,7,6])
# saving figure
plt.savefig('mygraph.png')

# Bar chart
labels= ['A','B','C']
values= [1,4,2]
bar= plt.bar(labels,values, label='Bar')
patters = ['/','o','*']

for bars in bar:
    bars.set_hatch(patters.pop(0))

bar[0].set_hatch('/')   # see documentation
bar[1].set_hatch('o')
bar[2].set_hatch('*')



# Real World Examples
# Line graph
plt.title('Gas prices',fontdict={'fontweight':'bold','fontsize':22})
gas=pd.read_csv('gas_prices.csv')
print(gas)
plt.plot(gas.Year, gas.USA ,'b.-', label='USA graph')
plt.plot(gas.Year, gas.Canada,'r*--' , label= 'Canada graph' )
plt.plot(gas.Year, gas['South Korea'],'g^-', label= 'Korea graph' )
plt.plot(gas.Year, gas.France,'r.--' , color='orange', label= 'France graph' )
plt.xlabel('Year')
plt.ylabel('Gas price')
plt.xticks(gas.Year[::5].tolist()+[2012])
plt.savefig('Gas_price_figure.png', dpi=100)
#for country in gas:
 #   if country !='Year':
  #      plt.plot(gas.Year, gas[country], label=country)



# FIFA DATASET
plt.style.use('ggplot')

fifa= pd.read_csv('fifa_data.csv')

#print(fifa.columns)
#bins= [ 40,50,60,70,80,90,100]
# HISTOGRAM
#plt.xlabel('Skill Level')
#plt.ylabel('Number of players')
#plt.title('Distribution of player skills in FIFA 2018')

#plt.hist(fifa.Overall, bins=bins,color='#c0d411')
#plt.xticks(bins)

# PIE Chart

left = fifa.loc[fifa['Preferred Foot'] == 'Left'].count()[0]
#print(left)
right = fifa.loc[fifa['Preferred Foot'] == 'Right'].count()[0]
#print(right)
labels= ['left','right']
colors = ['#fcba03','#e61291']
#plt.pie([left, right],labels=labels, colors=colors, autopct='%.2f %%')
# autopct shows percentage on graph

plt.title('Foot Prefernce of FIFA players (in lbs)')

# PIE chart in details
#print(fifa.Weight[0:20])
# Remove lbs from weights
fifa.Weight = [int(x.strip('lbs')) if type(x) == str else x for x in fifa.Weight]
print(fifa.Weight[0:20])

light = fifa.loc[fifa.Weight < 125].count()[0]
#print(light)
light_medium = fifa.loc[(fifa.Weight >=125) & (fifa.Weight <150)].count()[0]
medium= fifa.loc[(fifa.Weight >= 150) & (fifa.Weight < 175)].count()[0]
medium_heavy = fifa.loc[(fifa.Weight >=175) & (fifa.Weight <200)].count()[0]
heavy = fifa.loc[fifa.Weight >=200].count()[0]
explode = (.3,.1,0,0,.3)
# explode your graph
weights = [light,light_medium,medium,medium_heavy,heavy]
labels= ['light','light_medium','medium','medium_heavy','heavy']
plt.pie(weights,labels=labels,autopct='% 0.1f', explode=explode)
plt.savefig('Player_weights.png',dpi=100)
 

# BOX & WHISKER PLOT
#plt.style.use('ggplot')

barcelona = fifa.loc[fifa.Club == 'FC Barcelona']['Overall']
madrid = fifa.loc[fifa.Club == 'Real Madrid']['Overall']
revs = fifa.loc[fifa.Club== 'New England Revolution']['Overall']
labels = ['FC Barlcelona', 'Real Madrid','NE Revolution']

plt.boxplot([barcelona,madrid,revs],labels=labels, patch_artist=True , medianprops={'linewidth':5})

plt.title('Soccer Team Comparision')
plt.ylabel('Overall rating')






















































#plt.legend()
plt.show()