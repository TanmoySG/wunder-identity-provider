# wunder Identity Provider v0.1

The wunder Identity Provider is the primary IAM - Identity and Access Management platform for all wunder Platform Products. The idea is to unify the identity and access across the board for more coherent and hassle-free single-point service and data access.

The wIP Architecture has several moving parts, but broadly can be consolidated for the end-user into two primary access/interaction points - `registration` and `login`. 

The Architectural and Design details are documented [here](./architecture/README.md).

## Identity

The Identity of a User is uniquely defined (primarily) by the user's email ID, while the uID (system generated) and username (user defined) are used for secondary and tertiary identification. The (rough) ID Structure, that is stored and used can be found [here](./architecture/README.md#identity-specification). 

## Usage 

Sample New User Data
```
Name: Tanmoy
Mail: tanmoysps@gmail.com
Password: 123456
```
Running the End-to-End Registration & Verification Flow
```
make run-demo
```
Running the above should output    
```
Resources Torn Down

Running Demo...
[ DEV - Logging at logs ]
(DEV) [30/03/2022 03:46:03] INFO : {'return_code': 'ALR02', 'scope': 'authlib.requests.register', 'details': 'Request Registered Successfully. OTP Generated.', 'response': 'success'}
(DEV) [30/03/2022 03:46:07] INFO : {'return_code': 'MLS01', 'scope': 'mailer.send.mail', 'details': 'Mail Sent!', 'response': 'success'}
(DEV) [30/03/2022 03:46:07] INFO : {'return_code': 'ALR14', 'scope': 'authlib.requests.verify', 'details': 'Correct OTP. Authentication Successful.', 'response': 'success'}
(DEV) [30/03/2022 03:46:09] INFO : {'return_code': 'RPR01', 'scope': 'registration.register.verified', 'details': 'Profile Created. Welcome Mail Sent.', 'response': 'success'}
(DEV) [30/03/2022 03:46:12] INFO : {'return_code': 'MLS01', 'scope': 'mailer.send.mail', 'details': 'Mail Sent!', 'response': 'success'}
(DEV) [30/03/2022 03:46:12] SUCCESS : Process Complete
```
Teardown created resources while running the demo
```
make teardown
```