# Test SMTP Connection
## SMTP
```bash
telnet smtp.gmail.com 25
Trying 74.125.68.109...
Connected to smtp.gmail.com.
Escape character is '^]'.
220 smtp.gmail.com ESMTP m6sm1314984pfc.133 - gsmtp
```

## SMTPS

### Using SSL
```bash
openssl s_client -connect smtp.gmail.com:465
CONNECTED(00000003)
depth=2 OU = GlobalSign Root CA - R2, O = GlobalSign, CN = GlobalSign
verify return:1
depth=1 C = US, O = Google Trust Services, CN = GTS CA 1O1
verify return:1
depth=0 C = US, ST = California, L = Mountain View, O = Google LLC, CN = smtp.gmail.com
verify return:1
---
Certificate chain
 0 s:C = US, ST = California, L = Mountain View, O = Google LLC, CN = smtp.gmail.com
   i:C = US, O = Google Trust Services, CN = GTS CA 1O1
 1 s:C = US, O = Google Trust Services, CN = GTS CA 1O1
   i:OU = GlobalSign Root CA - R2, O = GlobalSign, CN = GlobalSign
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIExjCCA66gAwIBAgIQVkWCHiVGZO8DAAAAAMv3iDANBgkqhkiG9w0BAQsFADBC
...<omitted>
MwPSLvh2HjaIF7pQ49VSqgSjKEp26EWNP+4GKVUdPGObFxC/PmXjQrWKVfWnegqt
VrtCxAkMXdLFaiIK8pxlTZUIk1yYSJUSfbw=
-----END CERTIFICATE-----
subject=C = US, ST = California, L = Mountain View, O = Google LLC, CN = smtp.gmail.com

issuer=C = US, O = Google Trust Services, CN = GTS CA 1O1

---
No client certificate CA names sent
Peer signing digest: SHA256
Peer signature type: ECDSA
Server Temp Key: X25519, 253 bits
---
SSL handshake has read 2639 bytes and written 386 bytes
Verification: OK
---
New, TLSv1.3, Cipher is TLS_AES_256_GCM_SHA384
Server public key is 256 bit
Secure Renegotiation IS NOT supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
Early data was not sent
Verify return code: 0 (ok)
---
---
Post-Handshake New Session Ticket arrived:
...<omitted>
---
read R BLOCK
220 smtp.gmail.com ESMTP gb9sm9409673pjb.7 - gsmtp
```

### Using TLS
```bash
openssl s_client -starttls smtp -connect smtp.gmail.com:587
CONNECTED(00000005)
depth=2 OU = GlobalSign Root CA - R2, O = GlobalSign, CN = GlobalSign
verify return:1
depth=1 C = US, O = Google Trust Services, CN = GTS CA 1O1
verify return:1
depth=0 C = US, ST = California, L = Mountain View, O = Google LLC, CN = smtp.gmail.com
verify return:1
---
Certificate chain
 0 s:/C=US/ST=California/L=Mountain View/O=Google LLC/CN=smtp.gmail.com
   i:/C=US/O=Google Trust Services/CN=GTS CA 1O1
 1 s:/C=US/O=Google Trust Services/CN=GTS CA 1O1
   i:/OU=GlobalSign Root CA - R2/O=GlobalSign/CN=GlobalSign
---
Server certificate
-----BEGIN CERTIFICATE-----
MIIExjCCA66gAwIBAgIQVkWCHiVGZO8DAAAAAMv3iDANBgkqhkiG9w0BAQsFADBC
...<omitted>...
VrtCxAkMXdLFaiIK8pxlTZUIk1yYSJUSfbw=
-----END CERTIFICATE-----
subject=/C=US/ST=California/L=Mountain View/O=Google LLC/CN=smtp.gmail.com
issuer=/C=US/O=Google Trust Services/CN=GTS CA 1O1
---
No client certificate CA names sent
Server Temp Key: ECDH, X25519, 253 bits
---
SSL handshake has read 3071 bytes and written 316 bytes
---
New, TLSv1/SSLv3, Cipher is ECDHE-ECDSA-CHACHA20-POLY1305
Server public key is 256 bit
Secure Renegotiation IS supported
Compression: NONE
Expansion: NONE
No ALPN negotiated
SSL-Session:
    Protocol  : TLSv1.2
    Cipher    : ECDHE-ECDSA-CHACHA20-POLY1305
    Session-ID: 025EACDB2907E4B3A6A8281757E8D26267B94046042B86A0393692DAB4771D45
    Session-ID-ctx:
    Master-Key: 8F34FE9B422432F74BD062C7FD7D03B7A52A07682D50AF313CD7D5931900D30757E198C89B5E4DF3B4C813B00248C8EB
    TLS session ticket lifetime hint: 100800 (seconds)
    TLS session ticket:
    0000 - 01 db 8c 82 9a 73 82 f7-cd d0 21 06 99 ce 19 c6   .....s....!.....
    ...<omitted>...

    Start Time: 1621007660
    Timeout   : 7200 (sec)
    Verify return code: 0 (ok)
---
250 SMTPUTF8
ehlo gmail.com
250-smtp.gmail.com at your service
250-SIZE 35882577
250-8BITMIME
250-AUTH LOGIN PLAIN XOAUTH2 PLAIN-CLIENTTOKEN OAUTHBEARER XOAUTH
250-ENHANCEDSTATUSCODES
250-PIPELINING
250-CHUNKING
250 SMTPUTF8
```

## Other utilities
- telnet-ssl: apt install telnet-ssl
- gnutls-cli: apt install gnutls-cli

## Reference

- https://qmail.jms1.net/test-auth.shtml
- https://www.samlogic.net/articles/smtp-commands-reference-auth.htm
- https://www.ndchost.com/wiki/mail/test-smtp-auth-telnet