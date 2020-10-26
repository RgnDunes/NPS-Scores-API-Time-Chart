from flask import Flask, request, jsonify
import json
import index

app=Flask(__name__)
index_obj=index.Api_Requests()

@app.route("/getnps")
def getnps():
    response_dict=index_obj.get_NPS_Scores()
    return jsonify(response_dict)

if __name__=="__main__":
    app.run(debug=True)