from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def root():
    return render_template("form.html")

@app.route('/name')
def findName():
    name = request.form['pokemon']
    pokemon = collection.find( {'name': name} )
    for each in pokemon:
        pokename = each['name']
        pokeimg = each['img']
        pokeheight = each['height']
        pokeweight = each['weight']
    return render_template("pokemon.html", name=pokename, image=pokeimg, height=pokeheight, weight=pokeweight)

if __name__ == '__main__':
    app.run(debug=True)
