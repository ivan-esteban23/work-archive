from http.server import ThreadingHTTPServer,SimpleHTTPRequestHandler
from functools import partial
class HostingRedirect(SimpleHTTPRequestHandler):
 def do_GET(self):
  if self.path.split('?')[0]=='/index.html':
   self.send_response(301);self.send_header('Location','/');self.end_headers()
  else:super().do_GET()
ThreadingHTTPServer(('127.0.0.1',8768),partial(HostingRedirect,directory='/home/ivanaguilera/Work/visual-edit-pwa-20261013/staged/dist')).serve_forever()
