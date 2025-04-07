import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Hardcoded credentials
username = 'enter_your_username'
password = 'enter_your_password'

def login_instagram(driver, username, password):
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    # Accept cookies (if present)
    try:
        accept_button = driver.find_element(By.XPATH, "//button[text()='Only allow essential cookies']")
        accept_button.click()
        time.sleep(2)
    except:
        pass
    # Enter credentials
    user_input = driver.find_element(By.NAME, "username")
    pass_input = driver.find_element(By.NAME, "password")
    user_input.send_keys(username)
    pass_input.send_keys(password)
    pass_input.send_keys(Keys.RETURN)
    time.sleep(6)  # Wait for login to complete
    # Optional: Dismiss pop-ups
    try:
        not_now = driver.find_element(By.XPATH, "//button[contains(text(), 'Not Now')]")
        not_now.click()
        time.sleep(2)
    except:
        pass

def get_instagram_post_descriptions(target_user: str, num_posts: int):
    # Use hardcoded credentials instead of environment variables
    options = Options()
    # Comment out headless for debugging
    # options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    
    try:
        # Use the hardcoded username and password variables
        login_instagram(driver, username, password)
        
        profile_url = f"https://www.instagram.com/{target_user}/"
        print(f"\nOpening profile: {profile_url}")
        driver.get(profile_url)
        time.sleep(5)
        
        for _ in range(3):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)
            
        thumbnails = driver.find_elements(By.XPATH, '//a[contains(@href, "/p/") and descendant::img]')
        post_urls = []
        seen = set()
        
        for thumb in thumbnails:
            href = thumb.get_attribute("href")
            if href not in seen and href and "/p/" in href:
                post_urls.append(thumb)
                seen.add(href)
            if len(post_urls) >= num_posts:
                break
                
        print(f"Found {len(post_urls)} posts.")
        descriptions = []
        
        for i, thumb in enumerate(post_urls, 1):
            try:
                driver.execute_script("arguments[0].scrollIntoView();", thumb)
                time.sleep(1)
                thumb.click()
                time.sleep(3)
                
                try:
                    caption = driver.find_element(By.XPATH, '//div[@role="dialog"]//ul//span').text
                except:
                    caption = "[No description]"
                    
                descriptions.append(caption)
                close_btn = driver.find_element(By.XPATH, '//div[@role="dialog"]//button[contains(@aria-label, "Close")]')
                close_btn.click()
                time.sleep(2)
                
            except Exception as e:
                descriptions.append("[Error reading post]")
                print(f"Post {i}: Error -> {e}")
                
        print("\nPost Descriptions:\n")
        for i, desc in enumerate(descriptions, 1):
            print(f"{i}. {desc}\n")
            
    finally:
        driver.quit()

if __name__ == "__main__":
    get_instagram_post_descriptions("enter_your_password", num_posts=6)
