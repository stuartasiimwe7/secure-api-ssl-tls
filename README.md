# Secure API with SSL/TLS

This project demonstrates how to set up a secure API using Flask and SSL/TLS encryption. By encrypting data transmission, we ensure secure communication between clients and servers. This is a fundamental skill in system security and is widely applicable to embedded systems, IoT devices, and web applications.

## Features
- An API built with Flask that responds with a message.
- SSL/TLS encryption enabled for secure communication.
- Self-signed SSL certificates for local testing.

---

## Technologies Used
- **Python**: For building the API using Flask.
- **Flask**: A lightweight web framework for building the API.
- **OpenSSL**: For generating SSL/TLS certificates.
- **Git**: For version control and project hosting.

---

## How to Run the Project

### 1. Clone the Repository
Start by cloning this repository to your local machine:
```bash
git clone https://github.com/yourusername/secure-api-ssl-tls.git
cd secure-api-ssl-tls
```

### 2. Set Up the Development Environment
Create and activate a virtual environment using `venv`:

```bash
python -m venv venv
```
#### On Windows
```bash
venv\Scripts\activate
```

#### On macOS/Linux
```bash
# On macOS/Linux
source venv/bin/activate
```
Install Flask using pip:

```bash
pip install flask
```

### 3. Generate SSL/TLS Certificates
Generate self-signed SSL certificates using OpenSSL. Open your terminal and run the following commands:

```bash
openssl genpkey -algorithm RSA -out server.key
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

This will create:
- `server.key`: Your private key.
- `server.crt`: Your certificate.

These files will be used by the Flask application to enable HTTPS.

### 4. Run the Flask App
Run the app using the following command:

```bash
python app.py
```
