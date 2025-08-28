from youtubesearchpython import VideosSearch

def get_youtube_links(query, max_results=5):
    videos_search = VideosSearch(query, limit=max_results)
    results = videos_search.result().get("result", [])

    links = [video["link"] for video in results]
    return links


if __name__ == "__main__":
    query = input("Enter search query: ")
    links = get_youtube_links(query, max_results=5)

    if links:
        print("\nTop results:\n")
        for i, link in enumerate(links, 1):
            print(f"{i}. {link}")
    else:
        print("No results found.")
