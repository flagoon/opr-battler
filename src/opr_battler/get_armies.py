import requests

from opr_battler.army_book import ArmyBook
from opr_battler.constants.urls import ALL_ARMIES


def get_armies() -> list[ArmyBook]:
    """
    Call for the army list
    """
    armies = requests.get(ALL_ARMIES)

    return armies.json()
