#!/usr/bin/env python3
"""Browser screenshot utility for Claude Code projects."""

import os
import sys
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def take_screenshot(url, output_dir="screenshots", wait_time=5):
    """Take a screenshot of a webpage."""
    # Create screenshots directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Configure Chrome options
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    # Enable dangerous permissions if needed
    chrome_options.add_argument("--dangerously-skip-permissions")
    
    # Initialize driver
    driver = webdriver.Chrome(options=chrome_options)
    
    try:
        # Navigate to URL
        driver.get(url)
        
        # Wait for page to load
        WebDriverWait(driver, wait_time).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )
        
        # Generate filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{output_dir}/screenshot_{timestamp}.png"
        
        # Take screenshot
        driver.save_screenshot(filename)
        print(f"Screenshot saved: {filename}")
        
        return filename
        
    finally:
        driver.quit()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python screenshot.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    take_screenshot(url)