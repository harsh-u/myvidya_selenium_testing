from selenium import webdriver
def test_title():
    driver = webdriver.Firefox()
    driver.get("https://www.myvidya.org/")
    print(driver.title)
    assert 'MyVidya' == driver.title
    driver.close()

test_title()