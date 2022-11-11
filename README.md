# crfa-offchain-data-registry

This registry contains mappings of script hashes to dApps. Please add your project here or correct mistakes. We are maintaining it on best effort basis.


Caveats:
In the eUTXO model smart contracts are not deployed
to an address so there is nothing that forces smart contracts
to use a single script hash.
Nothing stops a project from having a script hash that changes over time by inlining data into the script

## Explanation for dapp file:
The name of the .json file should be the dApp name (in case it already exists, please update the existing one, if not create new one)

```
{   

    "id": "",                            // random 8 characters unique dApp id
    "projectName": "",                   // dApp name
    "link": "",                          // dApp main page link
    "twitter": "",                       // dApp twitter page link
    "category": "",                      // categories: DEFI, MARKETPLACE, COLLECTION, GAMING, COMMUNITY, TOKEN_DISTRIBUTION
    "subCategory": "",                   // sub-categories: AMM_DEX, ORDERBOOK_DEX, HYBRID_DEX, LENDING_BORROWING, NFT, ORACLE, WRAPPED_ASSETS
    "description": {
                   "short": ""           // short description of the dapp
    },	
    "features": [""],                     // dApp various features (for example: SWAP, LEND, YIELD, etc.)      
    
	                                  // each smart contract or batch of smart contracts to be grouped by releases
	                                  // (in present example: 2 releases, old and current one)
   "releases": [
   
        {
            "releaseNumber": 1,
            "releaseName": "V1",
            "description": "initial version of all scripts",
            "scripts":                     // scripts id of this particular release (in this example: 2 scripts)
                                           // random 6 characters unique script id (detailed at the scripts section at the end) 
                                           // the ids here must match the ones in script section
            [
                {
                    "id": "",
                    "version": 1
                },
                {
                    "id": "",
                    "version": 1
                }
            ]                                                    
        },
        {
            "releaseNumber": 2,                                        
            "releaseName": "V2",
            "description": "latest version of all scripts",
            "scripts":                        // scripts id of this particular release (in this example: 2 scripts)
                                              // random 6 characters unique script id (detailed at the scripts section at the end) 
                                              // the ids here must match the ones in script section
            [
                {
                    "id": "",
                    "version": 2
                },
                {
                    "id": "",
                    "version": 2
                }
             ],                                                   
        "auditId": "",                          // random 4 characters unique audit Id of the last released scripts that point
                                                // to current release (detailed in audits section)
        "contractId": ""                        // random 4 characters unique open source Id of the last released scripts that
                                                // point to current release (detailed in open source section)
        }              
    ],
    
    "contracts": [                              // open source section
        {
         "openSource": true,                    // true or false, depending on the case
         "contractLink": "",                    // open source contracts link
         "contractId": ""                       // random 4 characters unique open source Id
        }
    ],
    "audits": [                                 // audit section
        {
         "auditId": "",                         // random 4 characters unique audit Id
         "auditor": "",                         // auditor company name
         "auditLink": "",                       // audit report link
         "auditType": "MANUAL"                  // audit type: MANUAL or AUTOMATIC
        }        
    ],
    "scripts": [                                // SPEND scripts detail section
        {
            "id": "",                           // random 6 characters unique SPEND script id
            "name": "",                         // SPEND script name
            "purpose": "SPEND",                 // script type SPEND
            "versions": [
                {
                    "version": 1,               // older version of the SPEND script
		    "plutusVersion": 1,         // Plutus V1 or V2
	            "fullScriptHash": "",	// prefix and script hash or script hash+staking key, depending on the dAPP	    
                    "scriptHash": "",           // script hash or script hash+staking key, depending on the dAPP
                    "contractAddress": ""       // script address
                },
                {
                    "version": 2,               // latest version of the SPEND script
		    "plutusVersion": 2,         // Plutus V1 or V2
	            "fullScriptHash": "",	// prefix and script hash or script hash+staking key, depending on the dAPP
                    "scriptHash": "",           // script hash or script hash+staking key, depending on the dAPP
                    "contractAddress": ""       // script address
                }
            ]
        },                     
        {
            "id": "",                           // random 6 characters unique MINT script id
            "name": "",                         // MINT script name
            "purpose": "MINT",                  // script type MINT
            "versions": [
                {
                    "mintPolicyID": "",         // older MINT script policy ID
                    "version": 1                // older version of the MINT script
                },
                {
                    "mintPolicyID": "",          // latest version of the MINT script policy ID
                    "version": 2                 // latest version of the MINT script
                }
            ]
        }
    ]
}
```
