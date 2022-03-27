# AuthLib Standardized Return Codes

Standardized Return Codes are used to make sure that every action in the AuthLib returns replicable, verifiable and comparable statments or objects.

Return codes are created using fragments of various scopes. For Example, return codes of requestHandler methods can be different from that of generators.

## Defining Standardized Return Codes

Standardized return Codes have different scopes -

- `global-scope` Return Codes used by the main AuthLib [ `authLib.py` ] Script in providers directory.
- `script-scope` Return Codes used by the various handlers of AuthLib. Scripts like generators, maintenance, request, etc have separate scopes
- `result-scope` Return Codes corresponding to the result of an action - failed, success, waiting etc.

The complete return code may be defined as - `global-scope` + `script-scope` + `result-scope`

## Codes Used

### Global Scope

For authLib the Global Scoped return statement used is - `0A`

### Script Scope

For The following scopes the return statements used for Handlers are -
| Scripts | Code |
| ------- | ---- |
| authProfileHandler | `P` |
| generators | `G` |
| mainenance | `M`|
| requests | `R` |

### Return Scope

For The following scopes the return statements used for Handlers are -

Request Handler `R`

| Code | Sub Scope | Details |
| ---- | --------- | ------- |
| 01 | register | Invalid Email ID |
| 02 | register | Registered Successfully |
| 03 | register | Registration Request Already Exists. OTP/Mail Resent |
| 11 | verify | Mail Doesn't Exist in AuthLib. Re Register |
| 12 | verify | Request Expired. OTP Regenerated |
| 13 | verify | Incorrect OTP |
| 14 | verify | OTP Verified Successfully |
| 15 | verify | OTP Expired. OTP Regenerated |