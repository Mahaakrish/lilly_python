import modules.sal as s

ctc = int(input("Enter the ctc: "))

basic = s.bsal(ctc)
hra = s.hra(ctc)
da = s.da(ctc)
bonus = s.bonus(ctc)

print("The total salary the employee gets is",basic+hra+da+bonus)