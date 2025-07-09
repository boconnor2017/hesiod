### What Does a Crawler Do?

A **web crawler** (sometimes called a **spider** or **bot**) performs several key functions:

1. **Fetching Web Pages**: The primary role of a crawler is to access and download HTML pages from the web. It starts with a list of initial URLs (called **seeds**), then follows links on those pages to other URLs, and so on.

2. **Extracting Content**: Once a page is fetched, the crawler typically parses the HTML content to extract useful data like text, images, links, metadata, or any other structured data (e.g., JSON, XML). For example, it might scrape all the text from articles or product details from e-commerce sites.

3. **Following Links (Crawling)**: A good crawler isn’t just fetching one page. It recursively follows hyperlinks (anchor tags `<a href="...">`) on each page to explore and discover other pages, allowing it to build a **web graph** of interconnected pages.

4. **Storing or Processing Data**: After fetching the content, the crawler either:

   * Stores it in a local database for later use.
   * Processes it on the fly to extract specific data (e.g., scraping product prices or extracting specific sentences).

5. **Respecting the Robots.txt**: Most well-behaved crawlers follow rules specified in the `robots.txt` file on websites, which tells crawlers which pages they can or can’t access. For example, search engines use this to avoid overloading websites with requests.

---

### Python Crawlers: How Do They Work?

In Python, web crawlers are typically written using libraries like **Requests**, **BeautifulSoup**, **Scrapy**, and **Selenium**. Let’s break down how they work:

#### 1. **Fetching Web Pages**:

To fetch a web page, the crawler will typically use HTTP requests. Python’s `requests` library is commonly used for this:

```python
import requests

url = 'https://example.com'
response = requests.get(url)
html = response.text  # This contains the raw HTML of the page
```

This makes an HTTP GET request to the URL and gets the raw HTML in return.

#### 2. **Parsing HTML**:

Once the HTML is fetched, the crawler needs to extract useful information. This is often done using **BeautifulSoup**, which makes it easy to parse and navigate HTML documents:

```python
from bs4 import BeautifulSoup

soup = BeautifulSoup(html, 'html.parser')

# Example: Extract all links on the page
links = soup.find_all('a', href=True)
for link in links:
    print(link['href'])
```

This finds all `<a>` tags with an `href` attribute (i.e., links) and prints the URL for each one.

#### 3. **Following Links (Recursion)**:

A good crawler doesn't just scrape the first page; it follows links to discover other pages. Typically, the crawler collects a list of URLs (or "queue") and fetches them one by one. For instance, you could set up a simple recursive structure:

```python
def crawl(url, depth=3):
    if depth == 0:
        return
    
    print(f"Scraping: {url}")
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', href=True)
    for link in links:
        next_url = link['href']
        if next_url.startswith('http'):
            crawl(next_url, depth - 1)  # Recursively crawl

# Start crawling from a seed URL
crawl('https://example.com', depth=3)
```

This will recursively scrape pages, following links up to a specified depth.

#### 4. **Respecting `robots.txt`**:

Before making requests to a website, a crawler should check the site's `robots.txt` file to see if there are any restrictions on crawling. Here’s an example of how a crawler can check `robots.txt`:

```python
import requests

def check_robots(url):
    robots_url = url + '/robots.txt'
    response = requests.get(robots_url)
    return response.text

robots_txt = check_robots('https://example.com')
print(robots_txt)
```

This will download and display the contents of `robots.txt`, which tells the crawler which parts of the site it can and cannot crawl.

#### 5. **Rate Limiting and Throttling**:

To avoid overwhelming a server, crawlers often include **rate limiting**. This means they’ll add delays between requests. This can be done using `time.sleep()` in Python, like so:

```python
import time

time.sleep(2)  # Wait for 2 seconds between requests to avoid spamming
```

---

### Where Does the Crawler’s Runtime Live?

A web crawler can run anywhere you can execute Python code:

* **Local Machine**: For small crawls or testing, you can run a crawler directly on your own computer. For instance, running a script that scrapes a few websites or a few pages on a site.

* **Cloud Server or Virtual Machine**: For large-scale crawling or continuous crawls, a more powerful cloud environment might be used (e.g., AWS, Google Cloud, or even something like DigitalOcean or Linode). Cloud environments can scale resources dynamically based on the crawl’s complexity.

* **Distributed Crawlers**: For really large crawls (e.g., crawling the entire web or large parts of it), a crawler might be distributed across many machines. This is where tools like **Scrapy** come in, which can be configured for distributed crawling.

### How Does a Crawler Obtain Access?

There are a few different ways a crawler gains access to websites:

1. **Open Access**: Most websites are publicly accessible, and any crawler with the correct URL can access them.

2. **User-Agent**: Some websites check the **User-Agent** header to identify if the request is coming from a bot. A crawler can mimic a real browser by setting a custom User-Agent string:

   ```python
   headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
   }
   response = requests.get(url, headers=headers)
   ```

3. **Authentication**: Some websites require authentication (e.g., via login forms). Crawlers can handle this by managing sessions with cookies or using APIs with API keys:

   ```python
   session = requests.Session()
   login_data = {'username': 'myuser', 'password': 'mypassword'}
   session.post('https://example.com/login', data=login_data)
   ```

4. **API Access**: Some websites provide APIs that allow programmatic access to their data. Crawlers can use these APIs to pull structured data, often in JSON format. The crawler just needs an API key or token:

   ```python
   api_url = 'https://api.example.com/data'
   response = requests.get(api_url, headers={'Authorization': 'Bearer API_KEY'})
   data = response.json()
   ```

---

### Recap:

* A **crawler** fetches web pages, extracts useful data, follows links recursively, and respects robots.txt.
* Python crawlers often use libraries like **Requests** (for HTTP requests) and **BeautifulSoup** (for parsing HTML).
* The **runtime** can be local or cloud-based, depending on the scale of the crawl.
* Crawlers can **obtain access** to sites via open access, mimicking browsers, authentication, or using APIs.

If you were to build a crawler, you'd typically begin by fetching and parsing pages, then expanding to handle more complex things like rate limiting, authentication, or distributed crawling.

Let me know if you want to dig into any specific part of this or see a more detailed example!
