from selenium import webdriver

def test_google_title():
    driver = webdriver.Firefox()
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
