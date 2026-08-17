import requests


def get_armies():
    """
    Call for the army list
    """
    armies = requests.get(
        "https://army-forge.onepagerules.com/api/army-books?filters=official&gameSystemSlug=grimdark-future&searchText=&page=1&unitCount=0&balanceValid=false&customRules=true&fans=false&sortBy=null"
    )
    return armies
