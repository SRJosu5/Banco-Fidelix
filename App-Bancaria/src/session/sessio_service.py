import time

def session_service(client_id):
    from src.database.crud.read.client_bank_account_read import get_client_bank_account
    from src.database.crud.read.client_envelopes_read import get_client_envelopes
    from src.database.crud.read.client_card_data_read import get_client_card_data
    from src.database.crud.read.client_data_read import get_client_data
    from src.session import session_data

    while True:
        session_data.client_data = get_client_data(client_id)
        session_data.client_bank_account_data = get_client_bank_account(client_id)
        session_data.client_card_data = get_client_card_data(client_id)
        session_data.client_envelopes = get_client_envelopes(client_id)
        #print("Info cargada")
        #print(session_data.client_data, session_data.client_bank_account_data, session_data.client_card_data, session_data.client_envelopes)
        time.sleep(1)