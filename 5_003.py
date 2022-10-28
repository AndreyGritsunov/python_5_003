
def error_sim(text):
    n = ["a", "б", "в"]
    j = 0
    while j < len(n):
        i = 0
        while i < len(text):
            if text[i] == n[j]:
                return 1
            i = i + 1
        j = j + 1
    return 0

def main():
    f = ""
    m = input("Введите строку: ")
    l = m.split()
    i = 0
    while i < len(l):
        er_result = error_sim(l[i])

        if er_result == 0:
            f = f + " " + l[i]
        i = i + 1
    print(f)
    

    


main()