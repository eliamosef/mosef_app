import base64
from io import BytesIO

import plotly
from flask import Flask
from flask import render_template
import pandas as pd
from wordcloud import WordCloud
from PIL import Image
import numpy as np
import random
import spacy
from collections import Counter
import plotly.graph_objects as go
import json

app = Flask(__name__)


def couleur(*args, **kwargs):
    return "rgb(0, 100, {})".format(random.randint(0, 88))


exclure_mots = ['d', 'du', 'de', 'la', 'des', 'le', 'et', 'est', 'elle', 'une', 'en', 'que', 'aux', 'qui', 'ces', 'les',
                'dans', 'sur', 'l', 'un', 'pour', 'par', 'il', 'ou', 'à', 'ce', 'a', 'sont', 'cas', 'plus', 'leur',
                'se', 's', 'vous', 'au', 'c', 'aussi', 'toutes', 'autre', 'comme']

rename = {
    "Horodateur": "timestamp",
    "Courriel": "mail",
    "Nom": "name",
    "Prénom": "first_name",
    "Formation précédente": "q1",
    "Quelles sont les compétences que vous souhaitez acquérir à la suite de ce cours?": "q2"
}

@app.route("/about")
def about():
   staged_data = pd.read_csv("../app_data_wc.csv", sep=",", header=0)
   text = str(staged_data['wc'].values[0])
   
   mask = np.array(Image.open("./resources/cloud.png"))
   mask[mask == 1] = 255
   
   wordcloud = WordCloud(
       background_color='white',
       stopwords= set(exclure_mots),
       max_words=50, mask=mask).generate(text)
   
   wordcloudImage = wordcloud.recolor(color_func = couleur).to_image()
   img = BytesIO()
   wordcloudImage.save(img, 'PNG')
   
   imgword = 'data:image/png;base64,' + base64.b64encode(img.getvalue()).decode('ascii')
   
   lem_data = pd.read_csv("../app_data_lem.csv", sep=",", header=0, skipinitialspace=True)

   lem_data['res'] = list(zip(lem_data.lem, lem_data.wc))
   res = lem_data['res'].tolist()

   size = [y[1] for y in res]
   fig = go.Figure(
        data=[go.Scatter(
            x=[1 for x in res], y=[y[1] for y in res],
            text=[str(x[0]) + "<br>frequence: " + str(x[1]) for x in res],
            mode='markers',
            marker=dict(
                size=size,
                sizemode='area',
                sizeref=0.5 * max(size) / (40. ** 2),
                sizemin=4
            )
        )])

   fig.update_traces(textposition='top center')
   fig.update_layout(showlegend=False)
   fig.update_xaxes(visible=False)
   fig.update_yaxes(visible=False)

   graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

   return render_template('hello.html', wordcloud=imgword, graphJSON=graphJSON)

# @app.route("/")
# def index():
    # staged_data = pd.read_csv("../app_data_wc.csv", sep=",", header=0)
    # text = str(staged_data['wc'].values[0])

    # mask = np.array(Image.open("./resources/cloud.png"))
    # mask[mask == 1] = 255

    # wordcloud = WordCloud(
        # background_color='white',
        # stopwords= set(exclure_mots),
        # max_words=50, mask=mask).generate(text)

    # wordcloudImage = wordcloud.to_image()
    # img = BytesIO()
    # wordcloudImage.save(img, 'PNG')

    # imgword = 'data:image/png;base64,' + base64.b64encode(img.getvalue()).decode('ascii')

    # return render_template('index.html', tables=[staged_data.to_html(classes='data')],
                           # titles=staged_data.columns.values, wordcloud=imgword)


# @app.route("/chart")
# def chart():
    # lem_data = pd.read_csv("../app_data_lem.csv", sep=",", header=0, skipinitialspace=True)

    # lem_data['res'] = list(zip(lem_data.lem, lem_data.wc))
    # res = lem_data['res'].tolist()

    # size = [y[1] for y in res]
    # fig = go.Figure(
        # data=[go.Scatter(
            # x=[1 for x in res], y=[y[1] for y in res],
            # text=[x[0] + "<br>frequence: " + str(x[1]) for x in res],
            # mode='markers',
            # marker=dict(
                # size=size,
                # sizemode='area',
                # sizeref=0.5 * max(size) / (40. ** 2),
                # sizemin=4
            # )
        # )])

    # fig.update_traces(textposition='top center')
    # fig.update_layout(showlegend=False)
    # fig.update_xaxes(visible=False)
    # fig.update_yaxes(visible=False)

    # graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
    # header = "Fruit in North America"
    # description = """
    # A academic study of the number of apples, oranges and bananas in the cities of
    # San Francisco and Montreal would probably not come up with this chart.
    # """

    # return render_template('notdash2.html', graphJSON=graphJSON, header=header, description=description)
