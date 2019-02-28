import math
import json
import requests as re
from bs4 import BeautifulSoup

zipcodes = ["94108","94109","94110","10021","10022"]

def fetch_zipcode_links(zipcode_list):
    
    base_url = "https://www.yelp.com/search?find_desc=Restaurants&find_loc="
    zipcode_dict = {}
    
    for i in zipcode_list:
        
        # Get initial zipcode page
        zipcode_url = base_url+i
        response = re.get(zipcode_url)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Fetch number of results
        n_results = soup.find("p", {"class":"lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7"}).text
        n_results_index = n_results.find("of") + 2
        n_results = int(n_results[n_results_index:])
        
        # Fetch number of results per page
        n_showing = soup.find("p", {"class":"lemon--p__373c0__3Qnnj text__373c0__2pB8f text-color--normal__373c0__K_MKN text-align--right__373c0__3ARv7"}).text
        n_showing_index_start = int( n_showing.find("-") + 1)
        n_showing_index_end = n_showing_index_start + int(n_showing[n_showing_index_start:].find(" "))
        n_showing = int(n_showing[n_showing_index_start:n_showing_index_end])
        
        # Calculate number of pages to crawl
        n_pages = math.ceil(n_results / n_showing)
        
        # Derive page links
        zipcode_page_urls = []
        for j in range(n_pages):
            start_by = j*n_showing
            current_url = zipcode_url+"&start={}".format(start_by)
            zipcode_page_urls.append(current_url)
            
        zipcode_dict[i] = zipcode_page_urls
        
    #return zipcode_dict
    with open('/home/gnazareths/real_estate/data/yelp_scraping/toy_zipcode_links_df.json', 'w') as f:
        json.dump(zipcode_dict, f)
        
    return

fetch_zipcode_links(zipcodes)