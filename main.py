import logging
from datetime import datetime as dt
import os
from linkedin_tools.source import Alinkedin
from linkedin_tools.random_poll_questions import get_random_question
from linkedin_tools.random_summary import get_random_summary
from linkedin_tools.random_fact import get_random_fact
import time



log_folder = "logs"
os.makedirs(log_folder,exist_ok=True)

now = dt.now()
logging.basicConfig(filename=os.path.join(log_folder,f"Entries{now.year}_{now.month}_{now.day}.txt"),level=logging.INFO,format="%(asctime)s - %(levelname)s - %(message)s")


#go to linked profile click on create post and copy and url link
#go to linkedin profile click on edit button on about and copy the url link

create_post_url = "" #paste url here
update_about_url = "" #paste url here

logging.info("LinkedIn automation script started.")


try:
    linkedin = Alinkedin()
    logging.info("Successfully created LinkedIn automation object.")
except Exception as e:
    logging.error(f"Failed to initialize LinkedIn object: {e}")







try:
    fact = get_random_fact()
    linkedin.post_tweet(url=create_post_url,post=fact)

except Exception as e:
    print(e)


try:
    poll_question = get_random_question()
    linkedin.post_poll(poll=poll_question,url=create_post_url,login=False)

except Exception as e:
    print(e)


try:
    logging.info("Fetching random profile summary content.")
    summary_text = get_random_summary()
    logging.info("Attempting to update LinkedIn profile summary.")
    linkedin.update_summary(summary_text=summary_text, summary_link=update_about_url, login=False)
    logging.info("Profile summary successfully updated.")
except Exception as e:
    logging.error(f"Failed to update profile summary: {e}")


current_time = dt.fromtimestamp(time.time())
formatted_time = f"{current_time.strftime('%m/%d/%Y %I:%M:%S %p')}"
logging.info(f"Current script execution time: {formatted_time}")




try:
    logging.info("Script operations completed. Closing browser.")
    linkedin.quit_driver()
    logging.info("Browser successfully closed.")
except Exception as e:
    logging.error(f"Failed to close browser: {e}")

logging.info("LinkedIn automation script finished.\n\n")
