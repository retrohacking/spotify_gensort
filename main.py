from gensort import load_gensort, run_gensort

def main():
    client_manager, token=load_gensort()
    run_gensort(client_manager, token)

if __name__=="__main__":
    main()
