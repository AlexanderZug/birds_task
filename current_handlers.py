import json
from typing import Any

import uiweb as uiweb
from pony.orm import db_session, select

from db import db, Bird
from utils import CUSTOM_CARDS


def custom_cards_on_open(
        hashMap: uiweb.uiweb.javahashMap, _files: Any = None, _data: Any = None
) -> uiweb.uiweb.javahashMap:

    CUSTOM_CARDS["customcards"]["cardsdata"] = []
    with db_session:
        all_birds = select(p for p in Bird)
        for bird in all_birds:
            new_bird = {
                "key": str(bird.id),
                "number": "№. " + str(bird.id),
                "name": f"Название птицы: {bird.name}",
                "color": f"Цвет окраса: {bird.color}",
            }
            CUSTOM_CARDS["customcards"]["cardsdata"].append(new_bird)
        if not hashMap.containsKey("cards"):
            hashMap.put(
                "cards",
                json.dumps(CUSTOM_CARDS, ensure_ascii=False).encode("utf8").decode(),
            )

    return hashMap


def btn_add_bird_on_main_screen(
        hashMap: uiweb.uiweb.javahashMap, _files: Any = None, _data: Any = None
) -> uiweb.uiweb.javahashMap:
    hashMap.put("ShowScreen", "Добавить птицу")

    return hashMap


def btn_add_bird(
        hashMap: uiweb.uiweb.javahashMap, _files: Any = None, _data: Any = None
) -> uiweb.uiweb.javahashMap:
    with db_session:
        Bird(name=hashMap.get("name"), color=hashMap.get("color"))
        db.commit()
        hashMap.put("toast", "Птица добавлена")
    hashMap.put("ShowScreen", "Список птиц")
    hashMap.put("RefreshScreen", "")

    return hashMap
