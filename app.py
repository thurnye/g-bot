from flask import Flask, request, jsonify

app = Flask(__name__)

# Route to return student number
@app.route('/')
def home():
    return jsonify({"student_number": "200629468"})  # Replace with your actual student number.

# Webhook route for Dialogflow
@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)  # Get request from Dialogflow

    # Process the intent
    intent = req.get("queryResult", {}).get("intent", {}).get("displayName")

    # Generate a response
    if intent == "Weather Checker":
        response_text = "Hope it gets much better to your liking, where ever you are"
    else:
        response_text = "Fallback response"

    # Return the response in JSON format
    return jsonify({
        "fulfillmentText": response_text
    })

if __name__ == '__main__':
    app.run(debug=True)
