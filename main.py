from selenium import webdriver
import time
import re
import zipfile

filename = '/home/avboz/PycharmProjects/gym-malware/VirusShare_00000.zip'

with zipfile.ZipFile(filename) as zip:
    files = zip.namelist()

for i in range(len(files)):
    files[i] = re.sub(r'VirusShare_', '', files[i], 1)

with open("data.txt", "a") as f:
    for i in range(100, 5000):
        url = "https://www.virustotal.com/gui/file/" + files[i]
        driver = webdriver.Firefox(executable_path="/home/avboz/PycharmProjects/selenium_python/firefoxdriver/geckodriver")

        try:
            driver.get(url=url)
            time.sleep(1)
            driver.get(url=driver.current_url+'/details')
            time.sleep(1)
            elements = driver.execute_script(f'return document.all;')
            for element in elements:
                lines = ''
                for line in element.text:
                    lines += re.sub("^\s+|\n|\r|\s+$", '', line)
                result = re.search(r'MD5(.){32}SHA-1(.){40}SHA-256(.){64}', lines)
                if result is not None:
                    result = re.sub(r'MD5', '', result.group(0), 1)
                    result = re.sub(r'SHA-1', ',', result, 1)
                    result = re.sub(r'SHA-256', ',', result, 1)
                    f.write(result + '\n')
                    print(i+1)
                    print(result)
                    break
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()
