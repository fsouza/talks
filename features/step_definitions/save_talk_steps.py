from lettuce import *
from nose.tools import *

@step(u'Given I am logged in the system')
def given_i_am_logged_in_the_system(step):
    world.browser.go_to_url('/login')
    email_field = world.browser.find_element_by_xpath('//input[@type="text" and @name="email"]')
    login_button = world.browser.find_element_by_xpath('//input[@type="submit" and @value="Login"]')
    email_field.send_keys('franciscossouza@gmail.com')
    login_button.click()

@step(u'When I navigate to the new talk page')
def when_i_navigate_to_the_new_talk_page(step):
    world.browser.go_to_url('/talks/new')

@step(u'And fill the title field with "(.*)"')
def and_fill_the_title_field_with_group1(step, title):
    title_field = world.browser.find_element_by_xpath('//input[@type="text" and @name="title"]')
    title_field.send_keys(title)

@step(u'And fill the description field with "(.*)"')
def and_fill_the_description_field_with_group1(step, description):
    description_field = world.browser.find_element_by_xpath('//textarea[@name="description"]')
    description_field.send_keys(description)

@step(u'And fill the date field with "(.*)"')
def and_fill_the_date_field_with_group1(step, date):
    date_field = world.browser.find_element_by_xpath('//input[@type="text" and @name="date"]')
    date_field.send_keys(date)

@step(u'And click on the button Save talk')
def and_click_on_the_button_save_talk(step):
    button = world.browser.find_element_by_xpath('//input[@type="submit" and @value="Save talk"]')
    button.click()

@step(u'Then I should be redirected to the home page')
def then_i_should_be_redirected_to_the_home_page(step):
    current_url = world.browser.get_current_url()
    expected_url = world.browser.get_url('/')
    assert_equals(current_url, expected_url)

@step(u'And I should see "(.*)" on the screen')
def and_i_should_see_group1_on_the_screen(step, title):
    expected = '<li>%s</li>' %title
    assert expected in world.browser.get_source()

