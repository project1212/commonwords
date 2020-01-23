#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cherrypy
import re

class webService():
    @cherrypy.expose
    @cherrypy.tools.json_out()
    @cherrypy.tools.json_in()
    
    #parse input1 and input2 from json file, removeSpecialChar key will be used to include/not include special chars.
    def process(self, **kwargs):
        
        data = cherrypy.request.json
        input1 = data["input1"]
        input2 = data["input2"]
        removeSpecialChar = data['removeSpecialChar']
        
        if removeSpecialChar == 'true':
            input1ToList = re.sub("[^\w]", " ", input1).split()
            input2ToList = re.sub("[^\w]", " ", input2).split()
        else:
            input1ToList = input1.split()
            input2ToList = input2.split()
            
        similarList = [1 if word in set(input2ToList) else 0 for word in input1ToList]
        
        return sum(similarList)
    
        
def startServer():
    cherrypy.tree.mount(webService(), '/')
    cherrypy.config.update({'server.socket_port': 8080})
    cherrypy.engine.start()

if __name__ == '__main__':
    startServer()
