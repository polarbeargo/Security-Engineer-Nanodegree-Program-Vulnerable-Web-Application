import sys, os, json, requests, argparse, base64
import hashlib

basedir = os.path.abspath(os.path.dirname(__file__))
data_file = os.path.join(basedir, 'test-password.txt')


def calculate(hash, hashType):
    results = None

    with open(data_file, 'r') as pwdFile:
        for line in pwdFile.readlines():
            md5hash = hashlib.md5(line.strip().encode()).hexdigest()
            sha1hash = hashlib.sha1(line.strip().encode()).hexdigest()
            sha2hash = hashlib.sha256(line.strip().encode()).hexdigest()
            sha512hash = hashlib.sha512(line.strip().encode()).hexdigest()
            
            if (hash == md5hash):
                hashType = 'md5'
                results = line.strip()
                break
            elif (hash == sha1hash):
                hashType = 'sha-1'
                results = line.strip()
                break
            elif (hash == sha2hash):
                hashType = 'sha-256'
                results = line.strip()
                break
            elif (hash == sha512hash):
                hashType = 'sha-512'
                results = line.strip()
                break

    print ("Result = ",results)
    print('Actual Hash Type should be = ', hashType)
    return 
        
if __name__ == "__main__":
    usage = "{0} [-h] HASH [-t TYPE] ".format(os.path.basename(__file__))
    parser = argparse.ArgumentParser(
        description="Hash lookup using hashes.org",
        usage=usage
    )
    parser.add_argument('hash', metavar="HASH", help='Hash that you want to lookup.')
    parser.add_argument("-t", "--type", type=str, help="Hash type to process.", required=True)
    args = parser.parse_args()
    print('---------------------------------------------')
    print("Hased value passed = ", args.hash)
    print("Hash type passed = ", args.type)
    calculate(args.hash, args.type)
    print('---------------------------------------------')