import configparser

def config(first,sencond):
    Config = configparser.ConfigParser()

    Config.read("config.ini")
    data=Config.sections()

    db_host=Config.get(first,sencond)
    return db_host
