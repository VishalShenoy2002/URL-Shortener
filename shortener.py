import sys
import argparse
from pyshorteners.shorteners import tinyurl
 
def checkValidity(args:argparse.Namespace):

    if args.url is not "":
        return "VALID" 

    else:
        return "MAIN"

def shortenURL(url:str):

    shotener=tinyurl.Shortener()
    shorturl=shotener.short(url)

    return shorturl
    


        
if __name__ == "__main__":
    parser=argparse.ArgumentParser(prog="Shortner",description="CLI Application which shortens url's")
    parser.add_argument("-u","--url",default="",type=str)
    args=parser.parse_args()

    validity=checkValidity(args)

    if validity is "VALID":
        shorturl=shortenURL(args.url)
        print(f"DEATAILS : {validity}")
    else:
        url=input("Enter URL You want to Shorten: ")
        shorturl=shortenURL(url)
    
    print(f"SHORT URL: {shorturl}")
        
    


