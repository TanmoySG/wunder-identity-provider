# wunder Identity Provider v0.1

[![Containerize and Publish on Tagging](https://github.com/TanmoySG/wunder-identity-provider/actions/workflows/containerize-and-publish.yml/badge.svg)](https://github.com/TanmoySG/wunder-identity-provider/actions/workflows/containerize-and-publish.yml) [![Release on Tagging](https://github.com/TanmoySG/wunder-identity-provider/actions/workflows/release-on-github.yml/badge.svg)](https://github.com/TanmoySG/wunder-identity-provider/actions/workflows/release-on-github.yml) 

The wunder Identity Provider is the primary IAM - Identity and Access Management platform for all wunder Platform Products. The idea is to unify the identity and access across the board for more coherent and hassle-free single-point service and data access.

The wIP Architecture has several moving parts, but broadly can be consolidated for the end-user into two primary access/interaction points - `registration` and `login`. 

The Architectural and Design details are documented [here](./architecture/README.md).

<!--
## Identity

The Identity of a User is uniquely defined (primarily) by the user's email ID, while the uID (system generated) and username (user defined) are used for secondary and tertiary identification. The (rough) ID Structure, that is stored and used can be found [here](./architecture/README.md#identity-specification). 
-->

## Usage

### Running wIP Locally

Setup the Project
```
make setup
```
This will set-up the project for you - installing python dependancies and also will setup the Mailer Configurations with credentials.


Start the flask server.
```
flask run
```

### Running the wIP Container with Docker

For Ease of Usage, a Docker Container is published on GitHub Package Registry. Since the whole app is Containerized, it can run without Flask or other depedancies installed on the Host Machine, it only requires Docker installed locally.

Pull the Container
```
docker pull ghcr.io/tanmoysg/wunder-identity-provider:latest
```
The server configs need to be mounted onto the Container for the Mailer to work. To do so run the `setup.sh` script by passing the required parameters.
```
./setup.sh [SMTP PORT] [SMTP SERVER ADDRESS] [MAIL PASSWORD] [MAIL ADDRESS]
```
This Generates the `server-config.json` file in the present working directory.


Run the container using `docker run` command by mounting the server-configs and exposing the ports for local usage.
```
docker run -p 5000:5000 -v ${PWD}/server-config.json:/app/configs/server-config.json ghcr.io/tanmoysg/wunder-identity-provider:latest
```
Alernatively, (and popularly) `docker-compose` is used to run containers in a easy way. In this repo, you'll find a `docker-compose.yml` file that contains all cofigurations to run the docker container, without the hassle of doing all the mappings from the commandline. To use docker compose, go to the directory with the `docker-compose.yml` file and run
```
docker-compose up
```
This will run the docker container locally and should be ready to use!

Please Note, that the Docker container once torndown, the data inside it (created while running it) also gets deleted as no persistent volume is bound to it. To make the data persistent, you can additionally mount a [persistent docker volume](https://www.google.com/search?q=persistent+docker+volume&oq=persistent+docker+&aqs=chrome.0.0i20i263i512j0i512j69i57j0i512j0i22i30l6.3001j1j9&sourceid=chrome&ie=UTF-8) while running the container.

## API Endpoints

Once the container (or the flask app) is up and running locally, the following API Endpoints can be used to interact with `wunder Identity Provider`

- `/register/generate/` 
- `/register/verify/`
- `/login/`

### Registration - Generate OTP

Use the following Endpoint, Payload and Header to Generate OTP.

```
ENDPOINT: {url}/register/generate
METHOD:   POST
PAYLOAD:  {
            "email": {email},
            "name" : {name},
            "password: {password}
          }
```
Run a demo registration using `cURL` by replacing the values of email, password and name.

```
curl --request POST \
  --url http://{url}/register/generate \
  --header 'content-type: application/json' \
  --data '{
  "email": "jane@doe.com",
  "name": "Jane Doe",
  "password": "123456"
}'
```

### Registration - Verify OTP

Use the following Endpoint, Payload and Header for Verification.

```
ENDPOINT: {url}/register/verify
METHOD:   POST
PAYLOAD:  {
            "email": {email},
            "otp" :  {OTP}
          }
```
Run a demo verification using `cURL` by replacing the values of email, OTP recieved in your mail, within 90 seconds.
```
curl --request POST \
  --url http://{url}/register/verify \
  --header 'content-type: application/json' \
  --data '{
  "email": "jane@doe.com",
  "otp" : "oOTtPp"
}'
```

### Login

Use the following Endpoint, Payload and Header to Log-in.

```
ENDPOINT: {url}/login
METHOD:   POST
PAYLOAD:  {
            "email": {email},
            "password: {password}
          }
```

Run the demo using `cURL` by replacing the values of email, password.
```
curl --request POST \
  --url http://{url}/login \
  --header 'content-type: application/json' \
  --data '{
  "email": "jane@doe.com",
  "password" : "123456"
}'
```
