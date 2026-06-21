import socket
import threading

# Limit thread number
thread_limit = threading.Semaphore(20)
def scan(subdomain):
    with thread_limit:
        target_domain = 'google.com'
        full_url = f'{subdomain}.{target_domain}'

        # Get DNS Record A 
        try:
            ip = socket.gethostbyname(full_url)
            print(f"[FOUND] {full_url} -> {ip}")
            
        except socket.gaierror as e:
            pass

print('[+] Starting DNS enumeration...')

wordlist = [
"www", "mail", "ftp", "localhost", "webmail", "smtp", "pop3", "imap",
"dev", "test", "staging", "stage", "prod", "beta", "alpha", "demo", 
"local", "lab", "sandbox", "git", "gitlab", "github", "jenkins", "docker",
"admin", "administrator", "portal", "dashboard", "panel", "cpanel", 
"root", "manager", "control", "setup", "config", "login", "signin",
"api", "v1", "v2", "status", "cloud", "aws", "s3", "storage", "cdn", 
"dns", "ns1", "ns2", "vpn", "gateway", "router", "firewall", "proxy",
"shop", "store", "cart", "checkout", "billing", "pay", "payment", 
"blog", "forum", "news", "help", "support", "docs", "wiki", "faq",
"internal", "intranet", "corp", "staff", "secure", "security", 
"auth", "sso", "oauth", "db", "database", "sql", "mysql", "oracle"]

# Start thread
for subdomain in wordlist:
    t = threading.Thread(target=scan, args=(subdomain,))
    t.start()



