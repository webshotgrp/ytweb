#!/usr/bin/env python

#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import BaseHTTPServer
import SimpleHTTPServer
import os
import json
import time


currDir = os.path.dirname(os.path.abspath(__file__)) + '/'

class TestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    
#handle GET command
    def do_GET(self):
        
        try:
	        #reqFile = currDir + 'stlLoader/' + self.path
	        #reqFile = currDir + 'stlLoader' + self.path
		reqFile = currDir + self.path
		if self.path.endswith('/'):
                    reqFile = currDir + 'index.html'
                print reqFile
                f = open(reqFile, 'rb') #open requested file

                #send code 200 response
                self.send_response(200)
                if self.path.endswith('.stl'):
                    self.send_header('Content-type','text/stl')
                elif self.path.endswith('.pdf'):
                    self.send_header('Content-type','text/pdf')
                elif self.path.endswith('.html'):
                    self.send_header('Content-type','text/html')
                elif self.path.endswith('.js'):
                    self.send_header('Content-type','text/javascript')
                elif self.path.endswith('.png'):
                    self.send_header('Content-type','image/png')
                elif self.path.endswith('.jpg'):
                    self.send_header('Content-type','image/jpg')
                self.end_headers()

                #send file content to client
                self.wfile.write(f.read())
                f.close()
               # if self.path.endswith('.stl'):
               #     os.remove(reqFile)
               # return
            
        except IOError:
        	self.send_error(404, 'file not found')


    #handle POST command
    def do_POST(self):
        print('nothing to do')

        #self.data_string = self.rfile.read(int(self.headers['Content-Length']))
        # print("DATA string ->")
        # result = '/model/pocket.stl' 
        # self.send_response(200)
        # self.send_header("Content-type","text/plain")
        # self.send_header("Content-Length", len(result))
        # self.end_headers()
        # self.wfile.write(result)   
        # return

        # timestamp = str(time.time())
        # print(self.data_string)
        # #print(currDir)
        # #data = json.loads(self.data_string)
        # try:
        #     #deg = data['degree']
        #     #print (deg)
        #     directory = currDir + 'userData/' + timestamp
        #     readJSON.readJSN(self.data_string, directory)
        #     readJSON.runProgram(directory)

        #     result = 'userData/' + timestamp 
        #     self.send_response(200)
        #     self.send_header("Content-type","text/plain")
        #     self.send_header("Content-Length", len(result))
        #     self.end_headers()
        #     self.wfile.write(result)   
        #     return
            
        # except IOError:
        #     self.send_error(404, 'file not found')
    
def run():
    print('http server is starting 8114...')

    try:
        server_address = ('', 8114)
        httpd = BaseHTTPServer.HTTPServer(server_address, TestHandler)
        print 'started...'
        httpd.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        httpd.socket.close()
    
if __name__ == '__main__':
    run()
