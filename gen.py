import getopt, os, sys
from mnemonic import Mnemonic
from eth_account import Account

def usage():
    print("Usage: python gen.py [-a] [-s 128|160|192|224|256] [-i] [INPUT]")
    print("For more info, see python gen.py --help")

def help():
    print("This is a simple script to generate mnemonic phrases and ETH address. By default,")
    print("the script will generate a random 128 bit mnemonic phrase that can be used to")
    print("generate wallet address on several networks.\n")
    print("Simple usage example:")
    print("\tpython gen.py")
    print("> Mnemonic: eager supply congress gaze daughter mix issue vacant practice ivory treat vibrant\n")
    print("Example address output:")
    print("\tpython gen.py -a")
    print("> Mnemonic   : pistol three track razor chicken topple globe sustain blade dignity taxi potato")
    print("> ETH Address: 0x6e30Fd6b04cdEa38Ef3ee8a8F7247C07f1e6f873\n")
    print("The script can also generate an address from an existing mnemonic by specifiying the -i flag")
    print("followed by the mnemonic as follows:")
    print("\t python gen.py -a -i future crunch diamond near dry soul tomorrow under talent ready victory grit")
    print("> Mnemonic   : future crunch diamond near dry soul tomorrow under talent ready victory grit")
    print("> ETH Address: 0x68a0d7Ffba34A54A272C6E09cf54A8A0622C0368\n")
    print("Strength of the mnemonic can also be set with the -s flag as follows. By default this is set to 128 bits.")
    print("\t python gen.py -s 256")
    print("> voyage upgrade story hundred toe slice hurt mandate cannon wide wool help moon custom speed glass lemon wear pond sea canvas income blanket wisdom")



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

    print(f'Mnemonic   : {words}')
    # print(f'Entropy    : {entropy.hex()}')
    # print(f'Seed       : {seed.hex()}')

    if create_address:

        # eth address
        Account.enable_unaudited_hdwallet_features()
        acct = Account.from_mnemonic(words)

        print(f'ETH Address: {acct.address}')


    print("WRITE DOWN YOUR MNEMONIC. STORE IN A SAFE PLACE.")
    input("Press Enter to continue...")

    os.system('clear')


if __name__ == "__main__":
    main(sys.argv[1:])