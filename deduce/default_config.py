
"""Default configuration for Deduce."""

DEFAULT_CONFIG = {
    "adjacent_annotations_slack": "[\\. \\-]?[\\. ]?",
    "resolve_overlap_strategy": {
        "attributes": [
            "priority",
            "length"
        ],
        "ascending": [
            False,
            False
        ]
    },
    "redactor_open_char": "[",
    "redactor_close_char": "]",
    "annotators": {
        "prefix_with_initial": {
            "annotator_type": "deduce.annotator.TokenPatternAnnotator",
            "group": "names",
            "args": {
                "tag": "prefix+initiaal",
                "skip": ["."],
                "pattern": [
                    {
                        "lookup": "prefix"
                    },
                    {
                        "or": [
                            {
                                "lookup": "initial"
                            },
                            {
                                "is_initials": True
                            }
                        ]
                    }
                ]
            }
        },
        "prefix_with_interfix": {
            "annotator_type": "deduce.annotator.TokenPatternAnnotator",
            "group": "names",
            "args": {
                "tag": "prefix+interfix+naam",
                "skip": ["."],
                "pattern": [
                    {
                        "lookup": "prefix"
                    },
                    {
                        "lookup": "interfix"
                    },
                    {
                        "like_name": True
                    }
                ]
            }
        },
        "prefix_with_name": {
            "annotator_type": "deduce.annotator.TokenPatternAnnotator",
            "group": "names",
            "args": {
                "tag": "prefix+naam",
                "skip": ["."],
                "pattern": [
                    {
                        "lookup": "prefix"
                    },
                    {
                        "and": [
                            {
                                "like_name": True
                            },
                            {
                                "neg_lookup": "whitelist"
                            }
                        ]
                    }
                ]
            }
        },
        "interfix_with_name": {
            "annotator_type": "deduce.annotator.TokenPatternAnnotator",
            "group": "names",
            "args": {
                "tag": "interfix+achternaam",
                "skip": [],
                "pattern": [
                    {
                        "lookup": "interfix"
                    },
                    {
                        "and": [
                            {
                                "lookup": "interfix_surname"
                            },
                            {
                                "neg_lookup": "whitelist"
                            }
                        ]
                    }
                ]
            }
        },
        "initial_with_name": {
            "annotator_type": "deduce.annotator.TokenPatternAnnotator",
            "group": "names",
            "args": {
                "tag": "initiaal+naam",
                "skip": ["."],
                "pattern": [
                    {
                        "lookup": "initial"
                    },
                    {
                        "and": [
                            {
                                "like_name": True
                            },
                            {
                                "neg_lookup": "whitelist"
                            },
                            {
                                "neg_lookup": "prefix"
                            }
                        ]
                    }
                ]
            }
        },
        "initial_interfix": {
            "annotator_type": "deduce.annotator.TokenPatternAnnotator",
            "group": "names",
            "args": {
                "tag": "initiaal+interfix+naam",
                "skip": ["."],
                "pattern": [
                    {
                        "lookup": "initial"
                    },
                    {
                        "lookup": "interfix"
                    },
                    {
                        "like_name": True
                    }
                ]
            }
        },
        "first_name_lookup": {
            "annotator_type": "docdeid.process.MultiTokenLookupAnnotator",
            "group": "names",
            "args": {
                "tag": "voornaam",
                "overlapping": True,
                "lookup_values": "first_name"
            }
        },
        "surname_lookup": {
            "annotator_type": "docdeid.process.MultiTokenLookupAnnotator",
            "group": "names",
            "args": {
                "tag": "achternaam",
                "overlapping": True,
                "lookup_values": "surname"
            }
        },
        "patient_name": {
            "annotator_type": "deduce.annotator.PatientNameAnnotator",
            "group": "names",
            "args": {
                "tag": "_"
            }
        },
        "name_context": {
            "annotator_type": "deduce.annotator.ContextAnnotator",
            "group": "names",
            "args": {
                "iterative": True,
                "pattern": [
                    {
                        "name": "interfix_right",
                        "direction": "right",
                        "pre_tag": [
                            "initiaal",
                            "naam",
                            "voornaam",
                            "achternaam",
                            "voornaam_patient",
                            "achternaam_patient"
                        ],
                        "tag": "{tag}+interfix+achternaam",
                        "skip": [".", "-"],
                        "pattern": [
                            {
                                "lookup": "interfix"
                            },
                            {
                                "like_name": True
                            }
                        ]
                    },
                    {
                        "name": "initial_left",
                        "direction": "left",
                        "pre_tag": [
                            "initiaal",
                            "naam",
                            "voornaam",
                            "achternaam",
                            "voornaam_patient",
                            "achternaam_patient",
                            "interfix"
                        ],
                        "tag": "initiaal+{tag}",
                        "skip": ["."],
                        "pattern": [
                            {
                                "lookup": "initial"
                            }
                        ]
                    },
                    {
                        "name": "naam_left",
                        "direction": "left",
                        "pre_tag": [
                            "naam",
                            "voornaam",
                            "achternaam",
                            "voornaam_patient",
                            "achternaam_patient"
                        ],
                        "tag": "naam+{tag}",
                        "skip": ["-"],
                        "pattern": [
                            {
                                "and": [
                                    {
                                        "like_name": True
                                    },
                                    {
                                        "neg_lookup": "whitelist"
                                    },
                                    {
                                        "neg_lookup": "prefix"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "naam_right",
                        "direction": "right",
                        "pre_tag": [
                            "prefix",
                            "initiaal",
                            "naam",
                            "voornaam",
                            "achternaam",
                            "voornaam_patient",
                            "achternaam_patient",
                            "interfix"
                        ],
                        "tag": "{tag}+naam",
                        "skip": ["-"],
                        "pattern": [
                            {
                                "and": [
                                    {
                                        "like_name": True
                                    },
                                    {
                                        "neg_lookup": "whitelist"
                                    },
                                    {
                                        "neg_lookup": "prefix"
                                    }
                                ]
                            }
                        ]
                    },
                    {
                        "name": "prefix_left",
                        "direction": "left",
                        "pre_tag": [
                            "prefix",
                            "initiaal",
                            "naam",
                            "voornaam",
                            "achternaam",
                            "voornaam_patient",
                            "achternaam_patient",
                            "interfix"
                        ],
                        "tag": "prefix+{tag}",
                        "skip": ["."],
                        "pattern": [
                            {
                                "and": [
                                    {
                                        "lookup": "prefix"
                                    }
                                ]
                            }
                        ]
                    }
                ]
            }
        },
        "eponymous_disease": {
            "annotator_type": "docdeid.process.MultiTokenLookupAnnotator",
            "group": "names",
            "args": {
                "lookup_values": "eponymous_disease",
                "tag": "pseudo_name",
                "overlapping": True
            }
        },
        "placename": {
            "annotator_type": "docdeid.process.MultiTokenLookupAnnotator",
            "group": "locations",
            "args": {
                "lookup_values": "placename",
                "overlapping": True,
                "tag": "locatie"
            }
        },
        "street_pattern": {
            "annotator_type": "deduce.annotator.TokenPatternAnnotator",
            "group": "locations",
            "args": {
                "pattern": [
                    {
                        "re_match": "[A-Z][a-z]+(baan|bolwerk|dam|dijk|dreef|drf|dyk|gr|gracht|hf|hof|kade|laan|ln|markt|mrkt|pad|park|pd|plantsoen|plein|pln|plnts|prk|singel|sngl|st|steeg|stg|str|straat|weg|wg)$"
                    }
                ],
                "tag": "straat",
                "priority": 1
            }
        },
        "street_lookup": {
            "annotator_type": "docdeid.process.MultiTokenLookupAnnotator",
            "group": "locations",
            "args": {
                "lookup_values": "street",
                "overlapping": True,
                "tag": "straat",
                "priority": 1
            }
        },
        "housenumber": {
            "annotator_type": "deduce.annotator.ContextAnnotator",
            "group": "locations",
            "args": {
                "iterative": True,
                "pattern": [
                    {
                        "name": "housenumber_right",
                        "direction": "right",
                        "pre_tag": [
                            "straat"
                        ],
                        "tag": "{tag}+huisnummer",
                        "skip": [],
                        "pattern": [
                            {
                                "re_match": "\\d{1,4}$"
                            }
                        ]
                    },
                    {
                        "name": "housenumber_housenumberletter_right",
                        "direction": "right",
                        "pre_tag": [
                            "straat"
                        ],
                        "tag": "{tag}+huisnummer+huisnummerletter",
                        "skip": [],
                        "pattern": [
                            {
                                "re_match": "\\d{1,4}[a-zA-Z]$"
                            }
                        ]
                    },
                    {
                        "name": "housenumberletter_right",
                        "direction": "right",
                        "pre_tag": [
                            "huisnummer"
                        ],
                        "tag": "{tag}+huisnummerletter",
                        "skip": [],
                        "pattern": [
                            {
                                "re_match": "[a-zA-Z]$"
                            }
                        ]
                    }
                ]
            }
        },
        "postal_code": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "locations",
            "args": {
                "regexp_pattern": "(\\d{4}([A-Za-z]{2}| [A-Z]{2}))(?<!mg|MG|gr|ie)(\\W|$)",
                "capturing_group": 1,
                "tag": "locatie"
            }
        },
        "postbus": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "locations",
            "args": {
                "regexp_pattern": "([Pp]ostbus\\s\\d{1,5}(\\.\\d{2,4})?)",
                "tag": "locatie",
                "pre_match_words": ["postbus"]
            }
        },
        "hospital": {
            "annotator_type": "docdeid.process.MultiTokenLookupAnnotator",
            "group": "institutions",
            "args": {
                "lookup_values": "hospital",
                "overlapping": True,
                "tag": "ziekenhuis"
            }
        },
        "institution": {
            "annotator_type": "docdeid.process.MultiTokenLookupAnnotator",
            "group": "institutions",
            "args": {
                "lookup_values": "healthcare_institution",
                "overlapping": True,
                "tag": "zorginstelling"
            }
        },
        "date_dmy_1": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "dates",
            "args": {
                "regexp_pattern": "(?<!\\d)(([1-9]|0[1-9]|[12][0-9]|3[01])(?P<sep>[-/\\. ])([1-9]|0[1-9]|1[012])(?P=sep)((19|20|\\'|`)?\\d{2}))(?!\\d)",
                "tag": "datum",
                "capturing_group": 1
            }
        },
        "date_dmy_2": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "dates",
            "args": {
                "regexp_pattern": "(?i)(?<!\\d)(([1-9]|0[1-9]|[12][0-9]|3[01])[-/\\. ]{,2}(januari|jan|februari|feb|maart|mrt|april|apr|mei|juni|jun|juli|jul|augustus|aug|september|sep|sept|oktober|okt|november|nov|december|dec)[-/\\. ]((19|20|\\'|`)?\\d{2}))(?!\\d)",
                "tag": "datum",
                "capturing_group": 1,
                "pre_match_words": ["januari", "jan", "februari", "feb", "maart", "mrt", "april", "apr", "mei", "juni", "jun", "juli", "jul", "augustus", "aug", "september", "sep", "sept", "oktober", "okt", "november", "nov", "december", "dec"]
            }
        },
        "date_ymd_1": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "dates",
            "args": {
                "regexp_pattern": "(?<!\\d)(((19|20|\\'|`)\\d{2})(?P<sep>[-/\\. ])([1-9]|0[1-9]|1[012])(?P=sep)([1-9]|0[1-9]|[12][0-9]|3[01]))(\\D|$)",
                "tag": "datum",
                "capturing_group": 1
            }
        },
        "date_ymd_2": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "dates",
            "args": {
                "regexp_pattern": "(?i)(?<!\\d)(((19|20|\\'|`)\\d{2})[-/\\. ]{,2}(januari|jan|februari|feb|maart|mrt|april|apr|mei|juni|jun|juli|jul|augustus|aug|september|sep|sept|oktober|okt|november|nov|december|dec)[-/\\. ]([1-9]|0[1-9]|[12][0-9]|3[01]))(?!\\d)",
                "tag": "datum",
                "capturing_group": 1,
                "pre_match_words": ["januari", "jan", "februari", "feb", "maart", "mrt", "april", "apr", "mei", "juni", "jun", "juli", "jul", "augustus", "aug", "september", "sep", "sept", "oktober", "okt", "november", "nov", "december", "dec"]
            }
        },
        "age": {
            "annotator_type": "deduce.annotator.RegexpPseudoAnnotator",
            "group": "ages",
            "args": {
                "regexp_pattern": "(?i)(?<![\\d,\\.])((1?\\d?\\d)([\\.,]5)?(-(1?\\d?\\d)([\\.,]5)?)?)([ -](jaar|jarig|jarige|jr))(?!\\w)",
                "pre_pseudo": ["<", "al", "co", "controle", "de", "elke", "gedurende", "na", "nog", "ongeveer", "over", "policontrole", "sinds", "up", "vanaf"],
                "post_pseudo": ["aanwezig", "gebruikt", "geleden", "gerookt", "gestaakt", "gestopt", "getrouwd", "na", "naar", "nadien"],
                "pre_match_words": ["jaar", "jarig", "jarige", "jr"],
                "tag": "leeftijd",
                "capturing_group": 1
            }
        },
        "bsn": {
            "annotator_type": "deduce.annotator.BsnAnnotator",
            "group": "identifiers",
            "args": {
                "bsn_regexp": "(?<!\\d)(\\d{9})(?!\\d)",
                "capture_group": 1,
                "priority": 100,
                "tag": "bsn"
            }
        },
        "identifier": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "identifiers",
            "args": {
                "regexp_pattern": "\\d{7,}",
                "tag": "id"
            }
        },
        "phone": {
            "annotator_type": "deduce.annotator.PhoneNumberAnnotator",
            "group": "phone_numbers",
            "args": {
                "phone_regexp": "(?<!\\d)(\\(?(0031|\\+31|0)(1[035]|2[0347]|3[03568]|4[03456]|5[0358]|6|7|88|800|91|90[069]|[1-5]\\d{2})\\)?) ?-? ?((\\d{2,4}[ -]?)+\\d{2,4})",
                "min_digits": 9,
                "max_digits": 11,
                "tag": "telefoonnummer"
            }
        },
        "email": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "email_addresses",
            "args": {
                "regexp_pattern": "(([-a-zA-Z0-9:%._\\+~#=]{1,256})@([-a-zA-Z0-9:%._\\+~#=]{1,256})(\\.)(com|net|org|co|us|uk|nl|be|fr|sp|gov|nu))",
                "tag": "emailadres",
                "pre_match_words": ["com", "net", "org", "co", "us", "uk", "nl", "be", "fr", "sp", "gov", "nu"]
            }
        },
        "url": {
            "annotator_type": "docdeid.process.RegexpAnnotator",
            "group": "urls",
            "args": {
                "regexp_pattern": "((https?:\\/\\/(?:www\\.)?)?([-a-zA-Z0-9:%._\\+~#=]{1,256})(\\.)(com|net|org|co|us|uk|nl|be|fr|sp|gov|nu)(\\b)([():%_\\+.~,]*[-a-zA-Z-0-9#?&/=]+)*)",
                "tag": "url",
                "pre_match_words": ["com", "net", "org", "co", "us", "uk", "nl", "be", "fr", "sp", "gov", "nu"]
            }
        }
    }
}