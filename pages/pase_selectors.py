class ID:
    WORD_FILE_IN_TREE = "tree-node-wordFile"


class BasePage:
    APP = "#app"


class MainPage:
    EVENTS_BTN = "//*[@class='card mt-4 top-card' and .//*[contains(text(), 'Elements')]]"


class ElementsPage:
    CHECK_BOX_IN_MENU = ".menu-list > #item-1"
    ELEMENTS_HEADER = "//*[@class='main-header' and contains(text(), 'Elements')]"


class CheckBoxPage:
    RESULT_TEXT = "#result"
    CHECK_BOX_TREE = "#tree-node"
    CHECK_BOX_TREE_LABEL = "//label[.//input[@id='{}']]/span"
    CHECK_BOX_TREE_CHECKED = "//label[.//input[@id='{}']]//*[contains(@class, 'rct-icon-check')]"
    HOME_TREE_NODE = "//li[.//input[@id='tree-node-home']]"
    HOME_TREE_TOGGLE = "//li[.//input[@id='tree-node-home']]/span/button"
    DOWNLOADS_TREE_NODE = "//li[./span/label[@for='tree-node-downloads']]"
    DOWNLOADS_TREE_TOGGLE = "//span[.//label[@for='tree-node-downloads']]/button"
