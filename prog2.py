my_list=[1,2,3,4,4,4,5,1,3]
count_dict={}
for item in my_list:
 if item in count_dict:
     count_dict[item]+=1
 else:
     count_dict[item]=1
print("unique elements and their counts")
for key in count_dict:
    print(f"{key}:{count_dict[key]}")
     