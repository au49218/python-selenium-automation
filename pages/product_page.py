from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import Page


class ProductPage(Page):
    ADD_TO_CART_BTN = (By.ID, 'add-to-cart-button')
    NEW_ARRIVALS_LINK = (By.CSS_SELECTOR, '#nav-subnav > a:nth-child(7)')
    CART = (By.ID, 'nav-cart-count')
    SIZE_TOOLTIP = (By.ID, 'a-popover-content-1')
    DEALS_DISPLAY = (By.CSS_SELECTOR, "a[href*='fashion-boys']")
    SIZE_SELECTION_BTN = (By.ID, 'dropdown_selected_size_name')
    SIZE_OPTION_0 = (By.ID, 'size_name_0')
    PRICE_BUY_BOX = (By.ID, 'priceInsideBuyBox_feature_div')
    COLOR_OPTIONS = (By.CSS_SELECTOR, "#variation_color_name li")
    SELECTED_COLOR = (By.CSS_SELECTOR, "#variation_color_name .selection")

    def click_add_to_cart(self):
        self.click(*self.ADD_TO_CART_BTN)

    def select_size(self):
        self.click(*self.SIZE_SELECTION_BTN)
        self.click(*self.SIZE_OPTION_0)
        self.wait_for_element_appear(*self.PRICE_BUY_BOX)

    def hover_add_to_cart_btn(self):
        add_to_cart_btn = self.find_element(*self.ADD_TO_CART_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(add_to_cart_btn)
        actions.perform()

    def hover_new_arrivals_link(self):
        new_arrivals_link = self.find_element(*self.NEW_ARRIVALS_LINK)
        actions = ActionChains(self.driver)
        actions.move_to_element(new_arrivals_link)
        actions.perform()
        from time import sleep
        sleep(5)


    def verify_cart_count(self, expected_count: str):
        self.verify_text(expected_count, *self.CART)

    def verify_can_select_dress_colors(self):
        expected_colors = ['Emerald', 'Ivory', 'Navy']
        colors = self.find_elements(*self.COLOR_OPTIONS)

        for i in range(len(colors)):
            colors[i].click()
            self.verify_text(expected_colors[i], self.SELECTED_COLOR)

    def verify_size_selection_tooltip(self):
        self.wait_for_element_appear(*self.SIZE_TOOLTIP)

    def verify_deals_display(self):
        self.wait_for_element_appear(*self.DEALS_DISPLAY)
