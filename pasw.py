import requests
import argparse


ayristirici = argparse.ArgumentParser()
ayristirici.add_argument('--foo', help='foo yardım')
ayristirici.add_argument('-u', '--user', required=True, help="Kullanıcı adı gir")
ayristirici.add_argument('-p', '--pass', required=True, help="Sifre Gir")
#print(ayristirici.print_help())

args = vars(ayristirici.parse_args())

#print(args["user"])
#print(args["pass"])
user=args["user"]
pw=args["pass"]
print("Kulanıcı adı: "+user+" -- Sifre: "+pw)
r = requests.post('http://gordion.shaiyatr.net/member/trylog.php', data={'user': user, 'pw': pw })
print(r.text)