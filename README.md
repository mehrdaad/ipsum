![Logo](logo.png)

[![License](https://img.shields.io/badge/license-Public_domain-red.svg)](https://wiki.creativecommons.org/wiki/Public_domain)

About
----

**IPsum** is a threat intelligence feed based on 30+ different publicly available [lists](https://github.com/stamparm/maltrail) of suspicious and/or malicious IP addresses. All lists are automatically retrieved and parsed on a daily (24h) basis and the final result is pushed to this repository. List is made of IP addresses together with a total number of (black)list occurrence (for each). Greater the number, lesser the chance of false positive detection and/or dropping in (inbound) monitored traffic. Also, list is sorted from most (problematic) to least occurent IP addresses.

As an example, to get a fresh and ready-to-deploy auto-ban list of "bad IPs" that appear on at least 3 (black)lists you can run:

```
curl --compressed https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt 2>/dev/null | grep -v "#" | grep -v -E "\s[1-2]$" | cut -f 1
```

If you want to try it with `ipset`, you can do the following:

```
sudo su
apt-get -qq install iptables ipset
ipset -q flush ipsum
ipset -q create ipsum hash:net
for ip in $(curl --compressed https://raw.githubusercontent.com/stamparm/ipsum/master/ipsum.txt 2>/dev/null | grep -v "#" | grep -v -E "\s[1-2]$" | cut -f 1); do ipset add ipsum $ip; done
iptables -I INPUT -m set --match-set ipsum src -j DROP
```

In directory [levels](levels) you can find preprocessed raw IP lists based on number of blacklist occurrences (e.g. [levels/3.txt](levels/3.txt) holds IP addresses that can be found on 3 or more blacklists).

**Important:** If you are planning to use `git` to get the content of this repository do it like `git clone --depth 1 https://github.com/stamparm/ipsum.git`

Donations
----

If you appreciate the work please consider making a donation via [PayPal](https://www.paypal.com/) to `miroslav.stampar@gmail.com` or via [&#x0243;itcoin](bitcoin:1JCtgmpC1eWvdHXrKfvMAunfvcaaMXLP5G) to `1JCtgmpC1eWvdHXrKfvMAunfvcaaMXLP5G`.

Wall of shame (2017-11-04)
----

|IP|DNS lookup|Number of (black)lists|
|---|---|--:|
197.231.221.211|exit1.ipredator.se|13
62.210.37.82|62-210-37-82.rev.poneytelecom.eu|13
104.223.123.98|unassigned.quadranet.com|12
199.87.154.255|tor.les.net|12
85.248.227.163|ori.enn.lu|12
89.234.157.254|marylou.nos-oignons.net|11
62.210.105.116|62-210-105-116.rev.poneytelecom.eu|11
171.25.193.20|tor-exit0-readme.dfri.se|11
80.67.172.162|algrothendieck.nos-oignons.net|11
170.250.140.52|170.250.140.52.hwccustomers.com|11
62.102.148.67|-|11
23.129.64.11|tor01.emeraldonion.org|11
176.126.252.12|aurora.enn.lu|11
155.133.64.203|-|11
192.42.116.16|tor-exit.hartvoorinternetvrijheid.nl|11
5.254.79.66|lh31139.voxility.net|10
128.31.0.13|tor-exit.csail.mit.edu|10
51.15.53.83|83-53-15-51.rev.cloud.scaleway.com|10
64.113.32.29|tor.t-3.net|10
171.25.193.25|tor-exit5-readme.dfri.se|10
65.19.167.132|-|10
171.25.193.77|tor-exit1-readme.dfri.se|10
171.25.193.78|tor-exit4-readme.dfri.se|10
216.239.90.19|tor-gateway.vif.com|10
212.21.66.6|tor-exit-4.all.de|10
46.165.230.5|tor-exit.dhalgren.org|10
192.160.102.170|ogopogo.relay.coldhak.com|10
5.254.112.154|lh31138.voxility.net|10
85.248.227.164|tollana.enn.lu|10
77.247.181.162|chomsky.torservers.net|10
207.244.70.35|-|9
185.117.215.9|tor3.digineo.de|9
171.25.193.235|tor-exit3-readme.dfri.se|9
5.188.11.165|hostby.westvps.eu|9
163.172.212.115|163-172-212-115.rev.poneytelecom.eu|9
155.4.230.97|h-4-230-97.A328.priv.bahnhof.se|9
5.101.40.38|-|9
5.101.40.37|-|9
51.15.141.220|220-141-15-51.rev.cloud.scaleway.com|9
183.136.188.116|-|9
71.6.146.186|inspire.census.shodan.io|9
60.173.82.156|-|9
51.255.202.66|tor.asmer.com.ua|9
61.188.189.5|5.189.188.61.broad.nc.sc.dynamic.163data.com.cn|9
185.107.81.233|-|9
163.172.217.50|163-172-217-50.rev.poneytelecom.eu|9
18.85.22.204|wholesomeserver.media.mit.edu|9
212.47.227.114|-|9
222.85.224.95|-|9
218.60.136.106|-|9
198.96.155.3|exit.tor.uwaterloo.ca|9
192.160.102.168|prawksi.relay.coldhak.com|9
218.98.32.157|-|9
85.248.227.165|-|9
5.188.10.179|-|9
185.100.87.206|-|9
185.100.87.207|-|9
218.8.128.233|-|8
163.172.101.137|de-rien.fr|8
218.156.85.17|-|8
120.52.96.35|-|8
94.142.242.84|tor-exit-1.zenger.nl|8
5.188.10.156|-|8
58.221.249.102|-|8
212.129.18.55|212-129-18-55.rev.poneytelecom.eu|8
195.22.126.178|-|8
51.15.87.157|exit1.tor.short.dog|8
46.148.20.25|druid.vps|8
60.165.208.28|28.208.165.60.dail.dx.gs.dynamic.163data.com.cn|8
111.40.124.43|-|8
163.172.136.101|tor.ohundred.com|8
162.247.72.200|kiriakou.tor-exit.calyxinstitute.org|8
58.48.178.200|-|8
45.63.70.88|45.63.70.88.vultr.com|8
185.165.29.84|-|8
193.171.202.150|-|8
219.232.206.249|-|8
123.164.227.204|-|8
60.7.70.205|-|8
103.207.36.251|-|8
213.8.199.27|diup-199-27.inter.net.il|8
180.153.19.139|-|8
165.227.113.9|-|8
114.207.154.2|-|8
176.10.104.240|tor1e1.digitale-gesellschaft.ch|8
31.184.194.114|mastermail1.ru|8
5.199.130.188|tor.piratenpartei-nrw.de|8
23.129.64.12|tor02.emeraldonion.org|8
51.15.8.100|51-15-8-100.rev.poneytelecom.eu|8
96.255.14.191|pool-96-255-14-191.washdc.fios.verizon.net|8
178.20.55.18|marcuse-2.nos-oignons.net|8
178.20.55.16|marcuse-1.nos-oignons.net|8
181.214.87.4|-|8
91.212.150.219|-|8
89.248.167.131|mason.census.shodan.io|8
185.100.85.101|-|8
185.129.62.62|tor01.zencurity.dk|8
192.160.102.166|chaucer.relay.coldhak.com|8
121.108.193.86|KD121108193086.ppp-bb.dion.ne.jp|8
51.15.43.205|tor4thepeople3.torexitnode.net|8
203.190.163.125|-|8
202.107.104.119|-|8
71.6.135.131|census7.shodan.io|8
111.75.200.68|-|8
46.17.97.112|-|8
210.206.120.250|-|8
185.158.113.62|-|8
138.19.133.51|138019133051.ctinets.com|8
222.173.194.9|-|8
166.70.207.2|this.is.a.tor.node.xmission.com|8
185.94.111.1|-|8
204.85.191.31|tor01.telenet.unc.edu|8
37.220.35.202|wagyolo.10g.chmuranet.com|8
213.61.149.100|-|8
156.67.106.30|-|8
118.186.36.50|-|8
93.115.95.202|lh28409.voxility.net|8
162.247.73.206|rosaluxemburg.tor-exit.calyxinstitute.org|8
46.246.37.180|anon-37-180.vpn.ipredator.se|8
80.76.245.198|-|8
37.187.94.86|ns3035851.ip-37-187-94.eu|8
51.15.63.229|229-63-15-51.rev.cloud.scaleway.com|8
