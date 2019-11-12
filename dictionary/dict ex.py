Dict={'name':['sohail','surasha','adishree','alisha'],'roll':[1,2,3,4] ,'marks':[55,65,75,85],'gender':['male','male','female','female']}
for i in range(len(Dict['roll'])):
    if Dict['gender'][i]=='male':
        print(Dict['marks'][i])
        print(Dict['name'][i])
        print(Dict['gender'][i])