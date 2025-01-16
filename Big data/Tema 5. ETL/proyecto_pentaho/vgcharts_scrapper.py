from bs4 import BeautifulSoup
import urllib.request
import pandas as pd
import numpy as np
import time
from urllib.error import URLError
import logging
import sys
import random

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('vgchartz_scraper.log'),
        logging.StreamHandler(sys.stdout)
    ]
)

class VGChartzScraper:
    def __init__(self, pages=19):
        self.pages = pages
        self.base_url = 'https://www.vgchartz.com/games/games.php?page='
        self.url_params = {
            'console': '',
            'region': 'All',
            'developer': '',
            'publisher': '',
            'genre': '',
            'boxart': 'Both',
            'ownership': 'Both',
            'results': '50',  # Reduced results per page
            'order': 'Sales',
            'showtotalsales': '1',
            'showpublisher': '1',
            'showvgchartzscore': '0',
            'shownasales': '1',
            'showdeveloper': '1',
            'showcriticscore': '1',
            'showpalsales': '1',
            'showreleasedate': '1',
            'showuserscore': '1',
            'showjapansales': '1',
            'showlastupdate': '0',
            'showothersales': '1',
            'showgenre': '1',
            'sort': 'GL'
        }
        
        # Initialize data lists
        self.data = {
            'Rank': [], 'Name': [], 'Platform': [], 'Year': [],
            'Genre': [], 'Critic_Score': [], 'User_Score': [],
            'Publisher': [], 'Developer': [], 'NA_Sales': [],
            'PAL_Sales': [], 'JP_Sales': [], 'Other_Sales': [],
            'Global_Sales': []
        }
        
        # List of common user agents
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0'
        ]

    def build_url(self, page):
        """Construct URL with parameters"""
        params = '&'.join([f'{k}={v}' for k, v in self.url_params.items()])
        return f'{self.base_url}{page}&{params}'

    def get_soup(self, url, parser='html.parser'):
        """Safely retrieve and parse webpage with retry logic"""
        max_retries = 3
        for attempt in range(max_retries):
            try:
                headers = {
                    'User-Agent': random.choice(self.user_agents),
                    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                    'Accept-Language': 'en-US,en;q=0.5',
                    'Connection': 'keep-alive',
                    'Upgrade-Insecure-Requests': '1',
                }
                request = urllib.request.Request(url, headers=headers)
                response = urllib.request.urlopen(request)
                soup = BeautifulSoup(response.read(), parser)
                
                # Verify we got a valid page
                if soup.find('table'):
                    return soup
                
                logging.warning(f"Attempt {attempt + 1}: Page structure not as expected")
                time.sleep(2 * (attempt + 1))  # Exponential backoff
                
            except Exception as e:
                logging.error(f"Attempt {attempt + 1} failed: {str(e)}")
                if attempt < max_retries - 1:
                    time.sleep(2 * (attempt + 1))
                continue
                
        return None

    def parse_sales_value(self, value_str):
        """Safely parse sales values"""
        try:
            if value_str and not value_str.startswith('N/A'):
                # Remove any 'm' or 'M' suffix and convert to float
                clean_str = value_str.strip().lower().replace('m', '')
                return float(clean_str)
            return np.nan
        except (ValueError, AttributeError):
            return np.nan

    def parse_score(self, score_str):
        """Safely parse score values"""
        try:
            if score_str and not score_str.startswith('N/A'):
                return float(score_str)
            return np.nan
        except (ValueError, AttributeError):
            return np.nan

    def parse_year(self, year_str):
        """Safely parse release year"""
        try:
            if not year_str or year_str.startswith('N/A'):
                return np.nan
                
            # Try to extract year from different formats
            parts = year_str.strip().split()
            year = parts[-1]  # Take last part which should be the year
            
            # Handle two-digit years
            if len(year) == 2:
                year = '19' + year if int(year) >= 80 else '20' + year
            
            # Convert to integer
            return int(year)
        except (ValueError, AttributeError, IndexError):
            return np.nan

    def find_game_table(self, soup):
        """Find the game data table using multiple possible selectors"""
        # Try different ways to locate the table
        table = soup.find('table', {'id': 'generalBody'})
        if not table:
            table = soup.find('table', {'class': 'chart'})
        if not table:
            table = soup.find('table')
        
        return table

    def scrape_game_data(self, row):
        try:
            # Extract data from the row
            rank = row.find('td', class_='rank').text.strip()
            name = row.find('td', class_='name').text.strip()
            platform = row.find('td', class_='platform').text.strip()
            year = row.find('td', class_='year').text.strip()
            genre = row.find('td', class_='genre').text.strip()
            critic_score = row.find('td', class_='critic_score').text.strip()
            user_score = row.find('td', class_='user_score').text.strip()
            publisher = row.find('td', class_='publisher').text.strip()
            developer = row.find('td', class_='developer').text.strip()
            na_sales = row.find('td', class_='na_sales').text.strip()
            pal_sales = row.find('td', class_='pal_sales').text.strip()
            jp_sales = row.find('td', class_='jp_sales').text.strip()
            other_sales = row.find('td', class_='other_sales').text.strip()
            global_sales = row.find('td', class_='global_sales').text.strip()

            # Append data to the dictionary
            self.data["Rank"].append(rank)
            self.data["Name"].append(name)
            self.data["Platform"].append(platform)
            self.data["Year"].append(year)
            self.data["Genre"].append(genre)
            self.data["Critic_Score"].append(critic_score)
            self.data["User_Score"].append(user_score)
            self.data["Publisher"].append(publisher)
            self.data["Developer"].append(developer)
            self.data["NA_Sales"].append(na_sales)
            self.data["PAL_Sales"].append(pal_sales)
            self.data["JP_Sales"].append(jp_sales)
            self.data["Other_Sales"].append(other_sales)
            self.data["Global_Sales"].append(global_sales)

            return True
        except Exception as e:
            logging.error(f"Error scraping data: {e}")
            return False

    def scrape(self):
        """Main scraping function"""
        for page in range(1, self.pages + 1):
            logging.info(f"Scraping page {page}")
            url = self.build_url(page)
            soup = self.get_soup(url)
            
            if not soup:
                logging.error(f"Failed to retrieve page {page}")
                continue

            # Find the game table
            game_table = self.find_game_table(soup)
            if not game_table:
                logging.error(f"Could not find game table on page {page}")
                # Debug output
                logging.debug("Page content:")
                logging.debug(soup.prettify()[:1000])  # First 1000 chars
                continue

            # Process each game row
            game_rows = game_table.find_all('tr')[1:]  # Skip header row
            for row in game_rows:
                if self.scrape_game_data(row):
                    logging.info(f"Successfully scraped {self.data['Name'][-1]}")
                
            # Random delay between 2-4 seconds
            time.sleep(random.uniform(2, 4))

    def save_to_csv(self, filename="vgsales.csv"):
        """Save scraped data to CSV"""
        df = pd.DataFrame(self.data)
        df.to_csv(filename, index=False)
        logging.info(f"Data saved to {filename}")
        return df

def main():
    # Set debug level for more detailed output
    logging.getLogger().setLevel(logging.DEBUG)
    
    scraper = VGChartzScraper(pages=19)
    scraper.scrape()
    df = scraper.save_to_csv()
    logging.info(f"Scraped {len(df)} games in total")

if __name__ == "__main__":
    main()