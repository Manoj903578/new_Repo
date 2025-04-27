from flask import Flask, request, jsonify
#this is new API created to post any data 
#This is a simple Flask application that defines a single endpoint to post data.
#It uses the Flask framework to create a web server and handle HTTP requests.
app = Flask(__name__)

@app.route('/item', methods=['POST'])
def post_item():
  data = request.get_json()
  if not data:
    return jsonify({"error": "No data provided"}), 400
  return jsonify({"message": "Item received", "item": data}), 201

if __name__ == '__main__':
  app.run(debug=True)
