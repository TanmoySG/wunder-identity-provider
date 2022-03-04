# wunder Identity Provider v0.1

The wunder Identity Provider is the primary IAM - Identity and Access Management platform for all wunder Platform Products. The idea is to unify the identity and access across the board for more coherent and hassle-free single-point service and data access.

The wIP Architecture has several moving parts, but broadly can be consolidated for the end-user into two primary access/interaction points - `registration` and `login`. 

The Architectural and Design details are documented [here](./architecture/README.md).

## Identity

The Identity of a User is uniquely defined (primarily) by the user's email ID, while the uID (system generated) and username (user defined) are used for secondary and tertiary identification. The (rough) ID Structure, that is stored and used can be found [here](./architecture/README.md#identity-specification). 

## Usage - 