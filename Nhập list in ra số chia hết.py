a = int (input ('Nhập số chữ số trong danh sách '))
b = int (input ('Nhập ước cần tìm '))


lst = [int(input(f'Nhập số thứ {i+1} : ')) for i in range (a)]
#Do vòng lặp for ở trên nên i tự động gán từ 0 đến a-1
#Vì vậy ta sử dụng i + 1 để print ra chữ số 1 đầu tiên chứ không phải chữ số 0
newlist = []

for i in lst:
    if i % b == 0:
        newlist.append(i)

print (newlist)

