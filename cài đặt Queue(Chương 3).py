#tạo lớp Queue gồm các thuộc tính là : giới hạn số phần tử trong Queue và tạo Queue rỗng
class Queue:
    def __init__(self,full):
        self.danh_sach_full = full
        self.danh_sach = []
    # hàm trả về số phần tử trong Queue
    def length_queue(self):
        return self.danh_sach
    
    # hàm thêm phần tử mới vào vị trí cuối cùng queue
    def enqueue(self,value):
        # Kiểm tra nếu số phần tử trong Queue bé hơn số phần tử giới hạn trong Queue thì thêm phần tử mới vào Queue
        if len(self.danh_sach) < self.danh_sach_full:
            self.danh_sach.append(value)
            print(f"Đã thêm phần tử {value} vào Queue")
        # Ngược lại nếu số phần tử trong Queue bằng với số phần tử đã giới hạn trong Queue thì in ra Queue đã đầy
        else:
            print("Queue đã đầy")

    # hàm lấy phần tử đầu tiên của queue và xóa nó
    def dequeue(self):
        # Nếu số phần tử trong Queue lớn hơn 0 thì lấy phần tử ở đầu danh sách sử dụng hàm pop(0) và trả về giá trị đó.
        if len(self.danh_sach) > 0:
            return self.danh_sach.pop(0)
        # ngược lại nếu số phần tử bằng 0 thì in ra Queue rỗng và trả về None
        else:
            print("Queue rỗng")
            return None

    # Hàm in ra phần tử đầu tiên của Queue
    def Front(self):
        # Nếu số phần tử trong Queue lớn hơn 0 thì lấy giá trị đầu tiên trong Queue
        if len(self.danh_sach) > 0:
            print("Giá trị đầu tiên của Queue là: " ,self.danh_sach[0])
        # Ngược lại nếu bằng 0 thì in ra giá trị rỗng và trả về None
        else:
            print("Queue rỗng")
            return None

    # Hàm in ra phần tử cuối cùng của Queue
    def Rear(self):
        # Nếu số phần tử trong Queue lớn hơn 0 thì lấy giá trị cuối cùng trong Queue
        if len(self.danh_sach) > 0:
            print("Giá trị cuối cùng của Queue là: ",self.danh_sach[-1])
        else:
        # Ngược lại nếu bằng 0 thì in ra giá trị rỗng và trả về None
            print("Queue rỗng")
            return None

    # Hàm kiểm tra Queue đầy
    def is_full(self):
        return len(self.danh_sach) == self.danh_sach_full
    
    # Hàm kiểm tra Queue rỗng
    def is_empty(self):
        return self.danh_sach == 0
    
    # Hàm in ra các phần tử trong Queue
    def print_Queue(self):
        print("Các phần tử trong Queue: ")
        # Sử dụng vòng lặp để in ra từng giá trị trong Queue
        for values in self.danh_sach:
            print(values)

thuc_thi = Queue(int(input("Nhập số phần tử giới hạn trong Queue: ")))
# Thực thi thêm phần tử
while True:
    values = input("Nhập các giá trị cần thêm, cách nhau bởi dấu cách, hoặc gõ End để kết thúc: ")
    if values == "End":
        break
    for value in values.split():
        thuc_thi.enqueue(int(value))
# Queue sau khi thêm phần tử
print("****Sau khi thêm phần tử vào Queue****")
thuc_thi.print_Queue()
# in ra phần tử đang ở đầu của Queue
thuc_thi.Front()
# in ra phần tử ở cuối của Queue
thuc_thi.Rear()
# Thực thi lấy phần tử đầu tiên của Queue và xóa nó

thuc_thi.dequeue()
# Queue sau khi lấy phần tử đầu tiên và xóa nó
print("****Sau khi lấy phần tử đầu tiên và xóa nó****")
thuc_thi.print_Queue()

# kiểm tra xem Queue đầy hay chưa
print("Kiểm tra Queue đầy hay chưa: ",thuc_thi.is_full()) 
# Kiểm tra xem Queue có rỗng hay không
print("Kiểm tra Queue rỗng hay không: " ,thuc_thi.is_empty()) 






            
