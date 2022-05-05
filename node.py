from flask import Flask , jsonify , request, send_from_directory
from flask_cors import CORS

app = Flask(__name__)

CORS(app) #with this the app gets open to other clients

@app.route('/',methods = ['GET']) #configuring the endpoint (path and method)
def get_node_ui():
    return send_from_directory('ui','node.html')

@app.route('/wallet', methods = ['POST'])
def create_keys():
    if True:
        response = {
            'mensaje': 'te re cabe gil',
            'public_key': 'soy publica',
            'private_key': 'soy privada',
        }
        return jsonify(response),201
    else:
        response = {
            'message': 'Saving the keys failed'
        }
        return jsonify(response), 500



@app.route('/wallet', methods=['GET'])
def load_keys():
    if True:
        response = {
            'public_key': 'Ya no tenes mas llave publica',
            'private_key': 'Y menos que menos una privada',
        }
        return jsonify(response),201
    else:
        response = {
            'message': 'Loading the keys failed'
        }
        return jsonify(response),500

if __name__ == '__main__':
    from argparse import ArgumentParser
    parser = ArgumentParser() #execute its constructor.
    parser.add_argument('-p','--port',type = int, default = 5005)
    args = parser.parse_args() #extract data of my parse
    port = args.port #extract the port
    app.run(host='0.0.0.0', port = port) #can use arbitrary port

# localhost:5000/ put this on web browser and have the response.