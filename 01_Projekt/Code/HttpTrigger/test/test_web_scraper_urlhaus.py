import pytest
from unittest.mock import patch
from web_scraper_urlhaus import web_scraper_urlhaus


# Mock the requests.get function so it doesn't actually have to webscrape n
@patch('requests.get')
def test__get_data_csv(mock_get):
    # Simulate a successful HTTP response with some FAKE content
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = "some,csv,data,http://example.com\nanother,row,http://test.com"

    scraper = web_scraper_urlhaus()
    scraper._get_data_csv()

    # Check if URLs have been scraped and added to the list
    assert "test.com" in scraper.all_urls
