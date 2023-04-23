from flask import Flask, jsonify, request
from classifier import  get_prediction

app = Flask(__name__)



  # image = cv2.imdecode(np.fromstring(request.files.get("digit").read(), np.uint8), cv2.IMREAD_UNCHANGED)


if __name__ == "__main__":
  app.run(debug=True)
