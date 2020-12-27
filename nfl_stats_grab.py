from bs4 import BeautifulSoup
import requests
import csv

days = [31,29,31,30,31,30,31,31,30,31,30,31]

for year in range(1990, 2021): #years 1990 to 2020
    print(year)
    for week_num in range(1,22):
        print(week_num)
        result = requests.get("https://www.pro-football-reference.com/years/" + str(year) + '/week_' + str(week_num) + '.htm')
        src = result.content
        soup = BeautifulSoup(src, 'lxml')

        soup.select(".winner")
        soup.select(".loser")

        #print("https://www.basketball-reference.com/boxscores/?month=" + str(month) + '&day=' + str(day) + '&year='+ str(year))

        for x in range(len(soup.select(".winner"))):
            with open('NFL1990_to_2020W.csv', 'a', newline = '') as file:
                csv_write = csv.writer(file)
                csv_year = [int(soup.select(".winner")[x].find_all("td")[1].text)]
                csv_write.writerow(csv_year)
                #wins_scores.append(soup.select(".winner")[x].find_all("td")[1].text)

        for x in range(len(soup.select(".loser"))):
            with open('NFL1990_to_2020L.csv', 'a', newline = '') as file:
                csv_write = csv.writer(file)
                csv_year = [int(soup.select(".loser")[x].find_all("td")[1].text)]
                csv_write.writerow(csv_year)

        for x in range(len(soup.select(".draw"))):
            with open('NFL1990_to_2020DRAW.csv', 'a', newline = '') as file:
                csv_write = csv.writer(file)
                csv_year = [int(soup.select(".draw")[x].find_all("td")[1].text)]
                csv_write.writerow(csv_year)