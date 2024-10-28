from selenium.webdriver.common.by import By

class HordLocator:
    SIDE_BAR_TOGGLER=(By.CSS_SELECTOR, "[class^='side-bar-toggler']:not(ul)")
    SIDE_BAR_FIRST_ITEM = (By.XPATH, "//*[text()='ETH Staking']")
