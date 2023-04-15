# my own
from insta_follower import InstaFollower


# scroll_pop_down = driver.find_element(By.XPATH, value='/html/body/div[6]/div/div/div/div[2]')
# scroll_pop_down.send_keys(Keys.END)

instagram_follower = InstaFollower()
instagram_follower.login()
instagram_follower.find_followers()
instagram_follower.follow()
instagram_follower.terminate_window()

# '/html/body/div[6]/div/div/div/div[2]/ul/div/li[1]/div/div[2]/button/div'

# '/html/body/div[6]/div/div/div/div[2]'