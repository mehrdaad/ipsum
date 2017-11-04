import re
import subprocess
content = open("shame.txt", "rb").read()
for ip in re.findall(r"\b(\d+\.\d+\.\d+\.\d+)\|", content):
    process = subprocess.Popen("nslookup %s" % ip, stdout=subprocess.PIPE, shell=True)
    stdout = process.communicate()[0]
    match = re.search(r"\bname = ([^\s]+)", stdout)
    name = '-'
    if match:
        name = match.group(1).strip('.')
        if name.endswith('.in-addr.arpa'):
            name = '-'
    content = re.sub(r"\b%s\|" % re.escape(ip), "%s|%s|" % (ip, name), content)
open("shame.txt", "w+b").write(content)
