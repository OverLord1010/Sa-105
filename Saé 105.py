import urllib.request
import json
import time


def trie_ip(): 
    f = open("controltower_access.log", "r")
    j = open("ip_trie.txt", "w")

    listip=[]
    for ligne in f :
        a=ligne.split(" ")
        if a[0] in listip:
            continue
        else:
            listip.append(a[0])
            j.write(a[0])
            j.write("\n")
    print(listip)
    f.close()
    j.close()

def trie_access():
    f = open("controltower_access.log", "r")
    j = open("access_trie.txt", "w")

    listip=[]
    for ligne in f :
        a=ligne.split(" ")
        if a[0] in listip:
            continue
        else:
            listip.append(a[0])
            j.write(ligne)
    print(listip)
    f.close()
    j.close()

"""trie_ip()"""
"""trie_access()"""

def gene_lat_lon(liste) :
    j = open("longi_lati.txt", "w")
    tab=[]
    url = "http://ip-api.com/json/"
    for ip in liste:
        time.sleep(1)
        response = urllib.request.urlopen (url + ip)
        data = response.read()
        values = json.loads(data)
        lati=values['lat']
        longi=values['lon']
        tab.append([ip,lati,longi])
        print([ip,lati,longi])
        j.write(ip)
        j.write(str(lati))
        j.write(str(longi))
    return(tab)

f = open("ip_trie.txt", "r")
gene_lat_lon(f)