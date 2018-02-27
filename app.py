from flask import Flask, render_template, request
import pymongo
import json


app = Flask(__name__)

def setup():
    connection = pymongo.MongoClient('homer.stuy.edu')
    connection.drop_database('Kanto')
    
    global db
    db = connection['Kanto']
    global collection
    collection = db['pokemon']
    data = json.load(open('pokemon.json'))['pokemon']
    for pokemon in data:
        collection.insert(pokemon)


@app.route('/')
def root():
    return render_template("form.html")

@app.route('/name', methods = ['POST','GET'])
def findName():
    name = request.form['pokemon']
    pokemon = collection.find( {'name': name} )
    for each in pokemon:
        pokename = each['name']
        pokeimg = each['img']
        pokeheight = each['height']
        pokeweight = each['weight']
    return render_template("pokemon.html", query="name", name=pokename, image=pokeimg, height=pokeheight, weight=pokeweight)

@app.route('/eggtype', methods = ['POST','GET'])
def findEggType():
    eggtype = request.form['eggtype']
    pokemon = collection.find( {'egg': eggtype} )
    pokelist = []
    for each in pokemon:
        sublist = []
        sublist.append(each['name'])
        sublist.append(each['img'])
        sublist.append(each['height'])
        sublist.append(each['weight'])
        pokelist.append(sublist)
    return render_template("pokemon.html", query="eggtype", pokelist=pokelist)

if __name__ == '__main__':
    setup()
    app.run(debug=True)
