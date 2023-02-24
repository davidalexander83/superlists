from selenium import webdriver
from .base import FunctionalTest
from .server_tools import create_session_on_server
from .management.commands.create_session import create_pre_authenticated_session
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from django.conf import settings

def quit_if_possible(browser):
  try: browser.quit()
  except: pass

class SharingTest(FunctionalTest):

  def create_pre_authenticated_session(self, email):
    if self.staging_server:
      session_key = create_session_on_server(self.staging_server, email)
    else:
      session_key = create_pre_authenticated_session(email)
    # To set a cookie we need to first visit the domain.
    # 404 pages load the quickest!
    self.browser.get(self.live_server_url + '/404_no_such_url/')
    self.browser.add_cookie(dict(
      name = settings.SESSION_COOKIE_NAME,
      value = session_key,
      path = '/',
    ))

  def test_can_share_a_list_with_another_user(self):
    # Edith is a logged-in user
    self.create_pre_authenticated_session('edith@example.com')
    edith_browser = self.browser
    self.addCleanup(lambda: quit_if_possible(edith_browser))

    # Her friend Oniciferous is also hanging out on the Lists site
    oni_browser = webdriver.Firefox()
    self.addCleanup(lambda: quit_if_possible(oni_browser))
    self.browser = oni_browser
    self.create_pre_authenticated_session('oniciferous@example.com')

    # Edith goes to the home page and starts a list
    self.browser = edith_browser
    self.browser.get(self.live_server_url)
    self.add_list_item('Get help')

    # She notices a 'Share this list' option
    share_box = self.browser.find_element(By.CSS_SELECTOR, 'input[name="sharee"]')
    self.assertEqual(share_box.get_attribute('placeholder'), 'your-friend@example.com')