# AuthLib Standardized Return Codes

Standardized Return Codes are used to make sure that every action in the AuthLib returns replicable, verifiable and comparable statments or objects.

Return codes are created using fragments of various scopes. For Example, return codes of  requestHandler methods can be different from that of generators.

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

### Script Scope

For The following scopes the return statements used for Handlers are -
| Scripts | Code |
| ------- | ---- |
| authProfileHandler  `P` |
| generators | `G` |
| mainenance | `M`|
| requests | `R` |