import re
from typing import List


def numUniqueEmails(emails: List[str]) -> int:
    # result = set()
    # for e in emails:
    #     regex = '^([a-zA-Z0-9.]+)(\+?.*)?(@.*)$'
    #     # print(f'{re.match(regex, e).group(1)} : {re.match(regex, e).group(2)} : {re.match(regex, e).group(3)} ')
    #     front = re.match(regex, e).group(1).replace('.', '')
    #     back = re.match(regex, e).group(3)
    #     clean = front + back
    #     print(f'{e} : {clean}')
    #     result.add(clean)
    # return len(result)

    result = set()
    for e in emails:
        front, back = e.split('@')
        front = front.split('+')[0].replace('.', '')
        r = front + '@' + back
        print(f'{e} : {r}')
        result.add(front + '@' + back)
    return len(result)

if __name__ == '__main__':
    emails1 = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
    print(numUniqueEmails(emails1) == 2)

    emails2 = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
    print(numUniqueEmails(emails2) == 3)