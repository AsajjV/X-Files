# import necessary libraries
from flask import (
    Flask,
    render_template,
    jsonify,
    request)

import pandas as pd

from flask_sqlalchemy import SQLAlchemy

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

app = Flask(__name__)


conn = 'mysql://root:15LoveCraft12@127.0.0.1/FRL_Project2_db'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)
# data = pd.read_sql("SELECT distinct State FROM mil_base", conn)
# data = pd.read_sql("SELECT * FROM mil_base where State = 'Virginia'", conn)
# print(data)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/states")
def test():

    # df = pd.DataFrame(data, columns=['State', 'Longitude', 'Latitude'])
    data = pd.read_sql("SELECT distinct State FROM ufo_all_data", conn)
    df = pd.DataFrame(data, columns=['State'])
    # print(df)
    state_list = df['State'].tolist()
    # Format the data for Plotly
#     plot_trace = {
#         "x": df["State"].values.tolist()
#         # "type": "bar"
#    }
    # return jsonify(plot_trace)
    return jsonify(state_list)

    
@app.route("/states/<state>")

def state_metadata(state):
    """Return the MetaData for a chosen state."""
    
    print(state)

    results = pd.read_sql("SELECT State, Sightings_Total, Military_Bases, Marijuana FROM ufo_all_data where State = '"+ state+"'", conn)
    # Create a dictionary entry for each row of metadata information
    # print(type(results))
    
    # sql = ('SELECT State, Sightings_Total, Military_Bases, Marijuana FROM ufo_all_data where State = state')
    # results = db.engine.execute(sql)
    # print(results)
    state_metadata = results.to_dict('records')

    # for result in results.iterrows:
    #     print(result)

        # state_metadata["State"] = result[0]
        # state_metadata["Sightings_Total"] = result[1]
        # state_metadata["Military_Bases"] = result[2]
        # state_metadata["Marijuana"] = result[3]

    # print(state_metadata)
    
    return jsonify(state_metadata)


if __name__ == "__main__":
    # app.run(port=5001)
    app.run(debug=True)

