from bs4 import BeautifulSoup
import requests
import csv

days = [31,29,31,30,31,30,31,31,30,31,30,31]

for year in range(1960, 2021): #years 1960 to 2020
    print(year)
    for month in range(1,13):
        if month>=11 or month<=2:
            continue
        print(month)
        for day in range(1,days[month-1]+1):
            result = requests.get("https://www.baseball-reference.com/boxes/?year=" + str(year) + '&month=' + str(month) + '&day='+ str(day))
            src = result.content
            soup = BeautifulSoup(src, 'lxml')

            soup.select(".winner")
            soup.select(".loser")

            #print("https://www.basketball-reference.com/boxscores/?month=" + str(month) + '&day=' + str(day) + '&year='+ str(year))

            for x in range(len(soup.select(".winner"))):
                with open('1960_to_2020W.csv', 'a', newline = '') as file:
                    csv_write = csv.writer(file)
                    csv_year = [int(soup.select(".winner")[x].find_all("td")[1].text)]
                    csv_write.writerow(csv_year)
                #wins_scores.append(soup.select(".winner")[x].find_all("td")[1].text)

            for x in range(len(soup.select(".loser"))):
                with open('1960_to_2020L.csv', 'a', newline = '') as file:
                    csv_write = csv.writer(file)
                    csv_year = [int(soup.select(".loser")[x].find_all("td")[1].text)]
                    csv_write.writerow(csv_year)

                #loss_scores.append(soup.select(".loser")[x].find_all("td")[1].text)

