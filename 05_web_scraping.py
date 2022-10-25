from bs4 import BeautifulSoup
import  requests
import csv

source = requests.get('https://www.healthline.com/health/cancer').text
soup = BeautifulSoup(source, 'lxml')
heading = soup.find('div', class_='css-z468a2').h1.text
author = soup.find('section', class_="css-lizeih").text
article_body = soup.find('article', class_="article-body css-d2znx6 undefined")
summary = article_body.find_all('p')
causes = article_body.find_all('li')

csv_file = open('article_summary.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Author', 'Topic'])
csv_writer.writerow([author, heading])

csv_file.close()


#
#
# print(heading)
# print()
# print(author)
# print()
# for n in summary[:3]:
#     print(n.text)
#
# for n in causes[:3]:
#     print('\n', n.text)
#
