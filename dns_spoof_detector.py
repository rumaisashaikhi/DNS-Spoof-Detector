import dns.resolver
import socket

def get_real_ip(domain):
    try:
        # Public DNS se real IP
        answers = dns.resolver.resolve(domain, 'A')
        return answers[0].to_text()
    except:
        return None

def get_local_ip(domain):
    try:
        # Local DNS resolution
        return socket.gethostbyname(domain)
    except:
        return None

def detect_dns_spoof(domain):
    print(f"\nChecking domain: {domain}")

    real_ip = get_real_ip(domain)
    local_ip = get_local_ip(domain)

    print(f"Real IP: {real_ip}")
    print(f"Local DNS IP: {local_ip}")

    if real_ip != local_ip:
        print("⚠️ ALERT: Possible DNS Spoofing Detected!")
    else:
        print("✅ No DNS spoofing detected.")

# Run
domain = input("Enter domain to check: ")
detect_dns_spoof(domain)
