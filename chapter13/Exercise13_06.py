# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir


'''(Extract title fom web page) The following URL loads a random article from
Wikipedia: https://en.wikipedia.org/wiki/Special:Random. Write a program that
extracts the title of an article, by reading the content of the title element(i.e
the text between the "<title>" and </title> tags) Note: Depending on the setup on
your computer, you may need add code so as not to authenticate the SSL certificate
(ssl._create_default_http_context = ssl._create_unverified_context)'''

import ssl
import urllib.request


def main():
    # Open the URL
    ssl._create_default_https_context = ssl._create_unverified_context
    input = urllib.request.urlopen("https://en.wikipedia.org/wiki/Special:Random")
    s = input.read().decode()

    tagStart = str(s).find("<title>")  # Find the opening tag

    tagEnd = str(s).find('</title>')  # Find the closing tag

    # Extract the substring between the start and end tags
    print("The title of the page is " + str(s)[tagStart + 7:tagEnd])  # +7 to step <title>


main()
