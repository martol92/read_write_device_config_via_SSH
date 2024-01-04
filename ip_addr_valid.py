for address in ip_list:
        ip_octets = []
        address = address.rstrip("\n").split(".")
        ip_octets.append(address)

        if(len(ip_octets) == 4 and (int(ip_octets[0]) <= 223) and (int(ip_octets[0]) != 127) and (int(ip_octets[0]) != 169 or int(ip_octets[1] != 225)) and (1 <= int(ip_octets[1]) <= 255 and 1 <= int(ip_octets[2]) <= 255 and 1 <= int(ip_octets[3]) <= 255)):
            continue
        else:
            print("Tis is an invalid ip address {}" .format(address))