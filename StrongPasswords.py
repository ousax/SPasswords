import os
import re # check is a given password is strong or not
import argparse # for prefix FB_STRONGPASSWORD
import random
import secrets
import string
from pyfiglet import figlet_format
from rich.console import Console
from rich.table import Table
from rich.traceback import install
from rich import print
install()
parser = argparse.ArgumentParser(
    description="Strong passwords generator"
)
parser.add_argument("-plen", help="The password's length [10 by default]", type=int, required=False, default=10)
parser.add_argument("-sf", help="Save to a file", type=str, required=False, default=None)
parser.add_argument("-pNumber", help="Number of passwords to generate", type=int, default=1000, required=False)
parser.add_argument("-all_", help="Use digits, strings, punctuation", type=int, choices=[0, 1], default=0)
parser.add_argument("-eXD", help="Exclude digits [0] to exlude digits [1] to include digits", type=int, choices=[0, 1], required=False, default=1)
parser.add_argument("-eXP", help="Exclude, Include punctuations [0] exlude, [1] include", type=int, choices=[0, 1], required=False, default=1)
parser.add_argument("-eXS", help="Exclude, Include letters [lower, upper case] [0] exlude, [1] include", type=int, choices=[0, 1], required=False, default=1)
parser.add_argument("-prefix_", help="Add a prefix to a the passwords like [(fb, facebook), titktok, gmail, (twitter|xtwi), grok, openAI, ChatGpt...]", type=str, required=False, default="")
parser.add_argument("-passCheck", help="Check the complexity of the password", type=int, choices=[0, 1], required=False)
parser.add_argument("-useSecrets", help="Use secrets instead of random, this is ideal for randomness but could take time while generating passwords", choices=["Hex", "Choice", "UrlSafe", "n"], default="n")
"""
secrets.token_urlsafe
secrets.token_hex(
"""
args = parser.parse_args()
PassLength = args.plen
SaveToFile = args.sf
PassNumber = args.pNumber
UseAll = args.all_
eXD = args.eXD
eXS = args.eXS
eXP = args.eXP
prefix_ = args.prefix_
passCheck = args.passCheck
useSecrets = args.useSecrets
class Password:
    def __init__(self, *argsH):
        self.PassLength = PassLength
        self.SaveToFile = SaveToFile
        self.pNumber = PassNumber
        self.UseAll = UseAll
        self.eXD = eXD
        self.eXS = eXS
        self.eXP = eXP
        self.prefix_ = prefix_ 
        self.passCheck = passCheck
        self.useSecrets = useSecrets
        self.__Banner()
    def __Banner(self):
        Banner = figlet_format(
            "Password Generator",
            font="slant" 
            )
        print(f"[bold green] {Banner}[/ bold green]")
        print("[bold red]Treat your passwords as if they were your underwears[/ bold red]".center(60))
        console, table = Console(), Table(
            title="Information",
            style="bold green"
        )
        table.add_column("Length", highlight=True, justify="center", no_wrap=False)
        table.add_column("Number", highlight=True, justify="center", no_wrap=False)
        table.add_column("All", highlight=True, justify="center", no_wrap=False)
        table.add_column("Save", highlight=True, justify="center", no_wrap=False)
        table.add_column("eXD", highlight=True, justify="center", no_wrap=False)
        table.add_column("eXS", highlight=True, justify="center", no_wrap=False)
        table.add_column("eXP", highlight=True, justify="center", no_wrap=False)
        table.add_column("Prefix", highlight=True, justify="center", no_wrap=False)
        table.add_column("isCheck", highlight=True, justify="center", no_wrap=False)
        table.add_row(
            str(self.PassLength), 
            str(self.pNumber),
            "Y" if str(self.UseAll) == "1" else "N", 
            "Y" if self.SaveToFile == None else "N",
            "Y" if str(self.eXD) == "1" else "N", 
            "Y" if str(self.eXS) == "1" else "N", 
            "Y" if str(self.eXP) == "1" else "N",
            "Y" if str(self.prefix_) != "" else "N",
            "Y" if  str(self.passCheck) == "1" else "N"
            )
        console.print(table)
    def Core_(self):
        console, table = Console(), Table(title="Table of passwords")
        try:
            FileName = self.SaveToFile
            PassList = []
            if self.UseAll == 1:
                ALL = string.ascii_letters + string.digits + string.punctuation
            elif self.eXS == 0 and self.eXP == 0 and self.eXD == 0 and self.UseAll == 0:
                ALL = string.ascii_letters + string.digits + string.punctuation
            elif self.eXS == 1 and self.eXP == 1 and self.eXD == 1:
                ALL = string.ascii_letters + string.digits + string.punctuation
            elif self.eXS == 1 and self.eXD == 1 and self.eXP == 0:
                # exclude punctuation
                ALL = string.ascii_letters + string.digits
            elif self.eXS == 1 and self.eXP == 1 and self.eXD == 0:
                #exclude digits
                ALL = string.ascii_letters + string.punctuation
            elif self.eXS == 1 and self.eXD == 0 and self.eXP == 0:
                # include only ascii_letters
                ALL = string.ascii_letters
            elif self.eXS == 0 and self.eXP == 1 and self.eXD == 1:
                # exlude ascii_letters
                ALL = string.digits + string.punctuation 
            elif self.eXD == 1 and self.eXP == 0 and  self.eXS == 0:
                ALL = string.digits
                print("[bold yellow]You've excluded both ascii_letters, punctuations[/bold yellow]")
                print("[bold yellow]So to avoid raising a [red]'ValueError: Sample larger than population or is negative'[/red][/bold yellow]")
                print("[bold yellow]'self.PassLength' has been assigned a new value (10)[/bold yellow]")
                self.PassLength = len(string.digits)
            elif self.eXD == 0 and self.eXP == 1 and self.eXS == 0:
                ALL = string.punctuation 
                self.PassLength = len(string.punctuation) 
            self.prefix_ = self.prefix_+"_" if self.prefix_ != "" else ""
            for password in range(self.pNumber):#self.pNumber):
                if self.useSecrets == "UrlSafe":
                    #console.print("UrlSafe")
                    password = self.prefix_+"".join(secrets.token_urlsafe(self.PassLength))
                    PassList.append(password)
                elif self.useSecrets == "Hex":
                    #console.print("Hex")
                    password = self.prefix_+"".join(secrets.token_hex(self.PassLength))
                    PassList.append(password)
                elif self.useSecrets == "Choice":
                    #"console.print("Choice")
                    password = self.prefix_+''.join(secrets.choice(ALL) for x in range(self.PassLength))
                    PassList.append(password)
                else:
                    password = self.prefix_+''.join(random.sample(ALL, self.PassLength))
                    PassList.append(password)
            
            table.add_column("Index", style="bold magenta", no_wrap=False, justify="center", overflow="ellipsis")
            table.add_column("Password", style="bold cyan", no_wrap=False, justify="center", overflow="ellipsis")
            console.log("Starting ...")
            for index_, password in enumerate(PassList):
                table.add_row(str(index_), password)
            console.print(table)
            if self.SaveToFile != None:
                # save the output to a file name given by the user
                try:
                    file = open(self.SaveToFile, "w")
                    for LINES in PassList:
                        file.writelines(f"{LINES}\n")
                    console.print(f"[bold green] Output has been saved to {self.SaveToFile} [/ bold green]")
                except FileExistsError:
                    console.log("File alredy exists")
                    pass
                except Exception as FileCreationError:
                    console.log("LoginFileError: ")
                    console.print(f"[bold red] LoginFileError: {FileCreationError}")
            if self.passCheck == 1:
                # check the password is it strong or not
                #print("[bold greend][/bold green]")
                passCheck = input("Enter your password : ")
                PassList.insert(0, passCheck)
                def password_complexity(PassList):
                    for password in PassList:
                        score = 0
                        length_score = min(len(password) / 16, 1) * 40
                        uppercase_score = 15 if re.search(r"[A-Z]", password) else 0
                        lowercase_score = 15 if re.search(r"[a-z]", password) else 0
                        digit_score = 15 if re.search(r"\d", password) else 0
                        special_score = 15 if re.search(r"[!@#$%^&*()]", password) else 0
                        unique_chars = len(set(password))
                        unique_score = min(unique_chars / 10, 1) * 10 
                        penalty = 10 if re.search(r"(.)\1{2,}", password) else 0
                        score = length_score + uppercase_score + lowercase_score + digit_score + special_score + unique_score - penalty
                        print(password, min(max(score, 0), 100), "%")
                password_complexity(PassList)
        except Exception as Error:
            console.log("LogError")
            console.print("Error: ", Error)
Password().Core_()
    


