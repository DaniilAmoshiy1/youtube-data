from time import sleep

from selenium.webdriver.common.by import By
from selenium import webdriver

from source.config import (
    CHECK_VALUE,
    NAME_ELEMENT_ID,
    OUTPUT_FILE,
    VIEWS_ELEMENT_XPATH,
    LENGTH_ELEMENT_XPATH,
    NORMAL_EXIT_CODE,
    ERROR_EXIT_CODE,
    SECONDS_FOR_SLEEP,
)
from source.argument_parser import parser_args


def main(url: str):
    driver = webdriver.Chrome()

    if CHECK_VALUE not in url:
        print('Incorrect link, try again')
        driver.quit()
        exit(ERROR_EXIT_CODE)

    driver.get(url)
    print(driver.title)
    sleep(SECONDS_FOR_SLEEP)

    try:
        video_elements = {
            'name': driver.find_elements(By.ID, NAME_ELEMENT_ID),
            'length': driver.find_elements(By.XPATH, LENGTH_ELEMENT_XPATH),
            'views': driver.find_elements(By.XPATH, VIEWS_ELEMENT_XPATH)
        }

        zipped_elements = zip(
            video_elements['name'],
            video_elements['length'],
            video_elements['views']
        )

        with open(OUTPUT_FILE, 'w', encoding='UTF-8') as out_file:
            for name_element, length_element, views_element in zipped_elements:
                video_data = {
                    'name': f'Video name: {name_element.text}',
                    'length': f'Video length: {length_element.get_attribute("aria-label")}',
                    'views': f'{views_element.text}'
                }

                for key in video_data:
                    out_file.write(video_data[key] + '\n')
                out_file.write('\n')

    except Exception as err:
        print(f'Error: {err}')

    driver.quit()
    exit(NORMAL_EXIT_CODE)


if __name__ == '__main__':
    args = parser_args()
    main(args.url)
