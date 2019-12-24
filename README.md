# CoCo Cognigy Connector

CoCo Cognigy connector is a [Flask](http://flask.palletsprojects.com/en/1.1.x/ "Flask") application which allows you to expose your [Cognigy](https://www.cognigy.com/ "Cognigy") bots as a components at the [CoCo marketplace](https://marketplace.conversationalcomponents.com/ "CoCo marketplace").

### Deployment Flow:
1. Deploy Cognigy Bot(Do not forget to enable the API).
2. Create Rest endpoint for your bot.
 ![Create Rest endpoint.](/Screenshots/1CreateRestEndpoint.png)
2. Map component statuses and context action names in your bot responses.
	- **Done Status** - Status which will be returned when the bot/`component` achived it's goal(Add "<done>" tag to the message text).
	- **Failed Status** - Status which will be returned when the bot/`component` will not complete it's goad(Add "<failed>" tag to the message text).
	- **Out Of Status** - Status which will be returned when the conversation went out of context(Add "<out_of_context>" tag to the message text).
	- **Action Name** -  The current context action name.  (Add "<action:action_name>" tag to the message text).
 ![Map statuses and actions.](/Screenshots/2MapActionsAndStatuses.png)
3. Place the bot API URL in a JSON format at the following directory at the CoCo Cognigy Connector source:
`/CognigyManager/components` - Each file represent a component which can be accessed through an http call to` https://<host>/api/exchange/<file name - no extension>/<session ID>`
4. Upload the Flask app to a cloud service(Google app engine is recommende - yaml file included.)

 ```gcloud app deploy```