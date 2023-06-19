import operator

def person_lister(f):
    def inner(people):
        # complete the function
        # people is a 2d list 
        # people.sort(key=operator.itemgetter(0))
        i = 0
        for rows in people:
                list[0] = ("Mr. " if rows[3] == "M" else "Ms. ") + rows[0] + " " + rows[1]
        return list
    return inner
# name format is only returning the mr and ms

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')