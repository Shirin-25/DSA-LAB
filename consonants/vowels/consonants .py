def cou(s):
    vowels="aeiouAEIOU"
    v_lst=[]
    c_lst=[]
    for i in s:
      if i.isalpha():
        if i in vowels:
            v_lst.append(i)
        else:
            c_lst.append(i)
    print(f"the vowels are{v_lst}")
    print(f"\n the count is{len(v_lst)}")
    print(f"the consonant are{c_lst}")
    print(f"\n the count is{len(c_lst)}")
    
a=input("enter a string")
cou(a)
