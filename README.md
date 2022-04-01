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