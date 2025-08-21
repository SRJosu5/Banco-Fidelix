import threading

def session_service_thread(client_id):
    from src.session.sessio_service import session_service

    session_service_thread_data = threading.Thread(target=session_service, args=(client_id,), daemon=True)
    session_service_thread_data.start()