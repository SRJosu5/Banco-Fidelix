from socket import gethostbyname, create_connection, error

def is_connected():
    try:
        gethostbyname("google.com")
        connection = create_connection(("google.com", 80), 1)
        connection.close()
        return True
    except error:
        return False