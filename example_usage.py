from client import AgenticWebScrapingAntiBotBypasserClient

def main():
    client = AgenticWebScrapingAntiBotBypasserClient()
    res = client.scrape_url("https://example.com/protected-page", True)
    print(f"Protection Bypassed: {res['protection_bypassed']} (HTTP {res['http_status']})")
    print(res["extracted_html_markdown"])

if __name__ == "__main__":
    main()
