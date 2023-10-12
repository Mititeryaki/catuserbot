from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 24350557
    API_HASH = "3f302840f638ac2900a3becc056b3c59"
    # the name to display in your alive message
    ALIVE_NAME = "mardas"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://djnfycte:nJILS-RYLxyr9YZ3uF21721pjEY7NkNI@peanut.db.elephantsql.com/djnfycte"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzMBu0G321fQVgb3MoMm01-VMimRFypXDaImaDv48mHqDE6T_IYM7BGaqxnUWB__Aoo2mPMePrMx0yLFwRRziCUQUrNEIvybnOLLEEQkEUP6xIYFo3JUfCpcVfChD8ICverCrmQT0L-6tTMt5ALao6xqxug3WPW_8p19YeU5TldM1Fq_avo4KnfDDaMtkYq1GFd4MT9I0b3Z2EXKW2xxzQUxVdmrWAUse_GuAqWg4Vm7Hs7OnDDq-iYClO8qp2Hywa0TeGbd7gOFB4xdWGDfJkkFH_tc7n6pcyZDi3NCiEthj4kRmBUfVuH-TiJgzQyAGjvIfzC85_elYUbuI1GQrSKnHTM="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6691990790:AAHEu2RGNfYDZDDpYbe2B02VV5xorcDvDKU"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001674045959
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
