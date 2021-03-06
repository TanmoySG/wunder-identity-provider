# Notes and Observations

_This is to be used only to document Ideas and interim rough thoughts. Information here is to be structured, moved and documented in README going Forward._

## The Curious case of Login and the various Tokens

**Problem** - Should I use Primary User Access token as global access token for all WPlat Services ? Or should I opt for a User Access Token - Service Admin Access Token - App Access token Model?

**Two Models - What Exactly? Why and How?**

1. Primary Global Access Tokens -

    In existing wDB system, when a user creates an Account, Tokens are assigned directly for the account which is then used for accessing both wDB Official Dashboard as well as any end-user created application. This approach is easy to implement but gives away the logical access separation between admin(wDB user) and admin-created app user, making access global for everyone and every action. For reference see [wDB repo](https://github.com/TanmoySG/wunderDB).

2. User Access - wPlat Authorized Application Access - User Authorized App Access -

    A multi Token based approach, which creates Logical Divides between an user-admin and other access points and also introduces separate access for authorized applications built by wPlat, and for Admin Authorized Applications - maybe built by the admin.

## Identifying the different Access Points , Mediums and Types

There can be multiple points of access - Admin (who owns the account), A Team Member (to the admin), or the end-user of the data stored in the wPlat Service (like an user of a todo app created by the Admin's Company that uses wDB as a storage medium and must only have read and write access and not admin access) .

There can also be multiple mediums of platforms of access - Access from the wunder Dashboard for wDB (an official wPlat Offering that might need some special access that a non-wPlat Service should not have) or Access from the ToDo app Admin created( that app doesn't require all features of wDB like wDash does, so different access)

What Else ? [ Add new above ^ ]

![](https://github.com/TanmoySG/wunder-identity-provider/blob/dev/architecture/diagrams/Access-Types-Logic.jpg)


# Data Files - Notes

- `authLibProfiles_dev` - for Dev and Test. To be moved to production db `authLibProfiles`
    - uid
    - email - primary identifier
    - timestamp
    - latestHashedOTP - find a string concat and hash
    - status
    - (maybe) payload
    - anything else (To be added while dev and test)

- `authLibProfiles` - for Production
    - uid
    - email - primary identifier
    - timestamp
    - latestHashedOTP - find a string concat and hash
    - status
    - (maybe) payload
    - anything else (To be added while dev and test)


# OTP Architecture

[ OTP Verification Subsystem ]

![OTP-Subsystem](./diagrams/OTP-SubSystem.jpg)

[ Notes ]

- Shall use Time-based OTP Algorithm, w/o Google-auth.
- Enable Magic-link based authentication (integrated with OTP SubSys)
- Shall send OTP to Mail 
- Alpha Numeric OTP - 6 Digit, prep.
- _TBD_

# Versioning 


A proper versioning system that should be used in this project is

```
Major.Minor.Patch-target
```

In the Above 

- **Major** - Major Feature Additions, Breaking API Changes and other Major Changes that can effect the dependant systems.
- **Minor** - Minor Feature Additions, Backward Compatible, Usage Experience Enhancements and Minor Changes.
- **Patch** - Bug Fixes, Backward Compatible and Enhancement Fixes and Changes.
- **target** - Build Targets (OS Specific/OS Version Specific/Architecture Specific Targets) or pre-releases (beta/alpha) or audience/user Targets (general/Pro/internal/etc.)

[Refer to semver.org](https://semver.org/)


# Release and Deployment Strategy

Refer Issue [#79](https://github.com/TanmoySG/wunder-identity-provider/issues/79)

# Future

- Goal is to replace `authlib`in the future and enable profiles-level verification and remove intermediate step [Plan TBD]