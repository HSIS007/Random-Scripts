**Attack 1: Domain Trust Enumeration and Abuse using PowerView**

- Enumerate users who are in groups outside of the users primary domain (Get-DomainForeignUser)
- Enumerate groups in a domain  with users who are outside of the groups primary domain (Get-DomainForeignGroupMember)

* * *

**Attack 2: Over Pass-The-Hash (Pass-the-Key)**

- Uses kerberos encryption keys to request a TGT (no password is needed)
- You can read kerberos encryption key from lsass.exe ,dcsync  or calculate the keys using Rubeus (if you have password for user)
- We can use AES256 kerberos encryption keys instead of RC4 as it would work fine as well

* * *

**Attack 3: Pass-the-Ticket**
    - Extracted Kerberos tickets(kirbi file or b64 blob) can be used to load into different machine to use on different machine with particular user privileges
    - CS: Make a new token and then create a new token in sacrificial logon session to spawn a new beacon slide : 355

* * *

**Attack 4: Kerberoasting**
    - In this we abuse the step where when we are requesting a service ticket to system/service on the network. This is called Kerberoasting. Once we have TGT and want to access file share, SQL server etc. then we present our TGT to DC with the name (SPN) of the service. DC would then provide us service ticket which is encrypted with the service account password. So this password can be any domain user or machine account, which is running the service.
    - Password if encrypted with weak password then we can crack them
    - Type 18 : AES
    - Type 23 : RC4
    - **OPSEC**:
        - Only request a ticket for privileged or potentially useful account not all accounts
        - Target older account to avoid detection from honeypots
        - Only request RC4 tickets using Rubeus.exe /rc4opsec
    - **Detections:**
        - Event ID : 4769 for service ticket request
        - We can setup honeypots
        - Look for RC4 encryption for accounts with AES enabled

* * *

**Attack 5: AS-REP Roasting**
    - Pre-Authentication is not enabled, which means that if I want to logon as IT admin then DC will send ticket back which is encrypted with that user password. We can then decrypt that ticket to get the password
    - We can query DC to find accounts with Pre-Authentication not enabled

* * *

- **Attack 6: Golden Tickets**
    - Forged TGTs
    - krbtgt hash is compromised and forget new TGTs, with this ability we can be anybody, can be part of any group etc
    - interesting groups
        - 512 : Administrator
        - 513: Domain Controllers
        - 518 and 519 : Enterprise Admins
        - 520 : Schema Admins
    - **OPSEC**:
        - Blend in as much as possible, match /groups, /user and /id
        - If account does not exist then you have  20 mins before non existing user is validated

* * *

**Attack 7: Trust Attacks using krbtgt**
    - **SID History** **Hopping** : If any user in any child domain has a SID History of enterprise admins then that user gains Enterprise admin access on every domain controller in the forest

* * *

**Attack 8: Silver Tickets**
    - Effects the last part of Kerberos process, we are forging a TGS-REPs ticket, which is encrypted by machine account hash.
    - Compromise machine account hash and forge our own TGS-REPs to access the server/service. So we can pretend to be any user we want, can put yourself in any group.
    - No DC interaction as it has very stealth.
    - Machine password are changes every 30 days by default.
    - Encrypted and Signed by the NTLM hash of the machine account (Golden ticket is signed by hash of krbtgt) of the service running with that account.
    - /service: we can access CIFS for share, HOST and RPCSS for WMI, HOST and HTTP for PowerShell Remoting and WinRM.

* * *

**Attack 9: Kerberos Delegation**
    - **Constrained:** If we compromise the account with constrained delegation, we can request a service ticket to IIS for any user in the domain, including a domain administrator. It is set through the **msds-allowedtodelegateto** property
    - **Unconstrained:** If we succeed in compromising the web server service and a user authenticates to it, we can steal the user’s TGT and authenticate to any service. This is especially interesting if the authenticating user is a high-privileged domain account.
    - **RBCD:** The **msDS-AllowedToActOnBehalfOfOtherIdentity** property controls delegation from the backend service and their is no need for SeEnableDelegationPrivilege permissions.

* * *

**Attack 10: sAMAccountName Spoofing**

- https://mez0.cc/posts/pac-domain-controller-impersonation/
- https://exploit.ph/cve-2021-42287-cve-2021-42278-weaponisation.html

* * *

**Attack 11: SHADOWCOERCE**

- https://pentestlaboratories.com/2022/01/11/shadowcoerce/

* * *

**Attack 12: NTLM Relay to ADCS Certificate **

- https://pentestlab.blog/2021/09/14/petitpotam-ntlm-relay-to-ad-cs/


