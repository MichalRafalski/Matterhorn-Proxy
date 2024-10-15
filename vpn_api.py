from flask import Flask, jsonify, request
import os
import signal
import subprocess
import requests

app = Flask(__name__)

vpn_process = None
using_vpn = False

# Function to get current IP and location info
def get_ip_info():
    try:
        response = requests.get('https://ifconfig.me/all.json')
        data = response.json()
        return {
            'ip': data.get('ip_addr'),
            'country': data.get('country', 'Unknown'),
            'region': data.get('region', 'Unknown'),
            'city': data.get('city', 'Unknown'),
        }
    except Exception as e:
        return {"error": str(e)}

# Start VPN and update HAProxy to prioritize VPN connection
@app.route('/vpn-on', methods=['GET'])
def vpn_on():
    global vpn_process, using_vpn
    ovpn_file = request.args.get('file', default=None, type=str)
    
    if not ovpn_file:
        return jsonify({"message": "No OVPN file specified"}), 400
    
    ovpn_path = os.path.join('/etc/openvpn', ovpn_file)
    
    if not os.path.isfile(ovpn_path):
        return jsonify({"message": "OVPN file not found"}), 404

    if vpn_process is None:
        vpn_process = subprocess.Popen(['openvpn', '--config', ovpn_path])
        using_vpn = True
        return jsonify({"message": "VPN started", "ip_info": get_ip_info()}), 200
    else:
        return jsonify({"message": "VPN is already running"}), 400

# Stop VPN and fallback to the default connection
@app.route('/vpn-off', methods=['GET'])
def vpn_off():
    global vpn_process, using_vpn
    if vpn_process:
        os.kill(vpn_process.pid, signal.SIGTERM)
        vpn_process = None
        using_vpn = False
        return jsonify({"message": "VPN stopped", "ip_info": get_ip_info()}), 200
    else:
        return jsonify({"message": "VPN is not running"}), 400

# Get current IP and location info
@app.route('/ip-info', methods=['GET'])
def ip_info():
    return jsonify(get_ip_info()), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2211)
