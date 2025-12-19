# quest_stack_q1 Build an Array With Stack Operations
def buildArray(target, n) :  
    stream = 1
    output = []
    built_list = []
    # initial
    for i in range(0,len(target)):
        while target[i]!= stream:
            print(f"target[i] = {target[i]} and stream = {stream}")
            output.append("Push")
            output.append("Pop")
            stream+=1
        built_list.append(stream)
        output.append("Push")
        stream+=1

    return output


target = [1,3]
n = 3
result = buildArray(target,n)
print(result)