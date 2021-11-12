# Authoritative Pool
- Allow clients with static IP can request other parameters dynamically by using DHCPinform.
    - Authoritative server will reply DHCPinform with DHCPACK. 
    - Non-Authoritative server will ignore DHCPinform packets
- https://techhub.hpe.com/eginfolib/networking/docs/switches/WB/15-18/5998-8162_wb_2920_mcg/content/ch06s04.html