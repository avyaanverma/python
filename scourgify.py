import sys
import csv


def main():
    while True:
        try:
            if len(sys.argv) > 3:
                sys.exit("Too many command-line arguments")

            elif len(sys.argv) < 3:
                sys.exit("Not enough command-line arguments")

            elif not (sys.argv[1].endswith(".csv") or sys.argv[2].endswith(".csv") ):
                sys.exit("Not a Csv file")

            else:
                with open(sys.argv[1]) as file:
                    pass
                break

        except FileNotFoundError:
            sys.exit("Could not read csv")

    with open(sys.argv[1]) as before:

        before = csv.DictReader(before)

        with open(sys.argv[2], 'w') as after:
            headings  = ['first','last','house']

            after = csv.DictWriter(after,headings, delimiter = ",")
            after.writeheader()
            for line in before:
                name_read = line["name"]
                name_dict={}
                name_dict["last"],name_dict["first"] = name_read.split(",")
                name_dict["house"] = line["house"]
                name_dict["first"] = name_dict["first"].strip()
                print(name_dict)
                # line = str(name_dict["first"]+name_dict["second"]+line["house"])

                after.writerow(name_dict)









if __name__ == "__main__":
    main()