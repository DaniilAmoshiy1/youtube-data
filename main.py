from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

from working_files.config import (
    CHECK_VALUE,
    NAME_ELEMENT_ID,
    OUTPUT_FILE,
    VIEWS_ELEMENT_XPATH,
    LENGTH_ELEMENT_XPATH,
    NORMAL_EXIT_CODE,
    ERROR_EXIT_CODE,
    SECONDS_FOR_SLEEP,
)
from working_files.argument_parser import parser_args


driver: webdriver = webdriver.Chrome()


def main(url: str):
    if CHECK_VALUE in url:
        driver.get(url)
        print(driver.title)
        sleep(SECONDS_FOR_SLEEP)

        try:
            video_name_elements = driver.find_elements(By.ID, NAME_ELEMENT_ID)
            video_length_elements = driver.find_elements(By.XPATH, LENGTH_ELEMENT_XPATH)
            video_views_elements = driver.find_elements(By.XPATH, VIEWS_ELEMENT_XPATH)

            with open(OUTPUT_FILE, 'w', encoding='UTF-8') as out_file:
                for name_element, length_element, views_element in zip(video_name_elements,
                                                                       video_length_elements,
                                                                       video_views_elements):
                    video_name: str = f'Video name: {name_element.text}'
                    video_length: str = f'Video length: {length_element.get_attribute("aria-label")}'
                    video_views: str = f'{views_element.text}'
                    out_file.write(video_name + '\n')
                    out_file.write(video_length + '\n')
                    out_file.write(video_views + '\n\n')

        except Exception as err:
            print(f'Error: {err}')

        driver.quit()
        exit(NORMAL_EXIT_CODE)
    else:
        print('Incorrect link, try again')
        driver.quit()
        exit(ERROR_EXIT_CODE)


if __name__ == '__main__':
    args = parser_args()
    main(args.url)
