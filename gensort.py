from utils.authorization_manager import have_tokens,configure_tokens, read_tokens, generate_user_token, get_client_manager

def retrieve_tokens():
    if not have_tokens():
        return configure_tokens()
    else:
        return read_tokens()
        
def authorization(client_tokens):
    return generate_user_token(client_tokens["username"], client_tokens["client_id"], client_tokens["client_secret"])

def load_gensort():
    client_tokens=retrieve_tokens()
    user_token=authorization(client_tokens)
    return client_tokens, user_token
    
def run_gensort(client_manager, token):
    pass