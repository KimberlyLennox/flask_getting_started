from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
  """
  Returns the string "Hello, world" to the caller
  """
  return "Hello, world"
  
@app.route("/data/<name>", methods=["GET"])
def hello_name(name): # the name variable being passed in here is the string that the client puts in the <name> part of the url
    return "Hello, {}".format(name)
  
@app.route("/data", methods=["GET"])
def getData():
  """
  Returns the data dictionary below to the caller as JSON
  """
  data = {
    "name": "Kim",
    "message": "Hello there!"
  }
  return jsonify(data) # respond to the API caller with a JSON representation of data. jsonify is important, as it sets response headers that indicate the respose is in JSON as well
  
@app.route("/data", methods=["GET"])
def getName():
    data = {
        "name": "Kim"
        }
    return jsonify(data)

@app.route("/sum", methods=["POST"])
def sum():
    r = request.get_json()
    s = r["a"] + r["b"]
    return jsonify(s), 200
    
@app.route("/distance", methods=["POST"])
def PostDist():
    data_in = request.get_json()
    p1 = data_in["a"]
    p2 = data_in["b"]
    D = ((p2[0]-p1[0])**2+(p2[1]-p1[1])**2)**0.5
    data = {
            "distance": D,
            "a": p1,
            "b": p2
            }
    return jsonify(data)
    