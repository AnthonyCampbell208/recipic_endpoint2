from flask import Flask, jsonify, request


# load model
# model = pickle.load(open('model.pkl','rb'))

# app
app = Flask(__name__)

# routes
@app.route('/', methods=['POST'])
def predict():
    # get data
    data = request.get_json(force=True)
    return jsonify(data)

if __name__ == '__main__':
    app.run()

