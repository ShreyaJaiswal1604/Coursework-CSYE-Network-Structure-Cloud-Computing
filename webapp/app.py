from flask import Flask, jsonify, request
from sqlalchemy import create_engine, exc
from dotenv import load_dotenv
import os

# Load environment variables from environment.env file
load_dotenv()

app = Flask(__name__)

# Load database connection string from environment variable
DB_CONN = os.getenv('DB_CONN')
print("=========================")
print(DB_CONN)
print("=========================")

@app.route('/healthz', methods=['GET'])
def healthCheck():
    if request.method != 'GET':
        return jsonify({'error': 'Method Not Allowed'}), 405 

    if request.data:
        return jsonify({'error': 'Bad Request'}), 400

    try:
        engine = create_engine(DB_CONN)
        engine.connect()
    except exc.OperationalError:
        return '', 503

    response = jsonify({})
    response.headers['Cache-Control'] = 'no-cache'
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
