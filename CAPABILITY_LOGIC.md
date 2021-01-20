Client Capability Logic
=======================

This logic operates on an 802.11 association request frame, looking at various tagged parameter
values to determine client capabilities.

1. 802.11n: inspect tagged parameter number 45 (HT Capabilities)
    - a. is tagged parameter present? 
        - Y - 802.11n supported
        - N - 802.11n not supported
    - b. inspect octets 3 to 7 (Rx MCS sets) 
        - count Rx MCS bitmasks that are set (11111111) to determine number of streams supported
        
2. 802.11ac: inspect tagged parameter 191 (VHT Capabilities)
    - a. is tagged parameter present?
        - Y - 802.11ac supported
        - N - 802.11ac not supported
    - b. inspect octets 4 & 5 (Rx MCS map) - 
        - count Rx MCS map bit pairs set to '10' to determine number of streams supported
    - c. inspect octet 1 (one of the four vht capability octets)
        - if bit zero set to '1', client is SU Beam-formee capable
    - d. inspect octet 2 (one of the four vht capability octets)
        - if bit zero set to '1', client is MU Beam-formee capable        

3. 802.11k: inspect tagged parameter 70 (RM Enabled Capabilities) - RM = radio management
    - a. is tagged parameter present?
        - Y - 802.11k supported
        - N - 802.11k not supported

4. 802.11r - inspect tagged parameter 54 (Mobility Domain)
    - a. is tagged parameter present? 
        - Y - 802.11r supported
        - N - 802.11r not supported

5. 802.11v - inspect tagged parameter 127 (Extended capabilities)
    - a. is tagged parameter present?
        - N - 802.11v not supported
        - Y - 802.11v may be supported
            - does octet 3 exist in ext capabilities tagged parameter?
                - N - 802.11v not supported
                - Y - 802.11v may be supported
                    - a. is bit 3 of octet 3 set to '1'?
                        - Y - 802.11v is supported
                        - N - 802.11v not supported

6. Max/Min Power - inspect tagged parameter 33 (Power Capability)
    - a. is tagged parameter present?
        - N - unable to report max power
        - Y - inspect octet 0 & 1 of tagged parameter
            - a. octet 1 - max power in dBm
            - b. octet 0 - min power in dBm

7. Supported channels - inspect tagged parameter 6 (Supported Channels)
    - a. Step through each channel set octet-pair provided reporting start channel and other channels in range
        - Note: use step of 4 if start channel above number 14 (must be 5GHz channels), use step of 1 otherwise

8. 802.11w: inspect tagged parameter 48 (RSN capabilities) 
    - a. is bit 8 of 2nd last octet in the rsn capabilities field set?
        - Y - 11w supported
        - N - 11w not supported

9. 802.11ax inspect extended tag number 35 (HE Capabilities)
    - a. is HE capabilities tagged parameter present? 
        - Y - 802.11ax supported
        - N - 802.11ax not supported
    - b. (TBA) number of spatial streams
    - c. (TBA) BSS coloring
    - d. (TBA) UL/DL OFMDA
    - e. (TBA) UL/DL MU-MIMO