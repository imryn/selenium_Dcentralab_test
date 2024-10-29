from selenium.webdriver.common.by import By

class HordLocator:
    SIDE_BAR_TOGGLER=(By.CSS_SELECTOR, "[class^='side-bar-toggler']:not(ul)")
    SIDE_BAR_FIRST_ITEM = (By.CSS_SELECTOR, "span[class='duf-sidebar-textbox']")
    FAQ = (By.XPATH, "//h2[text()='Frequently Asked Questions']")
    FAQ_QUESTIONS = (By.CSS_SELECTOR, "span[class='sc-fqkvVR cauyVW faq-item-question font-500']")
