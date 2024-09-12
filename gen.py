import getopt, os, sys
from mnemonic import Mnemonic
from eth_account import Account

def usage():
    print("Usage: generator [-a] [-s 128|160|192|224|256] [-i] [INPUT]")

def help():
    print("TODO: Display help")


def main(argv):

    try:
        opts, args = getopt.getopt(argv, "has:i", ["help","address","strength=","input"])
    except getopt.GetoptError:
        usage()
        print("See --help for more info")
        sys.exit(1)

    generate = True
    create_address = False
    strength = 128
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            help()
            sys.exit(0)
        elif opt in ("-s", "--strength"):
            strength = int(arg)
        elif opt in ("-i", "--input"):
            generate = False
        elif opt in ("-a", "--address"):
            create_address = True

    words = ' '.join(args)

    mnemo = Mnemonic('english')

    if generate:
        words = mnemo.generate(strength)

    if not mnemo.check(words):
        print("Mnemonic not valid")
        sys.exit(1)

    entropy = mnemo.to_entropy(words)
    seed = mnemo.to_seed(words)

    print('Mnemonic:')
    print(f'\t {words}\n')
    print('Entropy:')
    print(f'\t {entropy.hex()}\n')
    print('Seed:')
    print(f'\t {seed.hex()}\n')

    ##address stuff:

    if create_address:

        print('Addresses:')
        # eth address
        Account.enable_unaudited_hdwallet_features()
        acct = Account.from_mnemonic(words)

        print(f'\tEth: {acct.address}')


    print("WRITE DOWN YOUR MNEMONIC. STORE IN A SAFE PLACE.")
    input("Press Enter to continue...")

    os.system('clear')


if __name__ == "__main__":
    main(sys.argv[1:])