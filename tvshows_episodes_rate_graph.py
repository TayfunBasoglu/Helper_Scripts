import requests
from bs4 import BeautifulSoup
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objs as go


take_link = input("Enter show's imdb link : ")
show_id = take_link.split("/")[4]

def total_season():
    url = "https://www.imdb.com/title/"+show_id+"/episodes"
    headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}
    source = BeautifulSoup(requests.get(url,headers=headers).content,"lxml")

    seasons = source.find("select", {"id": "bySeason"})
    season_sum = len(seasons.find_all("option"))

    show_name = source.find("h3", {"itemprop": "name"})
    show_name = show_name.text[:show_name.text.find("(")].strip()
    return(season_sum,show_name)


def episodes_info(season):
    df = pd.DataFrame(columns=["Name","Date","Rate","Vote","Season"])
    for i in range(1,season+1):
        print("Season",i,"...")
        url = "https://www.imdb.com/title/"+show_id+"/episodes?season="+str(i)
        headers = {"User-Agent": "Mozilla/5.0", "accept-language": "en-US,en"}
        source = BeautifulSoup(requests.get(url,headers=headers).content,"lxml")
        episodes = source.find_all("div", {"class": "info"})
        for episode in episodes:
            episode_name = episode.find("strong").text
            if "#" in episode_name:
                continue
            episode_date = episode.find("div", {"class": "airdate"}).text.strip()
            episode_rate = episode.find("span", {"class": "ipl-rating-star__rating"}).text
            episode_votes = episode.find("span", {"class": "ipl-rating-star__total-votes"}).text[1:-1]
            episode_df = pd.DataFrame([[episode_name,episode_date,episode_rate,episode_votes,i]],columns=["Name","Date","Rate","Vote","Season"])
            df = pd.concat([df,episode_df],ignore_index=True)
    return(df)

season_count = total_season()[0]
episode_frame = episodes_info(season_count)
episode_frame["Episode"] = range(1, episode_frame.shape[0]+1)
episode_frame["Rate"] = episode_frame["Rate"].astype("float")

fig = px.scatter(episode_frame,x="Episode", y="Rate", color="Season",hover_data={'Name':True,'Date':True,'Episode':True,'Season':True,'Rate':True,'Vote':True},symbol="Season",template="plotly_dark", text="Rate", title=total_season()[1]+" - Total episode : "+str(episode_frame.shape[0]))
fig.update_traces(marker=dict(size=11),textposition='top center')

js = '''document.body.style.backgroundColor = "#111111";'''
fig.show(renderer="browser",post_script=[js])
