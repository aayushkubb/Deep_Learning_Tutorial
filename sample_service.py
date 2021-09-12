import argparse
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/post', methods=['POST'])
def post_route():
    if request.method == 'POST':
        data = request.get_json(force=True)
        image=data['image']
        data_dict = {'class':"dog"}   
        return jsonify(data_dict)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port="5050")