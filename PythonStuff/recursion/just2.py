let=['a','b','c']
lan=""
i=0
while let:
    lan+=let[i]
    i=i+1
    let=let[i:]
print(lan)
