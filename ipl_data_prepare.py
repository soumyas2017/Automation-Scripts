from bs4 import BeautifulSoup
import requests
import re
if __name__ == '__main__':
    # url = "https://en.wikipedia.org/wiki/2008_Indian_Premier_League"
    # url = 'https://en.wikipedia.org/wiki/2017_Indian_Premier_League'
    # url = 'https://en.wikipedia.org/wiki/2018_Indian_Premier_League'
    url = 'https://en.wikipedia.org/wiki/2012_Indian_Premier_League'
    r = requests.get(url)
    data  = r.text
    soup = BeautifulSoup(data,'lxml')
    soup.prettify()
    data = list()
    urls = list()
    player_of_match =""
    pom_team = ""
    c=0
    # Fetching Scorecard from above url
    for links in soup.find_all('a',text='Scorecard'):
        c +=1 # Just a counter for no of matches in a season
        data = str(links).split(" ") # Splitting the scorecard hyperlink, as we need the text under <a> href tag
        urls = str(data[3]).split('\"') # The third part is our scorecard hyperlink for each matches in a season
        urlss = urls[1].replace("/game/","/scorecard/") # Replacing the url's game to scorecard, as wiki fetches the game
        open_site = requests.get(urlss) # We now open the webpage through hyperlink for scapping content
        site_data = open_site.text # we get all the data as form of text from the website
        soup_class = BeautifulSoup(site_data,'lxml') # we now use beautifulsoup function to parse on the text returned
        # We start to get the text from the tags 
        for datum in soup_class.find_all('div',attrs={'class': 'cscore_info-overview','data-reactid':'20'}):
            # Here we are fetching the two teams for the current match
            for team1 in soup_class.find_all('span',attrs={'class': 'cscore_name cscore_name--long','data-reactid':'28'}):
                team1 = team1.text
            for team2 in soup_class.find_all('span',attrs={'class': 'cscore_name cscore_name--long','data-reactid':'37'}):
                team2 = team2.text
            # Getting result
            for result in soup_class.find_all('span',attrs={'class': 'cscore_notes_game'}):
                result = result.text
            # Fetching Player of the match
            for pom in soup_class.find_all('a',attrs={'class': 'gp__cricket__player-match__player__detail__link','data-reactid':'53'}):
                if '&amp;lpos=cricket:game:scorecard:player' in str(pom):
                    # For older ipl seasons this works
                    pom = str(pom).split("&amp;lpos=cricket:game:scorecard:player\">")
                else:
                    # For recent season this works
                    pom = str(pom).split("&amp;lpos=cricket:game:game:player\">")
                    pom_player = str(pom[1]).split("<span>")
                    player_of_match = pom_player[0]
                    pom_team = str(pom_player[1]).split("</span>")[0]
                # Fetching team1 score. This team is the one who batted first.
            for find_team1_score in soup_class.find_all('div',attrs={'class': 'cscore_score','data-reactid':'31'}):
                team1_score = find_team1_score.text
                # Fetching team2 score. This team bats second.
            for find_team2_score in soup_class.find_all('div',attrs={'class': 'cscore_score','data-reactid':'40'}):
                team2_score = find_team2_score.text
            # Finding Field Umpires for the match
            for find_field_umpires in soup_class.find_all('h4',text='Umpires'):
                field_umpires = str(find_field_umpires).split('\"')[1]
                field_umpires = int(field_umpires)
                field_umpires += 1
                for single_umpire in soup_class.find_all('div',attrs={'class':'match-detail--right','data-reactid':str(field_umpires)}):
                        umpire = single_umpire.text
                        # Getting the Umpire Names properly
                try:
                    umpire = umpire.split(" ")
                    if len(umpire[0]) == 2:
                        parts_0 = umpire[0].split()
                    else:
                        parts_0 = re.findall('[A-Z][^A-Z]*',umpire[0])
                    parts_1 = re.findall('[A-Z][^A-Z]*',umpire[1])
                    if len(parts_0) == 2:
                        print ('Field Umpires - > {},{} {}'.format(parts_0[0],parts_0[1],umpire[1]))
                    elif len(parts_1) == 2 and len(umpire)>=3:
                        print ('Field Umpires - > {} {},{} {}'.format(umpire[0],parts_1[0],parts_1[1],umpire[2]))
                    else:
                        if (parts_1[1] == 'G'):
                            parts_1[1] = str(parts_1[1]).replace("G","GA Pratapkumar")
                            print ('Field Umpires - > {} {},{}'.format(umpire[0],parts_1[0],parts_1[1]))
                        else:
                            print ('Field Umpires - > {} {},{}'.format(umpire[0],parts_1[0],parts_1[1]))
                except(IndexError):
                    print ('Field Umpires Ex - > {} {},{}'.format(umpire[0],parts_0[0],parts_0[1]))
            # Finding TV Umpires
            for tv_umpire in soup_class.find_all('h4',text='TV Umpires'):
                tv_umpire = str(tv_umpire).split('\"')[1]
                tv_umpire = int(tv_umpire)
                tv_umpire += 1
                for tv_single_umpire in soup_class.find_all('div',attrs={'class':'match-detail--right','data-reactid':str(tv_umpire)}):
                    tv_umpire = tv_single_umpire.text
                    print ("TV Umpire -> {}" .format(tv_umpire))
            # Finding Reserve upmires
            for reserve_umpire in soup_class.find_all('h4',text='Reserve Umpire'):
                reserve_umpire = str(reserve_umpire).split('\"')[1]
                reserve_umpire = int(reserve_umpire)
                reserve_umpire += 1
                for reserve_single_umpire in soup_class.find_all('div',attrs={'class':'match-detail--right','data-reactid':str(reserve_umpire)}):
                    reserve_umpire = reserve_single_umpire.text
                    print ("Reserve Umpire -> {}" .format(reserve_umpire))
            # Finding Match Referee    
            for referee in soup_class.find_all('h4',text='Match Referee'):
                referee = str(referee).split('\"')[1]
                referee = int(referee)
                referee += 1
                for match_referee in soup_class.find_all('div',attrs={'class':'match-detail--right','data-reactid':str(referee)}):
                    referee = match_referee.text
                    print ("Match Referee -> {}" .format(referee))
            # Finding Toss Report
            for toss in soup_class.find_all('h4',text='Toss'):
                toss_report = str(toss).split('\"')[1]
                toss_report = int(toss_report)
                toss_report += 2
                for toss_data in soup_class.find_all('span',attrs={'data-reactid':str(toss_report)}):
                    datum = str(datum.text)
                    contents = datum.split(",")
                    venue = str(contents[1])
                    # Venue
                    venue = venue.split(" ")[5]
                    # Match Date and type
                    date = contents[2]
                    # Getting Season        
                    season = str(contents[2]).split(" ")[3]    
                    print("{} is played between {},scored {} and {} scored {} at {} on {} and the result is {} and pom is {} from {}, and toss report is {} and season is {}".format(contents[0],team1,team1_score,team2,team2_score,venue,date,result,player_of_match,pom_team,toss_data.text,season))
    print (c) # Total Matches of the season
