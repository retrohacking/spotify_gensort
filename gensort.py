from utils.authorization_manager import have_tokens,configure_tokens, read_tokens, generate_user_token

def check_tokens():
    if not have_tokens():
        configure_tokens()

def authorization():
    username, client_id, client_secret = read_tokens()
    return generate_user_token(username, client_id, client_secret)
