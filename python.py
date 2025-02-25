from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/nickname/ml', methods=['GET'])
def get_nickname():
    # Get parameters from the URL
    server_id = request.args.get('id')
    zone_id = request.args.get('zone')

    if not server_id or not zone_id:
        return jsonify({"error": "Missing parameters. Please provide 'id' and 'zone'."}), 400

    # Construct the API URL
    api_url = f"https://api.isan.eu.org/nickname/ml?id={server_id}&zone={zone_id}"

    # Make the API request
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):
            nickname = data.get("name", "Unknown")
            result = {
                "Developed by": "Shensi",
                "MLBB_S2": "Mobile Legends: Bang Bang",
                "NicknamePlayer": nickname,
                "Region": "unfind",
                "ZoneID": data.get('server'),
                "ServerID": data.get('id'),
                "Telegram Work": "Shensi_sn"
            }
            return jsonify(result)
        else:
            return jsonify({"error": "Failed to retrieve nickname. Please check the Server ID and Zone ID."}), 404
    else:
        return jsonify({"error": "Error fetching data from the API. Please try again later."}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Run the app on port 5000