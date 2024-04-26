import yagooglesearch

query = "site:@compwire.com.br"

client = yagooglesearch.SearchClient(
    query,
    tbs="li:1",
    verbosity=4,
    num=10,
    max_search_result_urls_to_return=1000,
    minimum_delay_between_paged_results_in_seconds=1,
    yagooglesearch_manages_http_429s=False,  # Add to manage HTTP 429s.
)
client.assign_random_user_agent()

urls = client.search()

if "HTTP_429_DETECTED" in urls:
    print("HTTP 429 detected...it's up to you to modify your search.")

    # Remove HTTP_429_DETECTED from list.
    urls.remove("HTTP_429_DETECTED")

    print("URLs found before HTTP 429 detected...")

    for url in urls:
        print(url)
