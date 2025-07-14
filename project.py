# import necessary modules

# for implementing the HTTP Web servers
import http.server

# provides access to the BSD socket interface
import socket

# a framework for network servers
import socketserver

# to display a Web-based documents to users
import webbrowser

# to generate qrcode
import pyqrcode
from pyqrcode import QRCode

# convert into png format
import png

# to access operating system control
import os

# for ngrok tunneling
from pyngrok import ngrok

# assigning the appropriate port value
PORT = 8010

# this finds the name of the computer user
os.environ['USERPROFILE']

# changing the directory to access the files desktop
# with the help of os module
desktop = os.path.join(os.path.join(os.environ['USERPROFILE']),
                       'OneDrive')
os.chdir(desktop)

# creating an HTTP request handler
Handler = http.server.SimpleHTTPRequestHandler

# Set up a local server
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("serving at port", PORT)
    
    # Start an ngrok tunnel to the server
    public_url = ngrok.connect(PORT)
    print("ngrok tunnel available at:", public_url)

    # Generate the QR code for the ngrok URL
    url = pyqrcode.create(public_url)
    # saves the QR code as an SVG file
    url.svg("myqr.svg", scale=8)
    # opens the QR code image in the web browser
    webbrowser.open('myqr.svg')
    
    print("Type this in your Browser", public_url)
    print("or Use the QRCode")

    # Start serving the HTTP server
    httpd.serve_forever()

