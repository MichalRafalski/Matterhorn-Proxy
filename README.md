# Matterhorn Proxy

**Matterhorn Proxy** sets up a VPN proxy server using Docker, OpenVPN, TinyProxy, and Flask. It allows users to temporarily connect to a VPN to access region-restricted content while providing an API to manage connections and retrieve IP information. Users can easily toggle the VPN on and off without changing client-side proxy settings, enabling full internet speeds when needed.

**Tested on Raspberry Pi 4.**

![Matterhorn](logo.webp)

## Features

- Connect to a VPN using OpenVPN.
- Manage connections with TinyProxy.
- RESTful API for controlling the VPN and retrieving IP information.
- Temporary VPN access for VOD services.
- Easy toggling of the VPN connection, allowing for full internet speeds when the VPN is off.
- Lightweight and efficient, designed for Raspberry Pi 4.

## Requirements

- Docker and Docker Compose.
- Raspberry Pi 4 (recommended).
- Make sure that your OVPN file has this line: `route 192.168.1.0 255.255.255.0 net_gateway`

## Setup Instructions

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MichalRafalski/Matterhorn-Proxy.git
   cd Matterhorn-Proxy
   ```

2. **Prepare OpenVPN Configuration:**

   Place your OpenVPN configuration file (`config.ovpn`) in the project directory.

3. **Build and Start the Container:**

   ```bash
   docker-compose up --build
   ```

## API Endpoints

- **Start VPN**: `curl -X POST http://localhost:2211/vpn-on`
- **Stop VPN**:  `curl -X POST http://localhost:2211/vpn-off`
- **Get IP Info**: `curl http://localhost:2211/ip-info`
- **Test proxy**: `curl -x http://192.168.1.15:8888 https://ifconfig.me/all.json`

Each endpoint returns a JSON response with relevant information.


## Why "Matterhorn"?
![Matterhorn](https://www.zermatt.ch/extension/portal-zermatt/var/storage/images/media/bibliothek/neuigkeiten-fotos/matterhorn-alpine-crossing-ab-dem-1.-juli-2023-wird-die-grenze-ueberschritten/3253359-1-ger-DE/Matterhorn-Alpine-Crossing-ab-dem-1.-Juli-2023-wird-die-Grenze-ueberschritten_front_magnific.jpg)

The name **Matterhorn Proxy** is inspired by the iconic Swiss mountain, known for its distinct pyramid shape and its status as a border between Switzerland and Italy. Just as the Matterhorn serves as a landmark for travelers navigating the surrounding region, Matterhorn Proxy serves as a gateway to access global content securely. The project aims to provide users with the freedom to bypass geographical restrictions while ensuring their privacy and security online.


## Author
Michal Rafalski

## License

This project is licensed under the MIT License.

