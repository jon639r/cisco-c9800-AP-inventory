import logging
from c9800 import C9800
import argparse
import pandas as pd

## Prerequisites
## pip install pandas
## pip install openpyxl

## Set logging level and format
logging.basicConfig(level=logging.INFO, format="%(asctime)-15s (%(levelname)s) %(message)s")

## Parse command line arguments.
parser = argparse.ArgumentParser(description="Utility to build .xls and .csv AP inventory from C9800")
parser.add_argument('-user', help='c9800 username', required=True)
parser.add_argument('-password', help='c9800 password', required=True)
parser.add_argument('-wlc_ip', help='c9800 IP address', required=True)
args=parser.parse_args()

# Create an object of type C9800 and store it in the wlc variable
wlc = C9800(args.wlc_ip, args.user, args.password)

# Call our wlc object and ask for the list of joined APs
aps = wlc.get_joined_aps()

# Convert AP dictionnary into dataframe
df = pd.DataFrame(aps).T

# Convert into Excel and CSV
df.to_excel("aps.xlsx", index=False)
df.to_csv("aps.csv", index=False)

print("Done!")