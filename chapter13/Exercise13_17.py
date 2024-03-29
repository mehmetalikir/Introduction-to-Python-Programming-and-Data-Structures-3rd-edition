# Author: Hidir Sezgin, Mehmet A. Kir
# Email : hidirsezgin@gmail.com, m.kir@student.unsw.edu.au
# GitHub: /hidirsezgin, /mehmetalikir

'''(Baby name popularity ranking) The popularity ranking of baby names from
years 2001 to 2010 is downloaded from www.ssa.gov/oact/babynames and stored
in files named babynameranking2001.txt, babynameranking2002.txt, . . . ,
babynameranking2010.txt. Each file contains one thousand lines. Each line
contains a ranking, a boy’s name, number for the boy’s name, a girl’s name,
and number for the girl’s name. For example, the first two lines in the file
babynameranking2010.txt are as follows:
So, the boy’s name Jacob and girl’s name Isabella are ranked #1 and the boy’s
name Ethan and girl’s name Sophia are ranked #2. 21,875 boys are named
Jacob and 22,731 girls are named Isabella. Write a program that prompts the
user to enter the year, gender, and followed by a name, and displays the ranking
of the name for the year.'''

import urllib.request


def main():
    # Prompt the user to enter the year, gender and name
    year = 2010  # input("Please enter the year:")
    gender = 'M'  # input("Please enter the gender:")
    name = "Alex"  # input("Please enter the name:")
    url = f"https://liveexample.pearsoncmg.com/data/babynameranking{year}.txt".strip()

    # Create input file from url

    inputFile = urllib.request.urlopen(url)
    for line in inputFile:
        items = line.strip().split()

        if gender == 'M' and items[1] == name:
            print(f"Boy name {name} is ranked #{items[0]} in year {year}")
        if gender == 'F' and items[3] == name:
            print(f"Girl name {name} is ranked #{items[0]} in year {year}")

    inputFile.close()  # Close the input file


main()
