# Eileen's Test Case Report
## Analyzer `ar_std_folding`
```
"ar_std_folding": {
    "tokenizer": "whitespace",
    "position_increment_gap": 512,
    "char_filter": [
      "to_spaces"
    ],
    "filter": [
      "ar_folding",
      "lowercase"
    ]
}
```

### Sentence 2, two charaters
```
{
    "analyzer": "ar_std_folding",
    "text": "مجلة جيل العلوم الإنسانية والاجتماعية"
}
```

Response
```
{
    "tokens": [
        {
            "token": "مجلة",
            "start_offset": 0,
            "end_offset": 4,
            "type": "word",
            "position": 0
        },
        {
            "token": "جيل",
            "start_offset": 5,
            "end_offset": 8,
            "type": "word",
            "position": 1
        },
        {
            "token": "العلوم",
            "start_offset": 9,
            "end_offset": 15,
            "type": "word",
            "position": 2
        },
        {
            "token": "الإنسانية",
            "start_offset": 16,
            "end_offset": 26,
            "type": "word",
            "position": 3
        },
        {
            "token": "والاجتماعية",
            "start_offset": 27,
            "end_offset": 38,
            "type": "word",
            "position": 4
        }
    ]
}
```
### Sentence 1 one charater
```
{
    "analyzer": "ar_std_folding",
    "text": "مجلة جيل العلوم الإنسانية والاجتماعية"
}

{
    "tokens": [
        {
            "token": "مجلة",
            "start_offset": 0,
            "end_offset": 4,
            "type": "word",
            "position": 0
        },
        {
            "token": "جيل",
            "start_offset": 5,
            "end_offset": 8,
            "type": "word",
            "position": 1
        },
        {
            "token": "العلوم",
            "start_offset": 9,
            "end_offset": 15,
            "type": "word",
            "position": 2
        },
        {
            "token": "الانسانية", # no hamza
            "start_offset": 16,
            "end_offset": 25,
            "type": "word",
            "position": 3
        },
        {
            "token": "والاجتماعية",
            "start_offset": 26,
            "end_offset": 37,
            "type": "word",
            "position": 4
        }
    ]
}
```

## Analyzer `ar_std`
```
"ar_std": {
  "tokenizer": "whitespace",
  "position_increment_gap": 512,
  "char_filter": [
    "to_spaces"
  ],
  "filter": [
    "icu_folding",
    "lowercase"
  ]
}
```
### Sentence 2 two charaters
```
{
    "analyzer": "ar_std",
    "text": "مجلة جيل العلوم الإنسانية والاجتماعية"
}


{
    "tokens": [
        {
            "token": "مجله",
            "start_offset": 0,
            "end_offset": 4,
            "type": "word",
            "position": 0
        },
        {
            "token": "جيل",
            "start_offset": 5,
            "end_offset": 8,
            "type": "word",
            "position": 1
        },
        {
            "token": "العلوم",
            "start_offset": 9,
            "end_offset": 15,
            "type": "word",
            "position": 2
        },
        {
            "token": "الانسانيه",
            "start_offset": 16,
            "end_offset": 26,
            "type": "word",
            "position": 3
        },
        {
            "token": "والاجتماعيه",
            "start_offset": 27,
            "end_offset": 38,
            "type": "word",
            "position": 4
        }
    ]
}
```

### Sentence 1 one charater
```
{
    "analyzer": "ar_std",
    "text":  "مجلة جيل العلوم الإنسانية والاجتماعية"
}


{
    "tokens": [
        {
            "token": "مجله",
            "start_offset": 0,
            "end_offset": 4,
            "type": "word",
            "position": 0
        },
        {
            "token": "جيل",
            "start_offset": 5,
            "end_offset": 8,
            "type": "word",
            "position": 1
        },
        {
            "token": "العلوم",
            "start_offset": 9,
            "end_offset": 15,
            "type": "word",
            "position": 2
        },
        {
            "token": "الانسانيه",
            "start_offset": 16,
            "end_offset": 25,
            "type": "word",
            "position": 3
        },
        {
            "token": "والاجتماعيه",
            "start_offset": 26,
            "end_offset": 37,
            "type": "word",
            "position": 4
        }
    ]
}
```

## Analyzer ar_std_lem
```
"ar_std_lem": {
  "tokenizer": "whitespace",
  "position_increment_gap": 512,
  "char_filter": [
    "to_spaces"
  ],
  "filter": [
    "icu_folding",
    "lowercase",
    "arabic_stemmer"
  ]
}
```
### Sentence 2 two charaters
```
{
    "analyzer": "ar_std_lem",
    "text":  "مجلة جيل العلوم الإنسانية والاجتماعية"
}

{
    "tokens": [
        {
            "token": "مجل",
            "start_offset": 0,
            "end_offset": 4,
            "type": "word",
            "position": 0
        },
        {
            "token": "جيل",
            "start_offset": 5,
            "end_offset": 8,
            "type": "word",
            "position": 1
        },
        {
            "token": "علوم",
            "start_offset": 9,
            "end_offset": 15,
            "type": "word",
            "position": 2
        },
        {
            "token": "انسان",
            "start_offset": 16,
            "end_offset": 26,
            "type": "word",
            "position": 3
        },
        {
            "token": "اجتماع",
            "start_offset": 27,
            "end_offset": 38,
            "type": "word",
            "position": 4
        }
    ]
}
```

### Sentence 1 one charater
```
{
    "analyzer": "ar_std_lem",
    "text":  "مجلة جيل العلوم الإنسانية والاجتماعية"
}

{
    "tokens": [
        {
            "token": "مجل",
            "start_offset": 0,
            "end_offset": 4,
            "type": "word",
            "position": 0
        },
        {
            "token": "جيل",
            "start_offset": 5,
            "end_offset": 8,
            "type": "word",
            "position": 1
        },
        {
            "token": "علوم",
            "start_offset": 9,
            "end_offset": 15,
            "type": "word",
            "position": 2
        },
        {
            "token": "انسان",
            "start_offset": 16,
            "end_offset": 25,
            "type": "word",
            "position": 3
        },
        {
            "token": "اجتماع",
            "start_offset": 26,
            "end_offset": 37,
            "type": "word",
            "position": 4
        }
    ]
}
```
