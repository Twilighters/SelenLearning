from selene.api import *

def test_login():
    browser.open("https://qacoursemoodle.innopolis.university/").driver.maximize_window()
    browser.element(".nav.navbar-nav.usernav a").click()
    browser.element("input#username").type("rishat")
    browser.element("input#password").type("Rishat-9173")
    browser.element("button#loginbtn").click()
    browser.element(".mr-1.usertext").should(have.text("Ришат Файзуллин")).click()
    browser.element("a:nth-of-type(6) > .menu-action-text").click()
    browser.element(".nav.navbar-nav.usernav a").should(be.visible)