money_acct = 998
transfer = 2000

print("ต้องการโอนเงิน :",transfer)
while money_acct < (transfer + 15):
    print('กรุณาโอนเงินเข้าบัญชี เงินไม่พอโอน')
    deposit = int(input('ฝากเงิน : '))
    money_acct = money_acct + deposit
    print("ยอดเงินในบัญชี :",money_acct)
    print('---')

print("คุณมีเงินในบัญชี : ",money_acct)
print('โอนเงินได้เลย')
print('เหลือเงินในบัญชี',money_acct - (transfer+15))

