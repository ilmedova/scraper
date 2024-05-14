import undetected_chromedriver
from bs4 import BeautifulSoup
import time
import csv

try:
    driver = undetected_chromedriver.Chrome()
    driver.get('https://www.amazon.com/')
    time.sleep(60)

    html = driver.page_source

    soup = BeautifulSoup(html, 'html.parser')
    links = []

    title = soup.title.string
    links_tags = soup.find_all('a')

    # print the results
    print('Title:', title)
    print('Links:')

    for link in links_tags:
        link_url = link.get('href')
        print(link_url)
        links.append(link_url)

    with open('links.csv', 'w', newline='') as csvfile:
        fieldnames = ['links']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for link in links:
            writer.writerow({'links': link})

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
