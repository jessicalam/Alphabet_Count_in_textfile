''' This python file goes through a file and then iterates through each word and
counts how many letters of each letter in the alphabet are in the file. This output
an x for every letter there is for that letter in the alphabet.
Written by Jessica Lam & Kevin Kye for CSE 201 HW4 Problem 1 Due on October 12, 2017
'''

file_str=input("Open what file: ")
#file_str="words.txt" #testcase
try:

    input_file=open(file_str) #potential user error.

    #initiated the values, made them this way so it was easier to keep track of.
    a_count=b_count=c_count=d_count=e_count=0
    f_count=g_count=h_count=i_count=j_count=0
    k_count=l_count=m_count=n_count=o_count=0
    p_count=q_count=r_count=s_count=t_count=0
    u_count=v_count=w_count=x_count=y_count=z_count=0

    for line in input_file: #goes through each line in the file
        line=line.lower() #made it lowercase
        for word in line: #goes through each letter in the line, counts up how many of each letter.
            if word == 'a':
                a_count=a_count+1
            if word == 'b':
                b_count=b_count+1
            if word == 'c':
                c_count=c_count+1
            if word == 'd':
                d_count=d_count+1
            if word == 'e':
                e_count=e_count+1
            if word == 'f':
                f_count=f_count+1
            if word == 'g':
                g_count=g_count+1
            if word == 'h':
                h_count=h_count+1
            if word == 'i':
                i_count=i_count+1
            if word == 'j':
                j_count=j_count+1
            if word == 'k':
                k_count=k_count+1
            if word == 'l':
                l_count=l_count+1
            if word == 'm':
                m_count=m_count+1
            if word == 'n':
                n_count=n_count+1
            if word == 'o':
                o_count=o_count+1
            if word == 'p':
                p_count=p_count+1
            if word == 'q':
                q_count=q_count+1
            if word == 'r':
                r_count=r_count+1
            if word == 's':
                s_count=s_count+1
            if word == 't':
                t_count=t_count+1
            if word == 'u':
                u_count=u_count+1
            if word == 'v':
                v_count=v_count+1
            if word == 'w':
                w_count=w_count+1
            if word == 'x':
                x_count=x_count+1
            if word == 'y':
                y_count=y_count+1
            if word == 'z':
                z_count=z_count+1

    print("a: ",a_count*"x")
    print("b: ",b_count*"x")
    print("c: ",c_count*"x")
    print("d: ",d_count*"x")
    print("e: ",e_count*"x")
    print("f: ",f_count*"x")
    print("g: ",g_count*"x")
    print("h: ",h_count*"x")
    print("i: ",i_count*"x")
    print("j: ",j_count*"x")
    print("k: ",k_count*"x")
    print("l: ",l_count*"x")
    print("m: ",m_count*"x")
    print("n: ",n_count*"x")
    print("o: ",o_count*"x")
    print("p: ",p_count*"x")
    print("q: ",q_count*"x")
    print("r: ",r_count*"x")
    print("s: ",s_count*"x")
    print("t: ",t_count*"x")
    print("u: ",u_count*"x")
    print("v: ",v_count*"x")
    print("w: ",w_count*"x")
    print("x: ",x_count*"x")
    print("y: ",y_count*"x")
    print("z: ",z_count*"x")

    input_file.close() #important to always close files

except IOError:
    print("The file", file_str, "does not exist.")


'''
#### Test Cases
print("a: ",a_count)
print("b: ",b_count)
print("c: ",c_count)
print("d: ",d_count)
print("e: ",e_count)
print("f: ",f_count)
print("g: ",g_count)
print("h: ",h_count)
print("i: ",i_count)
print("j: ",j_count)
print("k: ",k_count)
print("l: ",l_count)
print("m: ",m_count)
print("n: ",n_count)
print("o: ",o_count)
print("p: ",p_count)
print("q: ",q_count)
print("r: ",r_count)
print("s: ",s_count)
print("t: ",t_count)
print("u: ",u_count)
print("v: ",v_count)
print("w: ",w_count)
print("x: ",x_count)
print("y: ",y_count)
print("z: ",z_count)
'''


