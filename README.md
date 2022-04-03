# wunder Identity Provider v0.1

The wunder Identity Provider is the primary IAM - Identity and Access Management platform for all wunder Platform Products. The idea is to unify the identity and access across the board for more coherent and hassle-free single-point service and data access.

The wIP Architecture has several moving parts, but broadly can be consolidated for the end-user into two primary access/interaction points - `registration` and `login`. 

The Architectural and Design details are documented [here](./architecture/README.md).

## Identity

The Identity of a User is uniquely defined (primarily) by the user's email ID, while the uID (system generated) and username (user defined) are used for secondary and tertiary identification. The (rough) ID Structure, that is stored and used can be found [here](./architecture/README.md#identity-specification). 

## Usage 

Setup the Project
```
make build
```
This will set-up the project for you - installing python dependancies and also will setup the Mailer Configurations with credentials.

## Running Flask-App Demo

Start the flask server.
```
flask run
```

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
Run the demo using `cURL` by replacing the values of email, password and name.

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
PAYLOAD: {
          "email": {email},
          "otp" :  {OTP}
         }
```
Run the demo using `cURL` by replacing the values of email, OTP recieved in your mail, within 90 seconds.
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

## Manual Demos
You can Run Manual demos without running the flask server

### Run Demos with default Demo User Data

Default Sample User Data
```
Name: Tanmoy
Mail: tanmoysps@gmail.com
Password: 123456
```

Running the End-to-End Registration & Login Flows
```
make run-demo
```

Registration and Login Demos can also be run idividually.
```
// To run Registration Demo
make run-registration-demo

// To run Login Demo
make run-login-demo
```


### Run Demos with Custom User Data

You can run the demos with custom User Data. To do so, edit the `demo/demo_user.json`.

```
vi demo/demo_user.json
```
Replace the Default Mail, Name and Password with the ones you want to test
```
{
    "email": "Enter Mail Here",
    "name": "Name of User",
    "password": "Password"
}
```

Run the End-to-End Registration & Login Flows with custom user data.
```
make load-user-and-run-demo
```

Run the Registration Demo Individually with custom user data
```
make load-user-and-run-registration
```

Run the Login Demo Individually with custom user data
```
make load-user-and-run-login
```

### Teardown Resources

To Teardown resources created while running Demos, run
```
make teardown
```