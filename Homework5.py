immutable_var = 1, 2, "banana", True
print(immutable_var)
#immutable_var.remove(2) - данная команда не сработает, потому что
#в переменной применен кортеж с неизеняемыми данными.
#Для того, чтобы можно было изменить, нужно применить список.
#Например:
mutable_list = [1, 2, "banana", True]
mutable_list[0] = 1 * 2
mutable_list[2] = '2+2=4'
mutable_list[3] = (mutable_list[0] + mutable_list[1] == 4)
mutable_list.append(":)")
print(mutable_list)