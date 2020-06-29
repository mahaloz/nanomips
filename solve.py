def valid_chars(string):
    valid = bytearray('acdeqswxz'.encode('utf-8')) 
    for c in string:
        if c not in valid:
            return False
    return True
   
def check1(data_sect):
    print("========== CHECK 1 ==========") 
    indx = list() 
    valid = True 
    mid = 0x54
    for i in range(9):
        storage = bytearray()
        for j in range(9):
            a3 = i << 3
            a2 = a3 + mid
            a3 = a2 + j

            first_data = data_sect[a3]

            # start of data
            a3 = 0
            a3 += first_data
            second_data = data_sect[a3]

            storage.append(second_data)


        print(storage)
        valid &= valid_chars(storage) 
        
    return valid

def check2(data_sect): 
    print("========== CHECK 2 ==========") 
    valid = True  
    for i in range(9):
        storage = bytearray()
        indexs = list() 
        for j in range(9):
            a3 = j << 3
            a2 = a3 + j
            a2 += i
            # start of data
            a3 = 0
            a3 += a2
            first_data = data_sect[a3]
            # second data
            storage.append(first_data)
            indexs.append(a3) 
        print(indexs) 
        valid &= valid_chars(storage) 
    
    return valid 

def check3(data_sect): 
    print("========== CHECK 3 ==========") 
    valid = True 
    for i in range(9):
        storage = bytearray()
        indexs = list() 
        for j in range(9):
            a3 = i << 3
            a2 = a3 + i
            a2 += j
            # data start
            a3 = 0
            a3 += a2
            data = data_sect[a3] 
            indexs.append(a3) 
            
            storage.append(data)
        print(indexs)
        valid &= valid_chars(storage)

    return valid 


def fill_data_sect(input_flag,data_sect):
    input_data = input_flag[5:-1] 
    assert len(input_data) == 56
    
    for c in input_data: 
        pos = 0
        while (pos < len(data_sect)-1) and (data_sect[pos] != 0):
            pos += 1
        data_sect[pos] = c 

def check_flag(data_sect):
    correct = True
    correct &= check1(data_sect) 
    correct &= check2(data_sect) 
    correct &= check3(data_sect) 
    if correct:
        print("Right") 
    else:
        print("Wrong") 

def main(): 
    with open("babymips","rb") as fp:
        bin_data = fp.read()
    data_sect = bytearray(bin_data[0x010000:0x010000+0x0000a5])
    ro_data = bin_data[0x798:0x000798+0x7e] 
    input_flag = bytearray("flag{accdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd}".encode('utf-8'))
    input_flag = bytearray("flag{xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx}".encode('utf-8'))
    #bytearray(input("Input the flag: ").encode('utf-8')) 

    # program starts here 
    fill_data_sect(input_flag,data_sect)
    print(data_sect) 
    check_flag(data_sect) 

    
    
if __name__ == "__main__":
    main() 
