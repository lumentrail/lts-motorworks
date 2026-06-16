import http.server, os
os.chdir(r'C:\Users\Mike\Documents\LTS Motorworks\Website')
http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler, port=8787, bind='127.0.0.1')
