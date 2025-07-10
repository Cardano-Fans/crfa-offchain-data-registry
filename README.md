# CRFA Offchain Data Registry

This registry contains mappings of script hashes to dApps. Please add your project here or correct mistakes. We are maintaining it on best effort basis.

## JSON Schema

The structure of dApp entries is defined in [dapp-schema.json](./dapp-schema.json). This schema ensures consistency across all dApp entries in the registry.

## Caveats

In the eUTXO model smart contracts are not deployed to an address so there is nothing that forces smart contracts to use a single script hash. Nothing stops a project from having a script hash that changes over time by inlining data into the script.

## dApp File Structure

The name of the .json file should be the dApp name (in case it already exists, please update the existing one, if not create new one). The structure must follow the [JSON Schema](./dapp-schema.json).