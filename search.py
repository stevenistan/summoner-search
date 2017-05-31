import requests

def requestSummonerData(region, summonerName, APIKey):    
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v1.4/summoner/by-name/" + summonerName + "?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()

def requestRankedData(region, ID, APIKey):
    URL = "https://" + region + ".api.pvp.net/api/lol/" + region + "/v2.5/league/by-summoner/" + ID + "/entry?api_key=" + APIKey
    response = requests.get(URL)
    return response.json()
    
def main():
    region = 'na'
    summonerName = (str)(input('Type your Summoner Name here: '))
    summonerName = summonerName.lower().replace(" ", "")
    APIKey = 'RGAPI-1b438410-0037-4a9f-9989-d9ed18238786'

    responseJSON = requestSummonerData(region, summonerName, APIKey)
    
    ID = responseJSON[summonerName]['id']
    ID = str(ID)
    print(ID)
    name = responseJSON[summonerName]['name']
    responseJSON2 = requestRankedData(region, ID, APIKey)
    print(name + " is rank: "
          + responseJSON2[ID][0]['tier'] + " "
          + responseJSON2[ID][0]['entries'][0]['division'] + " "
          + str(responseJSON2[ID][0]['entries'][0]['leaguePoints'])
          + " LP")

if __name__ == "__main__":
    main()
