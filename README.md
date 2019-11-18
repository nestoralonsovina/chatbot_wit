# chatbot_wit
Small and simple bot made to learn the basics about them

Built using python and flask (web server) is connecting to a model created in wit.ai, which is able to identify
the differents intents and values as: 

Example:

Which is the **temperature** in **Paris**? That will return the intent "get_temperature" in the Location "Paris".

Similar behaviour for the hour.

If wit.ai doesn't find an intention, the bot will connect to cleverbot.ai and ask for "human" response, so you can
have a normal conversation with it.
