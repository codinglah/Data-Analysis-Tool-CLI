import pandas as pd
import matplotlib.pyplot as plt
import os
import traceback
def rinput():
    file = open("startup.txt", "r")
    cmd = input(file.read()).split(" ")
    while True:
        if cmd[0] == "about":
            file = open("about.txt", "r")
            cmd = input(file.read()).split(" ")
            continue
        elif cmd[0] == "quit":
            os._exit(0)
        elif cmd[0] == "credits":
            file = open("credits.txt", "r")
            cmd = input(file.read()).split(" ")
            continue
        elif cmd[0] == "license":
            file = open("LICENSE", "r")
            cmd = input(file.read()).split(" ")
            continue
        elif cmd[0] == "help":
            file = open("help.txt", "r")
            cmd = input(file.read()).split(" ")
            continue
        elif cmd[0] == "mean":
            herror = "False"
            # For *.csv files
            try:
                if cmd[1][-4:] == ".csv":
                    try:
                        if cmd[2] == "True":
                            df = pd.read_csv(cmd[1], header = 0, error_bad_lines = False, warn_bad_lines = False)
                        elif cmd[2] == "False":
                            df = pd.read_csv(cmd[1], header = None, error_bad_lines = False, warn_bad_lines = False)
                        else:
                            herror = "True"
                    except:
                        traceback.print_exc()
                    else:
                        if herror == "True":
                            file = open("herror.txt", "r")
                            cmd = input('"' + cmd[2] + file.read()).split(" ")
                            continue
                        else:
                            cmd = input(df.mean(), "\nDATool_CLI>").split(" ")
                            continue
            except:
                if len(cmd) < 3:
                    file = open("aerror.txt", "r")
                    cmd = input(file.read()).split(" ")
                    continue
            else:
                try: 
                    if cmd[2] == "True":
                        indic = "True"
                    elif cmd[2] == "False":
                        indic = "False"
                    else:
                        herror = "True"
                except:
                    pass
                else:
                    if herror == "False":
                        try:
                            if indic == "True":
                                df = pd.read_csv(cmd[1], header = 0, error_bad_lines = False, warn_bad_lines = False)
                            elif indic == "False":
                                df = pd.read_csv(cmd[1], header = None, error_bad_lines = False, warn_bad_lines = False)
                        except:
                            traceback.print_exc()
            # For *.xls and *.xlsx files
            try:
                if cmd[1][-4:] == ".xls" or cmd[1][-5:] == ".xlsx":
                    try:
                        if cmd[2] == "True":
                            df = pd.read_excel(cmd[1], header = 0, engine = "openpyxl")
                        elif cmd[2] == "False":
                            df = pd.read_excel(cmd[1], header = None, engine = "openpyxl")
                        else:
                            herror = "True"
                    except:
                        file = open("rerror.txt", "r")
                        cmd = input(file.read()).split(" ")
                        continue
                    else:
                        if herror == "True":
                            file = open("herror.txt", "r")
                            cmd = input('"' + cmd[2] + file.read()).split(" ")
                            continue
                        else:
                            cmd = input(df.mean(), "\nDATool_CLI>").split(" ")
                            continue
            except:
                if len(cmd) < 3:
                    file = open("aerror.txt", "r")
                    cmd = input(file.read()).split(" ")
                    continue
            else:
                try: 
                    if cmd[2] == "True":
                        indic = "True"
                    elif cmd[2] == "False":
                        indic = "True"
                    else:
                        herror = "True"
                except:
                    pass
                else:
                    if herror == "False":
                        try:
                            if indic == "True":
                                if not cmd[1][-4:] == ".csv":
                                    df = pd.read_excel(cmd[1], header = 0, engine = "openpyxl")
                                else:
                                    df = pd.read_csv(cmd[1], header = 0)
                            if indic == "False":
                                if not cmd[1][-4:] == ".csv":
                                    df = pd.read_excel(cmd[1], header = None, engine = "openpyxl")
                                else:
                                    df = pd.read_csv(cmd[1], header = None)
                            print(df.mean())
                            cmd = input("\nDATool_CLI>").split(" ")
                            continue
                        except:
                             file = open("rerror.txt", "r")
                             cmd = input(file.read()).split(" ")
                             continue   
            if not cmd[1][-4:] == ".csv" and not cmd[1][-4:] == ".xls" and not cmd[1][-5:] == ".xlsx":
                file = open("ferror.txt", "r")
                cmd = input(file.read()).split(" ")
                continue
        elif cmd[0] == "median":
            herror = "False"
            # For *.csv files
            try:
                if cmd[1][-4:] == ".csv":
                    try:
                        if cmd[2] == "True":
                            df = pd.read_csv(cmd[1], header = 0, error_bad_lines = False, warn_bad_lines = False)
                        elif cmd[2] == "False":
                            df = pd.read_csv(cmd[1], header = None, error_bad_lines = False, warn_bad_lines = False)
                        else:
                            herror = "True"
                    except:
                        file = open("rerror.txt", "r")
                        cmd = input(file.read()).split(" ")
                        continue
                    else:
                        if herror == "True":
                            file = open("herror.txt", "r")
                            cmd = input('"' + cmd[2] + file.read()).split(" ")
                            continue
                        else:
                            cmd = input(df.median(), "\nDATool_CLI>").split(" ")
                            continue
            except:
                if len(cmd) < 3:
                    file = open("aerror.txt", "r")
                    cmd = input(file.read()).split(" ")
                    continue
            else:
                try: 
                    if cmd[2] == "True":
                        indic = "True"
                    elif cmd[2] == "False":
                        indic = "False"
                    else:
                        herror = "True"
                except:
                    pass
                else:
                    if herror == "False":
                        try:
                            if indic == "True":
                                df = pd.read_csv(cmd[1], header = 0, error_bad_lines = False, warn_bad_lines = False)
                            elif indic == "False":
                                df = pd.read_csv(cmd[1], header = None, error_bad_lines = False, warn_bad_lines = False)
                            cmd = input(df.median(), "\nDATool_CLI>").split(" ")
                            continue
                        except:
                            file = open("foerror.txt", "r")
                            cmd = input(file.read()).split(" ")
                            continue
            # For *.xls and *.xlsx files
            try:
                if cmd[1][-4:] == ".xls" or cmd[1][-5:] == ".xlsx":
                    try:
                        if cmd[2] == "True":
                            df = pd.read_excel(cmd[1], header = 0)
                        elif cmd[2] == "False":
                            df = pd.read_excel(cmd[1], header = None)
                        else:
                            herror = "True"
                    except:
                        file = open("rerror.txt", "r")
                        cmd = input(file.read()).split(" ")
                        continue
                    else:
                        if herror == "True":
                            file = open("herror.txt", "r")
                            cmd = input('"' + cmd[2] + file.read()).split(" ")
                            continue
                        else:
                            cmd = input(df.median(), "\nDATool_CLI>").split(" ")
                            continue
            except:
                if len(cmd) < 3:
                    file = open("aerror.txt", "r")
                    cmd = input(file.read()).split(" ")
                    continue
            else:
                try: 
                    if cmd[2] == "True":
                        indic = "True"
                    elif cmd[2] == "False":
                        indic = "True"
                    else:
                        herror = "True"
                except:
                    pass
                else:
                    if herror == "False":
                        try:
                            if indic == "True":
                                df = pd.read_excel(cmd[1], header = 0)
                            if indic == "False":
                                df = pd.read_excel(cmd[1], header = None)
                            cmd = input(df.median(), "\nDATool_CLI>").split(" ")
                            continue
                        except:
                            file = open("foerror.txt", "r")
                            cmd = input(file.read()).split(" ")
                            continue
            if not cmd[1][-4:] == ".csv" and not cmd[1][-4:] == ".xls" and not cmd[1][-5:] == ".xlsx":
                file = open("ferror.txt", "r")
                cmd = input(file.read()).split(" ")
                continue
        elif cmd[0] == "mode":
            herror = "False"
            # For *.csv files
            try:
                if cmd[1][-4:] == ".csv":
                    try:
                        if cmd[2] == "True":
                            df = pd.read_csv(cmd[1], header = 0, error_bad_lines = False, warn_bad_lines = False)
                        elif cmd[2] == "False":
                            df = pd.read_csv(cmd[1], header = None, error_bad_lines = False, warn_bad_lines = False)
                        else:
                            herror = "True"
                    except:
                        file = open("rerror.txt", "r")
                        cmd = input(file.read()).split(" ")
                        continue
                    else:
                        if herror == "True":
                            file = open("herror.txt", "r")
                            cmd = input('"' + cmd[2] + file.read()).split(" ")
                            continue
                        else:
                            cmd = input(df.mode(), "\nDATool_CLI>").split(" ")
                            continue
            except:
                if len(cmd) < 3:
                    file = open("aerror.txt", "r")
                    cmd = input(file.read()).split(" ")
                    continue
            else:
                try: 
                    if cmd[2] == "True":
                        indic = "True"
                    elif cmd[2] == "False":
                        indic = "False"
                    else:
                        herror = "True"
                except:
                    pass
                else:
                    if herror == "False":
                        try:
                            if indic == "True":
                                df = pd.read_csv(cmd[1], header = 0, error_bad_lines = False, warn_bad_lines = False)
                            elif indic == "False":
                                df = pd.read_csv(cmd[1], header = None, error_bad_lines = False, warn_bad_lines = False)
                            cmd = input(df.mode(), "\nDATool_CLI>").split(" ")
                            continue
                        except:
                            file = open("foerror.txt", "r")
                            cmd = input(file.read()).split(" ")
                            continue
            # For *.xls and *.xlsx files
            try:
                if cmd[1][-4:] == ".xls" or cmd[1][-5:] == ".xlsx":
                    try:
                        if cmd[2] == "True":
                            df = pd.read_excel(cmd[1], header = 0)
                        elif cmd[2] == "False":
                            df = pd.read_excel(cmd[1], header = None)
                        else:
                            herror = "True"
                    except:
                        file = open("rerror.txt", "r")
                        cmd = input(file.read()).split(" ")
                        continue
                    else:
                        if herror == "True":
                            file = open("herror.txt", "r")
                            cmd = input('"' + cmd[2] + file.read()).split(" ")
                            continue
                        else:
                            cmd = input(df.mode(), "\nDATool_CLI>").split(" ")
                            continue
            except:
                if len(cmd) < 3:
                    file = open("aerror.txt", "r")
                    cmd = input(file.read()).split(" ")
                    continue
            else:
                try: 
                    if cmd[2] == "True":
                        indic = "True"
                    elif cmd[2] == "False":
                        indic = "True"
                    else:
                        herror = "True"
                except:
                    pass
                else:
                    if herror == "False":
                        try:
                            if indic == "True":
                                df = pd.read_excel(cmd[1], header = 0)
                            if indic == "False":
                                df = pd.read_excel(cmd[1], header = None)
                            cmd = input(df.mode(), "\nDATool_CLI>").split(" ")
                            continue
                        except:
                            file = open("foerror.txt", "r")
                            cmd = input(file.read()).split(" ")
                            continue
            if not cmd[1][-4:] == ".csv" and not cmd[1][-4:] == ".xls" and not cmd[1][-5:] == ".xlsx":
                file = open("ferror.txt", "r")
                cmd = input(file.read()).split(" ")
                continue
rinput()