import csv
import os
import pytest
from pages.home_page import HomePage
from pages.search_page import SearchPage

def load_search_data():
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "search_data.csv")
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))

@pytest.mark.parametrize("data", load_search_data())
def test_product_search(driver, data):
    home = HomePage(driver)
    search = SearchPage(driver)
    home.search(data["search_term"])

    if data["expected"] == "results":
        assert search.has_results(), f"No results for {data['search_term']}"
    else:
        assert search.has_no_results_message(), "Expected no-results message"
