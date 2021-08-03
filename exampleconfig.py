from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 1964231
    API_HASH = "ec4c7aef178d0f34501bde03c9926da2"
    # the name to display in your alive message
    ALIVE_NAME = "SWALIH KP"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "Your value"
    # After cloning the repo and installing requirements do python3 telesetup.py an fill that value with this
    STRING_SESSION = "Your value"
    # create a new bot in @botfather and fill the following vales with bottoken and username respectively
    TG_BOT_TOKEN = "1949612539:AAEH5QGcXu-z1Ja_U5bMFtAQ9PvzKn21mHI"
    TG_BOT_USERNAME = "Swalihpookkotturbot"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -100
    # command handler
    COMMAND_HAND_LER = "."
    # sudo enter the id of sudo users userid's in that array
    SUDO_USERS = []
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
