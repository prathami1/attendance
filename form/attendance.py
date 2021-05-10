from selenium import webdriver

browser = webdriver.Chrome(r'path to chrome driver')

browser.get('url of the form')
firstName = browser.find_element_by_name("First Name?");
lastName = browser.find_element_by_name("Last Name?");
reflection = browser.find_element_by_name("Reflect on what you did");

# enter credentials here
firstName.send_keys("**First Name**");
firstName.send_keys("Keys.ENTER");
lastName.send_keys("**Last Name**");
lastName.send_keys("Keys.ENTER");

attendance = browser.find_element_by_name("Yes");
attendance.click();
reflection.send_keys(
    "I completed all assigned work by the teacher in a timely fashion in order to take advantage of this remote learning oppertunity");
reflection.send_keys("Keys.ENTER");

# submitting the form
submission = browser.find_element_by_link_text("Submit");
submission.click();

# written by Pratham Inamdar, implementing selenium through Python
