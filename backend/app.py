from flask import Flask, jsonify, request
from flask_cors import CORS
from fetch_store_news import fetch_store_news

app = Flask(__name__)
CORS(app)

first_run = True
data_manager = None  

if first_run:
    data_manager = fetch_store_news("Cummins", "keywords.txt")
    first_run = False

# REST API endpoint to retrieve data
@app.route('/api/data', methods=['GET'])
def get_data():
    time_range = request.args.get('timeRange', '7d')
    
    if data_manager is None:
        return jsonify({"error": "Data manager not initialized yet"}), 500
    
    news = data_manager.filter_by_period(time_range)
    
    data = {"items": news}
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)