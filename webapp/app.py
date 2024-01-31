from flask import Flask, jsonify, request, Response
from sqlalchemy import create_engine, exc
from dotenv import load_dotenv
import os

# Load environment variables from environment.env file
load_dotenv()

app = Flask(__name__)

# Load database connection string from environment variable
#DB_CONN = os.getenv('DB_CONN')
DB_CONN  = "postgresql://sjuser:sjpassword@localhost/sjdatabase"

@app.route('/healthz')

def healthCheck():
    response = Response()
    if request.data:
        response.status_code=400
        return response
    
    elif request.method != 'GET':
        response.status_code=405
        return response

    # try:
    #     engine = create_engine(DB_CONN)
    #     engine.connect()
    # except  Exception as e:
    #     print(f"e --> {e}")
    #     return '', 503

    response = jsonify({})
    response.headers['Cache-Control'] = 'no-cache'
    return response, 200

if __name__ == '__main__':
    app.run(debug=True)
