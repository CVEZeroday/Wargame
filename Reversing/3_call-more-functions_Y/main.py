count = 0
tmp = 0
tmp1 = 0
tmp2 = 0
arr = [0 for i in range(64)]
res = [0 for i in range(64)]

def argument_to_arr_count_cpp(arg):
    global count, tmp, tmp1, tmp2
    if tmp1 == 0:
        arr[count] = arg
        count += 1
    else:
        tmp2 = arg
        count += 1

def arr_count_minus1_to_s_arr_count_minus1():
    global count, tmp, tmp1
    tmp = arr[count-1]

def check_arr_count_minus1_eq_to_arr_count_minus2_cmm():
    global count, tmp, tmp1, tmp2
    if tmp1 != 0:
        b = tmp2
        for i in range(tmp1):
            a = arr[count-2+i]
            arr[count-2+i] = b
            b ^= a

        arr[count-1] = arr[count-2]
        res[tmp] = b

        tmp1 = 0
    else:
        res[tmp] = arr[count-1]
        arr[count-2] = arr[count-1]
    count -= 1

def xor_count_minus2_with_count_minus1_cmm():
    global count, tmp, tmp1
    count -= 1
    tmp1 += 1

argument_to_arr_count_cpp(63);                
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(51);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();
argument_to_arr_count_cpp(62);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(4);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

print(arr)
print(res)

argument_to_arr_count_cpp(61);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(101);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();
argument_to_arr_count_cpp(60);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(80);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();
argument_to_arr_count_cpp(59);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(102);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();
argument_to_arr_count_cpp(58);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(82);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();
argument_to_arr_count_cpp(57);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(52);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();
argument_to_arr_count_cpp(56);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(83);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(55);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(50);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(54);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(87);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(53);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(52);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(52);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(91);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(51);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(57);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(50);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(91);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(49);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(51);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(48);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(4);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(47);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(102);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(46);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(7);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(45);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(56);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(44);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(10);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(43);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(99);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(42);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(7);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(41);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(52);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(40);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(90);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(39);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(53);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(38);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(4);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(37);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(102);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(36);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(86);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(35);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(99);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(34);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(6);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(33);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(50);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(32);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(93);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(31);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(99);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(30);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(6);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(29);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(52);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(28);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(5);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(27);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(99);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(26);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(2);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(25);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(97);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(24);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(81);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(23);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(97);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(22);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(80);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(21);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(49);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(20);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(88);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(19);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(98);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(18);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(84);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(17);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(51);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(16);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(88);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(15);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(53);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(14);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(7);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(13);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(48);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(12);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(85);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(11);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(48);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(10);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(82);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(9);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(100);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(8);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(1);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(7);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(52);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(6);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(3);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(5);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(100);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(4);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(83);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(3);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(100);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(2);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(0);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(1);
arr_count_minus1_to_s_arr_count_minus1();
argument_to_arr_count_cpp(101);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

argument_to_arr_count_cpp(0);
arr_count_minus1_to_s_arr_count_minus1();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
xor_count_minus2_with_count_minus1_cmm();
argument_to_arr_count_cpp(0);
check_arr_count_minus1_eq_to_arr_count_minus2_cmm();

print(arr)
print(res)
ascii = res
ascii_char = [chr(i) for i in ascii]
print(ascii_char)

s = ""
for i in ascii_char:
    s += i

print(s)
