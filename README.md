# CoCo Cognigy Connector

CoCo Cognigy connector is a [Flask](http://flask.palletsprojects.com/en/1.1.x/ "Flask") application which allows you to expose your [Cognigy](htps://www.cognigy.com/ "Cognigy") bots as a components at the [CoCo marketplace](https://marketplace.conversationalcomponents.com/ "CoCo marketplace").

### Deployment Flow:

1. Deploy Cognigy Bot(Do not forget to enable the API).
2. Place the bot API URL in a JSON format at the following directory at the CoCo Cognigy Connector source:
`/CognigyManager/components` - Each file represent a component which can be accessed through an http call to` https://<host>/api/exchange/<file name - no extension>/<session ID>`
3. Upload the Flask app to a cloud service(Google app engine is recommende - yaml file included.)
