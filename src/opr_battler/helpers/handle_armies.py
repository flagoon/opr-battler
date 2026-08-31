from opr_battler.army_book import ArmyBook


def create_new_faction_object(army):
    return {
        "uid": army.get("uid"),
        "name": army.get("factionName"),
        "coverImagePath": army.get("coverImagePath"),
        "members": [{"uid": army.get("uid"), "name": army.get("name")}],
    }


def handle_armies(armies: list[ArmyBook]):
    new_armies = {}

    # army can have a factionName, which will make it a part of a faction
    for army in armies:
        # simplify the new armies, to create cards we only need the uid, name (or factionName) and list of facation members
        if army.get("factionName") is None:
            new_armies[army.get("name")] = {
                "uid": army.get("uid"),
                "name": army.get("name"),
                "coverImagePath": army.get("coverImagePath")
                if army.get("coverImagePath").startswith("https://")
                else f"https://army-forge.opr-cdn.com/{army.get('coverImagePath')}",
                "members": [],
            }
        else:
            # army is part of the faction and will have members.
            # It can be a main faction, like battle brothers, or part of battle brothers, like blood brothers.
            # if it has faction name, but doesn't have factionId, it means it's a main faction
            # if it has both, then it's a subfaction
            if army.get("factionId") is None:
                # it can be already in new_armies, or not.
                faction_army = new_armies.get(army.get("factionName"))
                if faction_army is None:
                    new_armies[army.get("factionName")] = create_new_faction_object(
                        army
                    )
                else:
                    # this is primary faction, so it has to be on first position on the members list
                    faction_army["members"].insert(
                        0, {"uid": army.get("uid"), "name": army.get("name")}
                    )
            else:
                faction_army = new_armies.get(army.get("factionName"))
                if faction_army is None:
                    new_armies[army.get("factionName")] = create_new_faction_object(
                        army
                    )
                else:
                    faction_army["members"].append(
                        {"uid": army.get("uid"), "name": army.get("name")}
                    )

    # Sort factions/armies
    return sorted(new_armies.values(), key=lambda army: army["name"].lower())
