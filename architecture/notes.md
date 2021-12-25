# Notes and Observations

_To be moved structured and documented in README going Forward_

## Curios case of Login and the various Tokens

**Problem** - Should I use Primary User Access token as global access token for all WPlat Services ? Or should I opt for a User Access Token - Service Admin Access Token - App Access token Model?

**Two Models - What Exactly? Why and How?**

1. Primary Global Access Tokens -

    In existing wDB system, when a user creates an Account, Tokens are assigned directly for the account which is then used for accessing both wDB Official Dashboard as well as any end-user created application. This approach is easy to implement but gives away the logical access separation between admin(wDB user) and admin-created app user, making access global for everyone and every action. For reference see [wDB repo](https://github.com/TanmoySG/wunderDB).

2. User Access - wPlat Authorized Application Access - User Authorized App Access -

    A multi Token based approach, which creates Logical Divides between an user-admin and other access points and also introduces separate access for authorized applications built by wPlat, and for Admin Authorized Applications - maybe built by the admin.