report = {'deep':7.8, 'sammy' :7.8, 'dan':9.5, 'dan':8.5}

print (report)
print(type(report))

print(report ['sammy'])
#print(report[0])
#KeyError: 0

report ['sumit'] = 8.11
print(report)

report ['sammy'] = 7.25
print(report)

del report['sammy']
print(report)

print(report. keys())
print(report.values())
print(report. items())