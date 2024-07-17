try:
    a = input('Введите оценки Aaron через пробел: ').split()
    b = input('Введите оценки Bilbo через пробел: ').split()
    j = input('Введите оценки Johnny через пробел: ').split()
    k = input('Введите оценки Khendrik через пробел: ').split()
    s = input('Введите оценки Steve через пробел: ').split()
    al = list(map(int, a))
    bl = list(map(int, b))
    jl = list(map(int, j))
    kl = list(map(int, k))
    sl = list(map(int, s))
    A = (sum(al) / len(al))
    B = (sum(bl) / len(bl))
    J = (sum(jl) / len(jl))
    K = (sum(kl) / len(kl))
    S = (sum(sl) / len(sl))
    grades = [A, B, J, K, S]
    students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
    students_list = list(students)
    students_list.sort()
    As = students_list[0]
    Bs = students_list[1]
    Js = students_list[2]
    Ks = students_list[3]
    Ss = students_list[4]
    Dict = {As: A, Bs: B, Js: J, Ks: K, Ss: S}
    print(Dict)

except ValueError:
    print("Неверный ввод, укажите по примеру: 1 2 3 4 5")