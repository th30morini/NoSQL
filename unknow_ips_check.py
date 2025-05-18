import ipaddress
from connexion import get_connexion

def detect_unknown_ips():
    db = get_connexion()
    if db is None:
        return

    collection = db["logs"]

    # Liste blanche de plage IP
    whitelist = ipaddress.ip_network("192.168.1.0/24")

    all_ips = collection.distinct("ip")
    print("\nIPs inconnues :")

    for ip in all_ips:
        try:
            ip_obj = ipaddress.ip_address(ip)
            if not (ip_obj in whitelist):
                print(f"IP inconnue : {ip}")
        except ValueError:
            print(f"Format IP invalide ignoré : {ip}")


#detect_unknown_ips()