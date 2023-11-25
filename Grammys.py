import pandas as pd
import numpy as np
import plotly.express as px
pd.set_option('display.float_format', lambda x: '%.2f' % x)
full_data = pd.read_csv("datasets/grammy_live_web_analytics.csv")
rec_academy = pd.read_csv("datasets/ra_live_web_analytics.csv")
full_data.head()
rec_academy.head()
px.line(full_data, x="date", y="visitors")
full_data.groupby('awards_night').mean(numeric_only = True)
combined_site = full_data[full_data['date'] < '2022-02-01']
grammys = full_data[full_data['date'] >= '2022-02-01']
combined_site = combined_site.copy()
grammys = grammys.copy()
rec_academy = rec_academy.copy()
combined_site.shape
frames = [combined_site, grammys, rec_academy]
for frame in frames:
    frame['pages_per_session'] = frame['pageviews'] / frame['sessions']
px.line(combined_site, x="date", y="pages_per_session")
px.line(grammys, x="date", y="pages_per_session")
px.line(rec_academy, x="date", y="pages_per_session")
def bounce_rate(dataframe):
    '''
    Calculates the bounce rate for visitors on the website.
    input: dataframe with bounced_sessions and sessions columns
    output: numeric value from bounce rate
    '''
    sum_bounced = dataframe['bounced_sessions'].sum()
    sum_sessions = dataframe['sessions'].sum()
    return 100 * (sum_bounced / sum_sessions)
frame_name_list = ["Combined", "Grammys", "Recording Academy"]
bounce_rate_list = []
for frame in frames:
    bounce_rate_list.append(bounce_rate(frame))
for frame_name, bounce_rate_value in zip(frame_name_list, bounce_rate_list):
    print(f'The bounce rate for the {frame_name} website is {bounce_rate_value:0.2f}')
sd_cs = combined_site['avg_session_duration_secs'].mean()
sd_grammys = grammys['avg_session_duration_secs'].mean()
sd_tra = rec_academy['avg_session_duration_secs'].mean()
print(f"The mean session duration in seconds is {sd_cs:0.2f} for the combined site, {sd_grammys:0.2f} for the Grammys and {sd_tra:0.2f} for the Recording Academy.")
age_grammys = pd.read_csv("datasets/grammys_age_demographics.csv")
age_tra = pd.read_csv("datasets/tra_age_demographics.csv")
age_grammys.head()
age_grammys['website'] = 'Grammys'
age_tra['website'] = 'Recording Academy'
age_grammys.head()