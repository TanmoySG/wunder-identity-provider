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
| `0AR01` | register `0` | Invalid Email ID `1` |
| `0AR02` | register `0` | Registered Successfully `2`|
| `0AR03` | register `0` | Registration Request Already Exists. OTP/Mail Resent `3` |
| `0AR11` | verify `1` | Mail Doesn't Exist in AuthLib. Re Register `1` |
| `0AR12` | verify `1`  | Request Expired. OTP Regenerated `2` |
| `0AR13` | verify `1`  | Incorrect OTP `3` |
| `0AR14` | verify  `1` | OTP Verified Successfully `4`|
| `0AR15` | verify  `1` | OTP Expired. OTP Regenerated `5` |