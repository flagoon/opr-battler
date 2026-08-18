from typing import TypedDict


class ArmyBook(TypedDict):
    uid: str
    enabledGameSystems: list[int]
    name: str
    genericName: str
    hint: str
    background: str
    unitCount: int
    modifiedAt: str
    editedAt: str
    official: bool
    versionString: str
    coverImagePath: str
    bannerImagePath: str
    visibility: int
    factionId: str | None
    factionName: str | None
    factionRelation: str | None
    factionNameGeneric: str | None
    userId: str
    balanceValid: bool
    balanceValidReason: int
    popularity: int
    downvotes: int
    flavouredUid: str


def map_army(army: ArmyBook):
    return {
        "uid": army["uid"],
        "name": army["name"],
        "desc": army["background"],
        "cover_image": army["coverImagePath"],
    }


def map_all_armies(armies: list[ArmyBook]):
    """
    Get list of armies from backend, and get only important data from it
    """
    mapped_army = map(map_army, armies)

    return mapped_army
