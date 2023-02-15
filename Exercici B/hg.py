import json

datas = """
    {
    "book":[
        {"title":"La bestia"
         "cover":"Tapa dura"
         "year":"2015"
         "pages":256""
        }
        {"title":"Bibliomania"
         "cover":"Tapa blanda"
         "year":"2022"
         "pages":"328"
        }
        {"title":"Levius"
         "cover":"Tapa dura"
         "year":"2020"
         "pages":"720"
        }
        {"title":"Wanted"
         "cover":"tapa blanda"
         "year":"2011"
         "pages":"208"
        }
    ]
"""


with open("Libros.json","w") as file:
    json.dump(datas,file)