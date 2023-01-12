import os
import smtplib
import requests
import logging 
import env
import concurrent.futures
logging.basicConfig(filename="log.txt", level=logging.DEBUG, format="%(asctime)s %(message)s")
logging.debug("Debug logging test...")

EMAIL_ADDRESS = os.environ['EMAIL_USER']
EMAIL_PASSWORD = os.environ.get('EMAIL_PASS')



wiki_page_urls = [
    "https://en.wikipedia.org/wiki/Ocean",
    "https://en.wikipedia.org/wiki/Island",
    "https://en.wikipedia.org/wiki/this_page_does_not_exist",
    "https://en.wikipedia.org/wiki/Shark",
]


def check_uptime(website):
    r = requests.get(website, timeout=5)
    if r.status_code == 200:
        logging.info("website is up!")
        page_status = 'Active'
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

            smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

            subject = f'{website}  IS DOWN'
            body = 'Make sure the server restarted and it is back up!'
            msg = f'Subject: {subject}\n\n{body}'

            smtp.sendmail(EMAIL_ADDRESS, 'iyandataofeek11@gmail.com', msg)
            logging.info(f'Mail Successfully sent to {EMAIL_ADDRESS}')

    else:
        page_status = 'Not Active'
        return page_status
    return website + " - " + page_status
            

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = []
    for url in wiki_page_urls:
        futures.append(executor.submit(check_uptime, website=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result)
