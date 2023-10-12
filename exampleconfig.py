from sample_config import Config


class Development(Config):
    # get this values from the my.telegram.org
    APP_ID = 21066338
    API_HASH = "e859e806021f315abfaf7a20fb3d587d"
    # the name to display in your alive message
    ALIVE_NAME = "mardas"
    # create any PostgreSQL database (i recommend to use elephantsql) and paste that link here
    DB_URI = "postgres://djnfycte:nJILS-RYLxyr9YZ3uF21721pjEY7NkNI@peanut.db.elephantsql.com/djnfycte"
    # After cloning the repo and installing requirements do python3 stringsetup.py an fill that value with this
    STRING_SESSION = "1AZWarzMBu6vn9os3AdI2aLfIu954aAEKMCFmiiEO62LqsV0y7FItoyv8xm6lrfvlGWNAOjKVrJRuitwgWMTwowU8PGBtixbWwJAAQl2mkaJ0h_4DOPHn4XjAckxMj3VbYKSeDuMslxXYWNcJax4HpI2B1eBx8C36UC8MByG9Pb3h2d_J7vK0u8QoWF5HfkC0EfIVSaBnFGl-JE44neidWl2xeTHzzhJTiqB_FZcO86nV3tUGTFzVKkfWpxUL-OTdWbBeMyl7orvLC8Pc7gwbWuhlnXQU-gmug3cyr_BETeYYZ6yK03GZQJuKeu9enN52094ChGGnen_9Eu0C0ZrMJ3hArQo0tnw="
    # create a new bot in @botfather and fill the following vales with bottoken
    TG_BOT_TOKEN = "6326938318:AAHkWq2RmQgSrJPTP-zANIuAM0wpVuG18E0"
    # create a private group and a rose bot to it and type /id and paste that id here (replace that -100 with that group id)
    PRIVATE_GROUP_BOT_API_ID = -1001946273476
    # command handler
    COMMAND_HAND_LER = "."
    # command hanler for sudo
    SUDO_COMMAND_HAND_LER = "."
    # External plugins repo
    EXTERNAL_REPO = "https://github.com/TgCatUB/CatPlugins"
    # if you need badcat plugins set "True"
    BADCAT = "True"
