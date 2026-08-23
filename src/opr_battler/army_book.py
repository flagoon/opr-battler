from typing import TypedDict


class ArmyBook(TypedDict):
    uid: str
    enabledGameSystems: list[int]
    name: str
    genericName: str
    hint: str | None
    background: str
    unitCount: int
    modifiedAt: str
    editedAt: str
    official: bool
    versionString: str
    coverImagePath: str
    bannerImagePath: str | None
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
