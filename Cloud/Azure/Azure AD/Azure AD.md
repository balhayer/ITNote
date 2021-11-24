# External Identity
- Tenant: Resource Tenant (where the app or resource is), Account Tenant (Where the account is)
# Authentication Method for Azure AD Hybrid Identity
- Cloud Authentication
    - Azure AD password hash synchronization: enable authentication for on-prem objects in Azure AD, users can use same username and password 
    - Azure AD Pass-through Authentication (PTA): provides password validation for Azure AD authentication by using an agents running on on-prem servers.
- Federated Authentiation
    - Hands off authentication proceses to another trusted system such as on-prem AD Federation Services (AD FS)

## Note
- premium fetures like Identity Protection and Azure AD Domain Services required password hash sync
- Sign in features not natively supported by Azure AD
    - Sign-in using smartcards or certificates.
    - Sign-in using on-premises MFA Server.
    - Sign-in using third-party authentication solution.
    - Multi-site on-premises authentication solution.
- https://docs.microsoft.com/en-us/azure/active-directory/hybrid/choose-ad-authn