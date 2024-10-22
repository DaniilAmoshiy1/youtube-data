from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

from config import (
    CHECK_VALUE,
    NAME_ELEMENT_ID,
    OUTPUT_FILE,
)
import parseArguments


driver: webdriver = webdriver.Chrome()


def main(url: str):
    if CHECK_VALUE in url:
        driver.get(url)
        print(driver.title)
        sleep(1)

        try:
            video_name_elements = driver.find_elements(By.ID, NAME_ELEMENT_ID)

            with open(OUTPUT_FILE, 'w') as out_file:
                for element in video_name_elements:
                    video_name: str = f'Video name: {element.text}'
                    out_file.write(video_name + '\n')

        except Exception as err:
            print(f'Error: {err}')

        driver.quit()
        exit(0)
    else:
        print('Incorrect link, try again')
        driver.quit()
        exit(0)


if __name__ == '__main__':
    args = parseArguments.parser_args()
    main(args.url)
