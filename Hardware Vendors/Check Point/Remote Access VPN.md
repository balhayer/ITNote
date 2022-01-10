# Verification Commands
- List Office Mode VPN users (including SNX and L2TP): fw tab -t om_assigned_ips -f
- List SNX VPN users: fw tab -t sslt_om_ip_params -f
- List L2TP VPN user: fw tab -t L2TP_tunnels -f
- List MAB user (Not SNX just MAB portal): fw tab -t cvpn_session
- List Office Mode users that are currently connected in Visitor Mode: vpn show_tcpt

# Examples

- Get VPN logged-on users: fw tab -t sslt_om_ip_params -f | grep UserName | cut -f5 -d”;”
- Same as above, but just get username and sort ascending with case-ignore: fw tab -t sslt_om_ip_params -f | grep UserName | cut -f5 -d”;” | cut -f3 -d” ” | sort -f

# Reference

- https://community.checkpoint.com/t5/Remote-Access-VPN/Remote-Access-VPN-Short-List-of-Most-Useful-Resources-and-Tools/m-p/78983#M16070