import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('ad_clicks.csv')
print(ad_clicks.head())
ad_clicks.groupby('utm_source').user_id.count().reset_index()
ad_clicks['is_click']= ~ad_clicks.ad_click_timestamp.isnull()

clicks_by_source = ad_clicks.groupby(['utm_source','is_click']).user_id.count().reset_index()
clicks_pivot = clicks_by_source.pivot(
columns='is_click',
index='utm_source',
values='user_id').reset_index()
clicks_pivot['percent_clicked'] = \
   clicks_pivot[True] / \
   (clicks_pivot[True] + 
    clicks_pivot[False])
ad_clicks.groupby('experimental_group').user_id.count().reset_index()
ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
a_clicks = ad_clicks[ad_clicks.experimental_group == 'A']
a_clicks = ad_clicks[ad_clicks.experimental_group == 'B']

AB_Clicks = ad_clicks.groupby(['is_click','day']).user_id.count().reset_index()

AB_Click_Pivot = AB_Clicks.pivot(
columns='is_click',
index='day',
values='user_id').reset_index()
AB_Click_Pivot['percent_clicked'] = \
   AB_Click_Pivot[True] / \
   (AB_Click_Pivot[True] + 
    AB_Click_Pivot[False])
print(AB_Click_Pivot)