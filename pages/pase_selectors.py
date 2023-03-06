class BasePage:
    APP = "#app"


class MainPage:
    EVENTS_BTN = "//*[@class='category-cards' and .//*[contains(text(), 'Elements')]]"


class ElementsPage:
    MAIN_HEADER = ".main-header"
    CHECK_BOX_IN_MENU = ".menu-list > #item-1"
    CHECK_BOX_TREE = "#tree-node"
    HOME_TREE_TOGGLE = "//li[.//input[@id='tree-node-home']]/span/button"
