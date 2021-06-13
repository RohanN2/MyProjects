from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/hi')
def get_location_names():
    response = jsonify(
        {
            'location': util.get_location_name()
        }
    )
    response.header.add('Access-Control-Allow-Origin','*')


if  __name__ == '__main__':
    print('Starting python flask server for home prediction module')
    app.run()