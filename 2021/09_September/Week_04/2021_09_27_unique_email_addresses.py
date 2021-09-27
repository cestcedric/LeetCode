class Solution:
    # O(n * m) time: split in O(m), m = average address length
    # O(n * m) space: unique set with at most n addresses of length m
    def numUniqueEmails(self, emails: list) -> int:
        unique = set()

        for email in emails:
            local, domain = email.split('@')
            local = local.split('+')[0].replace('.', '')

            unique.add('{}@{}'.format(local, domain))

        return len(unique)



testcases = [
    (['test.email+alex@leetcode.com','test.e.mail+bob.cathy@leetcode.com','testemail+david@lee.tcode.com'], 2),
    (['a@leetcode.com','b@leetcode.com','c@leetcode.com'], 3)
]

for i, (emails, target) in enumerate(testcases):
    output = Solution().numUniqueEmails(emails)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')