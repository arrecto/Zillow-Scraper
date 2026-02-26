# Zillow Scraper — Hawaii Real Estate Data Collection

A Scrapy-based web scraper for collecting property listing data from Zillow, targeting the Hawaii real estate market through Zillow's internal async search API.

## Overview

This scraper uses Zillow's internal `async-create-search-page-state` API endpoint rather than traditional HTML parsing. By sending structured JSON queries with geographic bounds and filter criteria, it retrieves property listing data directly from Zillow's search backend — a more reliable and efficient approach than DOM scraping.

### Key Features

- **API-Based Extraction** — Queries Zillow's internal PUT endpoint for structured JSON responses instead of parsing HTML
- **Geographic Targeting** — Configurable map bounds covering the Hawaiian Islands (latitude 20.96–22.43, longitude -160.50 to -158.84)
- **Scrapy Framework** — Built on Scrapy's async architecture with Twisted for efficient crawling
- **Extensible Pipeline** — Standard Scrapy Item/Pipeline architecture for adding storage backends

## Architecture

```
Scrapy CrawlProcess
    ↓
ListingSpider.start_requests()
    ↓  PUT request with JSON payload
Zillow async-create-search-page-state API
    ↓  JSON response
ListingSpider.parse()
    ↓  Extract listResults
Property Listing URLs / Data
```

### Search Payload

The scraper sends a PUT request with a `searchQueryState` payload containing:
- **Map bounds** — Latitude/longitude bounding box for Hawaii
- **Filters** — Sort selection, property type filters
- **Display options** — List view results with category-based result sets

## Tech Stack

| Component | Technology |
|-----------|-----------|
| Framework | Scrapy |
| Language | Python 3.12 |
| Async Runtime | Twisted (AsyncioSelectorReactor) |
| Data Processing | Pandas |
| HTML Parsing | BeautifulSoup (bs4) |

## Project Structure

```
usa-hi-zillow/
└── zillow_scrape/
    ├── main.py                          # Entry point
    ├── scrapy.cfg                       # Scrapy config
    └── zillow_scrape/
        ├── settings.py                  # Request headers & Scrapy settings
        ├── spiders/
        │   └── class_spiders.py         # ListingSpider implementation
        ├── pipelines.py                 # Data processing pipeline
        ├── middlewares.py               # Request/response middleware
        └── items.py                     # Data models
```

## Usage

```bash
pip install scrapy pandas beautifulsoup4

cd zillow_scrape
python main.py
```

## Notes

- The scraper respects `robots.txt` rules (`ROBOTSTXT_OBEY = True`)
- Session cookies and headers are required for authentication with Zillow's API
- Designed for research and personal data collection purposes
