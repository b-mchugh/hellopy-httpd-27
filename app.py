from __future__ import absolute_import
import os
import socket
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

hostname = socket.gethostname()
IP = os.environ[u'OPENSHIFT_PYTHON_IP']
port = int(os.environ[u'OPENSHIFT_PYTHON_PORT'])

class RH(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.send_header(u'Content-type',u'text/html')
		self.end_headers()
		message = [u'Client: ' + self.address_string() + u'<br>',
					u'Server: ' + IP + u' aka ' + hostname + u'<br>',
					u'Date: ' + self.date_time_string() + u'<br>']
		for i in message:
			print i
			self.wfile.write(str(i).encode("utf8"))
		return

def run():
	server_address = (IP, port)
	httpd = HTTPServer(server_address, RH)
	httpd.serve_forever()
run()
