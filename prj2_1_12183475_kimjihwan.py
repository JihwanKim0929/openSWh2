#12183475 김지환
#project 2-1
print('12183475 김지환')
print('project 2-1')
print()
import numpy as np
import pandas as pd
kbo_data=pd.read_csv('2019_kbo_for_kaggle_v2.csv')


#1) Print the top 10 players in hits (안타, H), batting average (타율, avg), 
#homerun (홈런, HR), and on-base percentage (출루율, OBP) for each year 
#from 2015 to 2018. (15 points)
print('1)')
print()
kbo_tophit=kbo_data[['batter_name','H','p_year']].sort_values(by='H',ascending=False)
kbo_topavg=kbo_data[['batter_name','avg','p_year']].sort_values(by='avg',ascending=False)
kbo_tophomerun=kbo_data[['batter_name','HR','p_year']].sort_values(by='HR',ascending=False)
kbo_topobp=kbo_data[['batter_name','OBP','p_year']].sort_values(by='OBP',ascending=False)
print('안타 top10')
print()
for i in range(2015,2019):
    print(i,'년')
    print(kbo_tophit[kbo_tophit['p_year']==i].head(10))
    print()
print()
print('타율 top10')
print()
for i in range(2015,2019):
    print(i,'년')
    print(kbo_topavg[kbo_topavg['p_year']==i].head(10))
    print()
print()
print('홈런 top10')
print()
for i in range(2015,2019):
    print(i,'년')
    print(kbo_tophomerun[kbo_tophomerun['p_year']==i].head(10))
    print()
print()    
print('출루율 top10')
print()
for i in range(2015,2019):
    print(i,'년')
    print(kbo_topobp[kbo_topobp['p_year']==i].head(10))
    print()
print()

#2) Print the player with the highest war 
#(승리 기여도) by position (cp) in 2018. (15 points)
print('2)')

kbo_2018_topwar=kbo_data[kbo_data['p_year']==2018][['cp','batter_name','war','p_year']].sort_values(by='war',ascending=False)
position_list=['포수','1루수','2루수','3루수','유격수','좌익수','중견수','우익수']
print('2018년 각 포지션 별 최고 승리기여도 선수')
print()
for i in position_list:
    print(i)
    print(kbo_2018_topwar[kbo_2018_topwar['cp']==i].head(1))
    print()

print()
#3) Among R (득점), H (안타), HR (홈런), RBI (타점), SB (도루), war (승리 기여도), 
#avg (타율), OBP (출루율), and SLG (장타율), which has the 
#highest correlation with salary (연봉)? (15 points)
kbo_salary_corr=kbo_data[['R','H','HR','RBI','SB','war','avg','OBP','SLG','salary']]
print('연봉과의 상관계수')
print(kbo_salary_corr.corrwith(kbo_salary_corr.salary).sort_values(ascending=False))
print()
print('연봉과 상관계수가 가장 높은 것')
print(kbo_salary_corr.corrwith(kbo_salary_corr.salary).sort_values(ascending=False).index[1])
#salary 자신과의 상관계수는 항상1이므로 [0]이 아닌 [1]의 인덱스가 가장 높은 상관계수를 가짐 , RBI가 salary와 가장 높은 상관이 있음.
