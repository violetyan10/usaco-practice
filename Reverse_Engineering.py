T=int(input())
for _ in range(T):
    input()
    N,M=list(map(int,input().split()))
    inputs=[]
    outputs=[]
    for _ in range(M):
        inp,out=input().split()
        inputs.append(inp)
        outputs.append(out)
    changed=True
    while changed:
        changed=False
        size=len(inputs)
        for i in range(N): #if statement spot condition
            for num in range(2): #0 or 1
                num=str(num)
                seen=["0","1"]
                # for input in inputs:
                #     if input[i]==num:
                #         seen.remove(outputs[i])
                for j in range(len(inputs)):
                    if inputs[j][i]==num:
                        if outputs[j] in seen:
                            seen.remove(outputs[j])
                if seen:
                    new_inputs=[]
                    new_outputs=[]
                    for j in range(len(inputs)):
                        if inputs[j][i]!=num:
                            new_inputs.append(inputs[j])
                            new_outputs.append(outputs[j])
                    if len(new_inputs)!=len(inputs):
                        changed=True
                    inputs=new_inputs
                    outputs=new_outputs
    if not inputs:
        print("OK")
    else:
        print("LIE")