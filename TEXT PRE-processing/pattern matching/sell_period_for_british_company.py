#check quaterly sell of british company
import re
text = '''
Tesla's gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
BMW's gross cost of operating vehicles in FY2021 S1 was $8 billion.
'''
pattern=r'FY(\d{4} (?:Q[1-4]|S[1-2]))'
matches=re.findall(pattern,text)
print(matches)

p=r'\$(\d\.\d+) billion'
money=re.findall(p,text)
print("amount:",money)
