import http.server

def start_server(port=7000, bind="", cgi=True):
    if cgi==True:
        http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler, port=port)
    else:
        http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,port=port)

start_server() #If you want cgi, set cgi to True e.g. start_server(cgi=True)
