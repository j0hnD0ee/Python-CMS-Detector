#!/usr/bin/env/python
#-*-coding:utf-8-*-
# little cms detecor by johnd0e
# in line 15 u can add some directory for add some cms :)
import sys,urllib
__banner__="""\033[1;37m

- MINI CMS DETECTOR BY JOHNDOE -

"""
def johncms():
    site=sys.argv[1]
    print __banner__
    print "\033[1;37m\033[31m[-] \033[1;37mSite : "+site+""
    print "\033[1;37m\033[31m[+] \033[1;37mCMS en cours de scan.."
    list={"/wp-content/":"Wordpress","/administrator":"Joomla","/FCKeditor/editor/":"FCKeditor","/typo3conf/":"Typo3","/misc/drupal.js":"Drupal","/skin/frontend/":"Magento","/phpmyadmin":"phpmyadmin"}
    for (url,cms) in list.items():
        full=""+site+"/"+url+""
        try:
            lookit=urllib.urlopen(full)
            if lookit.getcode() == 200:
                print "\033[34m[*]\033[1;37m "+cms+" \033[31m=> \033[1;37mCMS Trouver :D"
            else:
                print "\033[1;37m\033[31m[-]\033[1;37m "+cms+" \033[31m=> \033[31mNope"
        except:
            print "\033[31m[-] \033[1;37mUtilisation : python "+sys.argv[0]+" http://site.com"
            sys.exit()
    print "\033[31m[!] \033[1;37mScan fini :p"
    print "\033[31m[!] \033[1;37mByebye :)"
    sys.exit()
if __name__ == "__main__":
    if len(sys.argv) !=2:
        print __banner__
        print "\033[31m[-] \033[1;37mUtilisation : python "+sys.argv[0]+" http://site.com"
    else:
        johncms()
