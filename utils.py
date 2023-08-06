from typing import Dict, Any

CUSTOM_CARDS: Dict[str, Any] = {
    "customcards": {
        "layout": {
            "type": "LinearLayout",
            "orientation": "vertical",
            "height": "match_parent",
            "width": "match_parent",
            "weight": "0",
            "Elements": [
                {
                    "type": "LinearLayout",
                    "orientation": "horizontal",
                    "height": "wrap_content",
                    "width": "match_parent",
                    "weight": "0",
                    "Elements": [
                        {
                            "type": "LinearLayout",
                            "orientation": "vertical",
                            "height": "wrap_content",
                            "width": "match_parent",
                            "weight": "1",
                            "Elements": [
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@name",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": "",
                                },
                                {
                                    "type": "TextView",
                                    "show_by_condition": "",
                                    "Value": "@color",
                                    "NoRefresh": False,
                                    "document_type": "",
                                    "mask": "",
                                    "Variable": "",
                                },
                            ],
                        }
                    ],
                },
                {
                    "type": "TextView",
                    "show_by_condition": "",
                    "Value": "@number",
                    "NoRefresh": False,
                    "document_type": "",
                    "mask": "",
                    "Variable": "",
                    "TextSize": "-1",
                    "TextColor": "#6F9393",
                    "TextBold": False,
                    "TextItalic": True,
                    "BackgroundColor": "",
                    "width": "wrap_content",
                    "height": "wrap_content",
                    "weight": 0,
                },
            ],
        }
    }
}
