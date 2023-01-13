import random
print(("Chọn các số từ 0 tới 100 , nếu bạn đoán đúng bạn sẽ thắng. "))
def thongtin_nhap(game_so): 
    thongtin_raw=input("Nhập vào số bạn chọn: ")
    if thongtin_raw.isnumeric():
    #đang kiểm tra giá trị nhập vào của người dùng (được lưu trong biến "thongtin_raw") có phải là số hay không. 
    #Phương thức "isnumeric()" được sử dụng để kiểm tra xem một chuỗi chỉ chứa các ký tự số (0-9) hay không. 
    #Nếu đầu vào là số, chương trình sẽ tiến hành bước tiếp theo, đó là kiểm tra xem số đó có nằm trong phạm vi hợp lệ (0-100) hay không. 
    #Nếu nhập không phải là số, chương trình sẽ hiển thị thông báo lỗi và yêu cầu người dùng nhập lại số hợp lệ.
        thongtin=int(thongtin_raw)
        if thongtin in game_so:
        #kiểm tra xem số mà người dùng nhập vào có nằm trong phạm vi hợp lệ hay không
        #Biến "game_so" là danh sách các số từ 0 đến 100 nên nếu thông tin nhập của người dùng (được lưu trong biến "thongtin") 
        #nằm trong danh sách đó thì có nghĩa là thông tin nhập hợp lệ và nằm trong khoảng giá trị hợp lệ.
            return thongtin
        else:
            print("Số bạn vừa nhập không hợp lệ , vui lòng nhập lại!")
            return -1
    else:
        print("Số bạn chọn không đúng , vui lòng nhập lại!")
        return -1
       
def dieukien(thongtin_nguoichoi,so_game):
    if thongtin_nguoichoi < so_game:
        print("Số của bạn bé hơn số của game đưa ra !")
    else:
        print("Số của bạn lớn hơn số của game đưa ra !")

def thongtin_game(con_so):
    game_so=[_ for _ in range(0, 101)]
    so_game=random.choice(game_so)
    
    a=0
    while a<con_so:
        thongtin_nguoichoi=thongtin_nhap(game_so)
        if thongtin_nguoichoi==-1:
            print("Thử lại 1 số khác: ")
        elif so_game==thongtin_nguoichoi:
            print(f"Hoan hô !!! Bạn đoán đúng rồi, bạn thật tài năng .Số đó chính là {thongtin_nguoichoi}")
            return
        else:
            print("Xin lỗi , bạn đoán sai bét rồi hihi ")
            dieukien(thongtin_nguoichoi,so_game)
            a=a+1
    else:
        print(f"Tất cả số bạn nhập bét , bạn đoán quá gà .Số của tôi đưa ra là {so_game}")

if __name__ == "__main__":
    luotchoi=50
    thongtin_game(luotchoi)
