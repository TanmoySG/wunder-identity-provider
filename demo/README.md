
## Manual Demos
You can Run Manual demos without running the flask server

Move the `demo.py` to the parent directory
```
mv demo.py ../
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
Run demos by loading custom user data.
```
// Run End-to-End Registration & Login Flows with custom user data.
make load-user-and-run-demo

// Run the Registration Demo with custom user data
make load-user-and-run-registration

// Run the Login Demo with custom user data
make load-user-and-run-login
```

### Teardown Resources

To Teardown resources created while running Demos, run
```
make teardown
```
