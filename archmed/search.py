from scholarly import scholarly


def get_search(query: str, count: int = 5, **kwargs):
    try:
        search_query = scholarly.search_pubs(query, sort_by="relevance", **kwargs)
        search = []
        for i in range(count):
            search.append(next(search_query))
        return search
    except:
        return {}
