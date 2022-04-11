# icloud-to-vaultwarden

This is a simple script that takes iCloud websites passwords CSV file exported from Safari and converts it to Bitwarden / Vaultwarden CSV.

Apart from reorganizing column order and veryfying / adding headers, the only thing it does is removing usernnames from "description" field, as bitwarden is showing username under description anyway.

## Dependencies

Should run on any modern Python (3.6+)

## Usage

```icloud_to_vaultwarden.py [-h] -i INPUT [-o OUTPUT]```

INPUT must be a valid file exported from Safari (it is checked for headers), output defaults to `` if not specified.

## Sanity check

* Have you read the source?
* Do you know me personally and trust me?
* Do you know what you are doing? 

If not, please do not use this script. Password management is a serious thing. I am not responsible in any way for any damages you may cause by using my code.