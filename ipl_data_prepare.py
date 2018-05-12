from bs4 import BeautifulSoup
import requests
import re
if __name__ == '__main__':
    url = "https://en.wikipedia.org/wiki/2008_Indian_Premier_League"
    # url = 'https://en.wikipedia.org/wiki/2017_Indian_Premier_League'
    # url = 'https://en.wikipedia.org/wiki/2018_Indian_Premier_League'
    r = requests.get(url)
    data  = r.text
    soup = BeautifulSoup(data,'lxml')
    soup.prettify()
    data = list()
    urls = list()
    alphabets = [chr(n) for n in range(65,90)]
    # print (alphabets)
    # with open("e:\\wiki_ipl_data.dat","w") as file:
    #     file.write(str(soup.encode('utf-8')))
    #     print("Wrote Successfully")
    #print (soup)
    c=0
    # for links in soup.find_all('a',class_='external text'):
    for links in soup.find_all('a',text='Scorecard'):
        # if links.string == "Scorecard":
            c +=1
            data = str(links).split(" ")
            urls = str(data[3]).split('\"')
            urlss = urls[1].replace("/game/","/scorecard/")
            open_site = requests.get(urlss)
            site_data = open_site.text
            soup_class = BeautifulSoup(site_data,'lxml')
            # print (play_details(site_data))
            # print (urlss)
            # exit(0)
            # play_details(urls[1])
            for datum in soup_class.find_all('div',attrs={'class': 'cscore_info-overview','data-reactid':'20'}):
                for team1 in soup_class.find_all('span',attrs={'class': 'cscore_name cscore_name--long','data-reactid':'28'}):
                    team1 = team1.text
                for team2 in soup_class.find_all('span',attrs={'class': 'cscore_name cscore_name--long','data-reactid':'37'}):
                    team2 = team2.text
                for result in soup_class.find_all('span',attrs={'class': 'cscore_notes_game'}):
                    result = result.text
                for pom in soup_class.find_all('a',attrs={'class': 'gp__cricket__player-match__player__detail__link','data-reactid':'53'}):
                    # pom = pom.replace("<span>","from")
                    # pom = pom.replace("</span","")
                    # pom = BeautifulSoup(str(pom),'lxml')
                    # pom = pom.get_text()
                    if '&amp;lpos=cricket:game:scorecard:player' in str(pom):
                        pom = str(pom).split("&amp;lpos=cricket:game:scorecard:player\">")
                    else:
                        pom = str(pom).split("&amp;lpos=cricket:game:game:player\">")
                    # print (';lpos=cricket:game:scorecard:player' in str(pom))
                    pom_player = str(pom[1]).split("<span>")
                    player_of_match = pom_player[0]
                    pom_team = str(pom_player[1]).split("</span>")[0]
                    # print(pom_team)
                    #print ("{},{}".format(player_of_match,pom_team))
                for find_team1_score in soup_class.find_all('div',attrs={'class': 'cscore_score','data-reactid':'31'}):
                    team1_score = find_team1_score.text
                    # print (team1_score)
                for find_team2_score in soup_class.find_all('div',attrs={'class': 'cscore_score','data-reactid':'40'}):
                    team2_score = find_team2_score.text
                    # print (team2_score)
                for find_team1_player in soup_class.find_all('div',attrs={'class': 'player-name'}):
                    team1_player = find_team1_player.text
                    # print (team1_player)
                    # print (play_details(soup_class))
    #             for all_data in soup_class.find_all("div",attrs={"class":"cell batsmen"}):
    # # for all_data in soup.find_all("div",attrs={"class":"cell batsmen"}):cell commentary
    #                 for a in all_data.find_all('a'):
    #     # print (all_data.text)
    #                     reactid = int(a.get('data-reactid'))
    #                     get_out_status = reactid + 1
    #                     for get_player_status in soup_class.find_all("div",attrs={'class':'cell commentary','data-reactid':get_out_status}):
    #                         print ("{},{}".format(all_data.text,get_player_status.text))
                for find_field_umpires in soup_class.find_all('h4',text='Umpires'):
                    # print (find_field_umpires)
                    field_umpires = str(find_field_umpires).split('\"')[1]
                    field_umpires = int(field_umpires)
                    field_umpires += 1
                    # print(field_umpires)
                    for single_umpire in soup_class.find_all('div',attrs={'class':'match-detail--right','data-reactid':str(field_umpires)}):
                        umpire = single_umpire.text
                        # print (umpire)
                        try:
                            umpire = umpire.split(" ")
                            print (umpire)
                            # test = ",".join(umpire[0])
                            # test = test.split()
                            # print(test)
                            # if re.findall('[A-Z][^A-Z]*',umpire[0]):
                            #     print ("True")
                            # else:
                            #     print("False")
                            # print(type(test))
                            if len(umpire[0]) == 2:
                                parts_0 = umpire[0].split()
                                print (parts_0)
                            else:
                                parts_0 = re.findall('[A-Z][^A-Z]*',umpire[0])
                                print (parts_0)
                            parts_1 = re.findall('[A-Z][^A-Z]*',umpire[1])
                            print (parts_1)
                            if len(parts_0) == 2:
                                print ('{},{} {}'.format(parts_0[0],parts_0[1],umpire[1]))
                            elif len(parts_1) == 2 and len(umpire)>=3:
                                print ('{} {},{} {}'.format(umpire[0],parts_1[0],parts_1[1],umpire[2]))
                            else:
                                print ('{} {},{}'.format(umpire[0],parts_1[0],parts_1[1]))
                            # print (umpire[0])
                            # print (parts[0])
                            # print (parts[1])
                            # print (umpire[2])
                            
                        except(IndexError):
                            print ('{} {},{}'.format(umpire[0],parts_0[0],parts_0[1]))
                        # single_umpire = datum.split(",")
                        # single_umpire = str(contents[1])
                for tv_umpire in soup_class.find_all('h4',text='TV Umpires'):
                    tv_umpire = str(tv_umpire).split('\"')[1]
                    tv_umpire = int(tv_umpire)
                    tv_umpire += 1
                    print(tv_umpire)
                    for tv_single_umpire in soup_class.find_all('div',attrs={'class':'match-detail--right','data-reactid':str(tv_umpire)}):
                        tv_umpire = tv_single_umpire.text
                        print (tv_umpire)
                    # tv_umpire = "No Umpires"
                for find_field_umpires in soup_class.find_all('h4',text='Umpires'):
                    field_umpires = str(find_field_umpires).split('\"')[1]
                    field_umpires = int(field_umpires)
                    field_umpires += 1
                    print(field_umpires)
                for toss in soup_class.find_all('h4',text='Toss'):
                    toss_report = str(toss).split('\"')[1]
                    toss_report = int(toss_report)
                    toss_report += 2
                    # print (type(toss_report))
                    for toss_data in soup_class.find_all('span',attrs={'data-reactid':str(toss_report)}):
                        # print (toss_data.text)
                        datum = str(datum.text)
                        contents = datum.split(",")
                        venue = str(contents[1])
                        print("{} is played between {},scored {} and {} scored {} at {} on {} and the result is {} and pom is {} from {}, and toss report is {}".format(contents[0],team1,team1_score,team2,team2_score,venue.split(" ")[5],contents[2],result,player_of_match,pom_team,toss_data.text))
                
    
    print (c)
