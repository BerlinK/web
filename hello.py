def wsgi_app( environ, start_response ) :
    headers = [( 'Content-Type', 'text/plain')]
    status = '200 OK'
    body = ''
    qstrs = environ['QUERY_STRING'].split( '&' )

    for i in qstrs :
        body += i + "\n"    
    start_response( status, headers )
    return [body]
