import requests

def requestSummonerData(region, summonerName, APIKey):    
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    print(URL)
    #requests.get is a function given to us my our import "requests". It basically goes to the URL we made and gives us back a JSON.
    response = requests.get(URL)
    #Here I return the JSON we just got.
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    print(URL)
    response = requests.get(URL)
    return response.json()
    
def main():
    region = 'NA'
    summonerName = (str)(input('Type your Summoner Name here and DO NOT INCLUDE ANY SPACES: '))
    APIKey = 'RGAPI-1b438410-0037-4a9f-9989-d9ed18238786'

    #I send these three pieces off to my requestData function which will create the URL and give me back a JSON that has the ID for that specific summoner.
    #Once again, what requestData returns is a JSON.
    responseJSON = requestSummonerData(region, summonerName, APIKey)
    
    ID = responseJSON[summonerName]['id']
    ID = str(ID)
    print(ID)
    responseJSON2 = requestRankedData(region, ID, APIKey)
    print(summonerName + " is rank: "
          + responseJSON2[ID][0]['tier'] + " "
          + responseJSON2[ID][0]['entries'][0]['division'] + " "
          + str(responseJSON2[ID][0]['entries'][0]['leaguePoints']))

if __name__ == "__main__":
    main()
