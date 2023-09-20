import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin


def replace_image_paths(url, old_path, new_path):
    
    response = requests.get(url)

    
    if response.status_code == 200:
        
        soup = BeautifulSoup(response.content, 'html.parser')

        
        images = soup.find_all('img')

        for image in images:
            
            image_src = image.get('src')

            
            if old_path in image_src:
                
                new_image_src = image_src.replace(old_path, new_path)

                
                image['src'] = new_image_src

                print(f"Image path replaced: {image_src} --> {new_image_src}")

        
        modified_html = soup.prettify()

               
        with open('modified_page.html', 'w') as file:
            file.write(modified_html)

        
        
    else:
        print(f"Failed to retrieve page: {url}")



website_url = 'https://dev2fe.tradeindia.com/'  
old_image_path = 'https://tiimg.tistatic.com/categoryimg/v1/1/T-Shirts-61.png'  
new_image_path = 'https://tiimg-dev2.tistatic.com/categoryimg/v1/1/T-Shirts-61.png'  

replace_image_paths(website_url, old_image_path, new_image_path)