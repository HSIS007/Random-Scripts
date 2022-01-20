# Using RSAT and ActiveDirectory module to enumerate DCSync rights, this tehcnique bypasses crowdstrike detection:

The “DS-Replication-Get-Changes” extended right
CN: DS-Replication-Get-Changes
GUID: 1131f6aa-9c07-11d1-f79f-00c04fc2dcd2

The “Replicating Directory Changes All” extended right
CN: DS-Replication-Get-Changes-All
GUID: 1131f6ad-9c07-11d1-f79f-00c04fc2dcd2

The “Replicating Directory Changes In Filtered Set” extended right (this one isn’t always needed but we can add it just in case :)
CN: DS-Replication-Get-Changes-In-Filtered-Set
GUID: 89e95b76-444d-4c62-991a-0facbeda640c

- Step 1: Install RSAT
- Step 2: Import-Module ActiveDirectory and check if active directory folder is created using "cd ad:"
- Step 3: (Get-Acl "ad:\dc=dragon,dc=com").Access | ? {$_.IdentityReference -match 'targetusername' -and ($_.ObjectType -eq "1131f6aa-9c07-11d1-f79f-00c04fc2dcd2" -or $_.ObjectType -eq "1131f6ad-9c07-11d1-f79f-00c04fc2dcd2" -or $_.ObjectType -eq "89e95b76-444d-4c62-991a-0facbeda640c" ) }
