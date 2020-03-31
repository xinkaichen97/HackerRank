result = [('{native-country=United-States,capital-gain=None}=>{capital-loss=None}', 0.9091117303508036), ('{capital-gain=None,capital-loss=None}=>{native-country=United-States}', 0.9471465500099423), ('{native-country=United-States,capital-loss=None}=>{capital-gain=None}', 0.909875835721108)]
result = sorted(result, key=lambda x: x[1], reverse=True)
print(result)
for rule, confid in result:
    print(rule)