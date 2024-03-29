# Backend test queries

## curl - POST
curl -X POST \
 http://localhost:8200/begreper/ \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json' \
 -d ' {
        "anbefaltTerm": "thomas-01",
        "status": "utkast",
        "ansvarligVirksomhet": {
           "id": "986105174"
       }
}' -v

## curl - PATCH
curl -X PATCH \
 http://localhost:8200/begreper/a98a795d-d702-46d6-ad36-ed108645ca85 \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json' \
 -d ' {
        "anbefaltTerm": "curl-1-b",
        "status": "utkast",
        "ansvarligVirksomhet": {
           "id": "910244132"
       }
}' -v

## curl - PATCH (2)
curl -X PATCH \
 http://localhost:8200/begreper/a98a795d-d702-46d6-ad36-ed108645ca85 \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json' \
 -d ' {
        "anbefaltTerm": "curl-1-c",
        "kildebeskrivelse": {
            "forholdTilKilde": "egendefinert",
            "kilde": [
            {
                "uri": "https://brreg.no",
                "tekst": "brreg"
            }
            ]
        }
}' | jq

## curl - PATCH (3)
curl -X PATCH \
 http://localhost:8200/begreper/a98a795d-d702-46d6-ad36-ed108645ca85 \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json' \
 -d ' {
        "kildebeskrivelse": {
            "forholdTilKilde": "egendefinert",
            "kilde": [
                {
                    "uri": "https://brreg.no",
                    "tekst": "brreg"
                },
                {
                    "uri": "https://test.brreg.no",
                    "tekst": "dev.brreg"
                },
                {
                    "uri": "https://dev.brreg.no",
                    "tekst": "test.brreg"
                }
            ]
        }
}' | jq

## curl - PATCH (3)
curl -X PATCH \
 http://localhost:8200/begreper/a98a795d-d702-46d6-ad36-ed108645ca85 \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json' \
 -d ' {
        "anbefaltTerm": "curl-1-c"
}' -v


## curl - GET
curl http://localhost:8200/begreper/05458701-21e1-4167-b8b2-fae8dc118ecd \
 -H 'cache-control: no-cache' \
 -H 'content-type: application/json' | jq

curl 'http://localhost:8200/begreper/a98a795d-d702-46d6-ad36-ed108645ca85' | jq
curl "http://localhost:8200/begreper/a98a795d-d702-46d6-ad36-ed108645ca85" | jq

curl http://localhost:8200/begreper/a98a795d-d702-46d6-ad36-ed108645ca85 -H 'content-type: application/json' | jq

curl http://localhost:8202/986105174/05458701-21e1-4167-b8b2-fae8dc118ecd -H 'content-type: application/json'




## fetch
var myJson = { 
    anbefaltTerm: 'fetch-1',
    status: 'utkast',
    ansvarligVirksomhet: { 
        id: '910244132'
    }
};
fetch("http://localhost:8200/begreper/", myJson);