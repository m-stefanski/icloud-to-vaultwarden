import argparse
import csv
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert iCloud to Bitwarden/Vaultwarden CSV password file")
    parser.add_argument("-i", "--input", help="iCloud csv file: Safari -> Preferences -> Password -> (...) -> Save all", required=True)
    parser.add_argument("-o", "--output", help="Vaultwarden csv file", default="vaultwarden.csv")
    args = parser.parse_args()

    icloud_file = args.input
    vaultwarden_file = args.output

    icloud_headers_test = "Title,URL,Username,Password,Notes,OTPAuth"

    password_data = []
    with open(icloud_file, "r") as icloud_csv:
        icloud_reader = csv.reader(icloud_csv)
        # Verify headers
        icloud_headers = next(icloud_reader)
        if icloud_headers != icloud_headers_test.split(","):
            raise Exception("Invalid iCloud headers")

        for row in icloud_reader:
            password_row = []
            password_row.append(re.sub(r' (.*)', '', row[0])) # remove username from every description
            password_row.append(row[1]) # url unchanged
            password_row.append(row[2]) # username unchanged
            password_row.append(row[3]) # password unchanged
            password_row.append(row[4]) # notes unchanged
            password_row.append(row[5]) # otp unchanged
            password_data.append(password_row)

    # As documented in https://bitwarden.com/help/condition-bitwarden-import/ , section: "Condition a .csv"
    vaultwarden_headers = "collections,type,name,notes,fields,reprompt,login_uri,login_username,login_password,login_totp"
    
    with open(vaultwarden_file, "w") as vaultwarden_csv:
        vaultwarden_writer = csv.writer(vaultwarden_csv, delimiter=",")
        vaultwarden_writer.writerow(vaultwarden_headers.split(","))
        for password_row in password_data:
            row = []
            row.extend(["", ""]) # collections, type
            row.append(password_row[0]) #name
            row.append(password_row[4]) #notes
            row.extend(["", ""]) # fields, reprompt
            row.append(password_row[1]) #login_uri
            row.append(password_row[2]) #login_username
            row.append(password_row[3]) #login_password
            row.append(password_row[5]) #login_totp
            vaultwarden_writer.writerow(row)

