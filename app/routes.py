from app import app
from flask import render_template, redirect, url_for, request
import json
import os
import numpy as np
from matplotlib import colors, pyplot as plt
from app.models.product import Product


@app.route('/')
def index():
    return render_template("index.html.jinja")

@app.route('/extract', methods = ["POST", "GET"])
def extract():
    if request.method== "POST":
        product_id=request.form.get("product_id")
        product = Product(product_id)
        product.extract_name()
        if product.product_name:
            product.extract_opinions()
        else:
            pass

        if not os.path.exists("app/opinions"):
            os.makedirs("app/opinions")

        with open(f"app/opinions/"+product_id+".json", "w", encoding="UTF-8") as jf: 
            json.dump(all_opinions, jf, indent=4, ensure_ascii=False)
        return redirect (url_for('product',product_id=product_id))
    else:
        return render_template("extract.html.jinja")


@app.route('/products')
def products():
    products = [filename.split(".")[0] for filename in os.listdir("app/opinions")]
    return render_template("products.html.jinja", products = products)



@app.route('/author')
def author():
    return render_template("author.html.jinja")



@app.route('/product/<product_id>')
def product(product_id):
    opinions = pd.read_json(f"opinions/"+id+".json")
    opinions["stars"] = opinions["stars"].map(lambda x: float(x.split("/")[0].replace(",", ".")))

    stats = {
        "opinions_count" : len(opinions),
        "pros_count" : opinions["pros"].map(bool).sum(),
        "cons_count" : opinions["cons"].map(bool).sum(),
        "average_score" : opinions["stars"].mean().round(2),
    }

    if not os.path.exists("app/plots"):
                os.makedirs("app/plots")

    recomendation = opinions["recomendation"].value_counts(dropna=False).sort_index().reindex(["Nie polecam", "Polecam", None], fill_value=0)
    recomendation.plot.pie(
        label="",
    autopct = lambda p: '{:.1f}%'.format(round(p)) if p>0 else '',
        colors = ["crimson", "forestgreen", "lightskyblue"],
        labels = ["Nie polecam", "Polecam", "Nie mam zdania"]
    )
    plt.title("Rekomendacje")
    plt.savefig(f"plots/{id}_recommendations.png")
    plt.close()


    stars = opinions["stars"].value_counts().sort_index().reindex(list(np.arange(0,5.5,0.5)), fill_value=0)
    stars.plot.bar(
        color = "pink"
    )
    plt.title("Oceny produktu")
    plt.xlabel("Liczba gwiazdek")
    plt.ylabel("Liczba opinii")
    plt.grid(True, axis="y")
    plt.xticks(rotation= 0)
    plt.savefig(f"plots/{id}_stars.png")
    plt.close()

    return render_template("product.html.jinja", product_id=product_id, stats=stats, opinions=opinions)