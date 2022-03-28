# AuthLib Standardized Return Codes

Standardized Return Codes are used to make sure that every action in the AuthLib returns replicable, verifiable and comparable statments or objects.

Return codes are created using fragments of various scopes. For Example, return codes of requestHandler methods can be different from that of generators.


| Code | Details |
| ---- | ------- |
| `ALR01`  | Invalid Email ID |
| `ALR02`  | Registered Successfully |
| `ALR03` | Registration Request Already Exists. OTP/Mail Resent |
| `ALR11`  | Mail Doesn't Exist in AuthLib. Re Register |
| `ALR12`  | Request Expired. OTP Regenerated  |
| `ALR13` | Incorrect OTP |
| `ALR14` | OTP Verified Successfully|
| `ALR15`  | OTP Expired. OTP Regenerated |

## Defining Standardized Return Codes

Standardized return Codes have different scopes -

- `global-scope` Return Codes used by the main AuthLib [ `authLib.py` ] Script in providers directory.
- `script-scope` Return Codes used by the various handlers of AuthLib. Scripts like generators, maintenance, request, etc have separate scopes
- `result-scope` Return Codes corresponding to the result of an action - failed, success, waiting etc.

The complete return code may be defined as - `global-scope` + `script-scope` + `result-scope`

## Codes Used

### Global Scope

For authLib the Global Scoped return statement used is - `AL`

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

Sub-Scopes - register `0` and verify `1`

| Code | Sub Scope | Details |
| ---- | --------- | ------- |
| `ALR01` | register `0` | Invalid Email ID `1` |
| `ALR02` | register `0` | Registered Successfully `2`|
| `ALR03` | register `0` | Registration Request Already Exists. OTP/Mail Resent `3` |
| `ALR11` | verify `1` | Mail Doesn't Exist in AuthLib. Re Register `1` |
| `ALR12` | verify `1`  | Request Expired. OTP Regenerated `2` |
| `ALR13` | verify `1`  | Incorrect OTP `3` |
| `ALR14` | verify  `1` | OTP Verified Successfully `4`|
| `ALR15` | verify  `1` | OTP Expired. OTP Regenerated `5` |
