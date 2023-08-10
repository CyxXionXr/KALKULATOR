#---[MODULE]---#
import os
from rich import print as prints
from rich.panel import Panel

#---[THEMA]---#
p = '\x1b[1;97m'# WARNA-PUTIH
m = '\x1b[1;91m' # WARNA-MERAH
k = '\x1b[1;93m' # WARNA-KUJING
h = '\x1b[1;92m' # WARNA-HIJAU
x = '\33[m' # DEFAULT

#---[BACER]---#
def clear():
    os.system('clear')
def back():
    menu()
    
#---[BANNER]---#
class banner():
	def __init__(self):
		self.banner()
		
	def banner(self):
		os.system('clear')
		prints(Panel(f'''\t[green]
╦╔═╔═╗╦  ╦╔═╦ ╦╦  ╔═╗╔╦╗╔═╗╦═╗
╠╩╗╠═╣║  ╠╩╗║ ║║  ╠═╣ ║ ║ ║╠╦╝
╩ ╩╩ ╩╩═╝╩ ╩╚═╝╩═╝╩ ╩ ╩ ╚═╝╩╚═
    [white]Coded By [yellow]CYXIEON-XD
''',width=50,padding=(0,7),title=f"[red]Version 2.1",style=f"red"))
		
#---[MENU]---#
class menu():
	def __init__(self):
		self.menu()
		
	def menu(self):
		banner()
		while True:
			prints(Panel(f"[white]Pilih Operasi Matematika Di Bawah Ini",width=50,padding=(0,5),style=f"red"))
			prints(Panel(f"[yellow][[green]•[yellow]][white] Operasi Penjumlahan [[yellow] Kode : [green]+ [white]]\n[yellow][[green]•[yellow]][white] Operasi Pengurangan [[yellow] Kode : [green]- [white]]\n[yellow][[green]•[yellow]][white] Operasi Pembagian   [[yellow] Kode : [green]/ [white]]  \n[yellow][[green]•[yellow]][white] Operasi Perkalian   [[yellow] Kode : [green]* [white]]",width=50,padding=(0,3),style=f"red"))
			operasi = input(f'%s[%s•%s]%s Masukan Kode : '%(p,m,p,h))
#--->			
			prints(Panel(f"[yellow] Masukan Angkan Ke 1",width=50,padding=(0,10),style=f"red"))
			bilangan_1 = int(input(f'%s[%s•%s]%s Masukan : '%(p,m,p,h)))
#--->			
			prints(Panel(f"[yellow] Masukan Angkan Ke 2",width=50,padding=(0,10),style=f"red"))
			bilangan_2 = int(input(f'%s[%s•%s]%s Masukan : '%(p,m,p,h)))
#--->						
			if operasi == "+":
			    print(f"%s[%s•%s]%s Hasil dari"%(p,m,p,h),bilangan_1,"+",bilangan_2, "=",bilangan_1+bilangan_2)
#--->			    
			elif operasi == "-":
			    print(f"%s[%s•%s]%s Hasil dari"%(p,m,p,h),bilangan_1,"-",bilangan_2, "=",bilangan_1-bilangan_2)
#--->			    
			elif operasi == "/":
			    print(f"%s[%s•%s]%s Hasil dari"%(p,m,p,h),bilangan_1,"/",bilangan_2, "=",bilangan_1/bilangan_2)
#--->			    
			elif operasi == "*":
			    print(f"%s[%s•%s]%s Hasil dari"%(p,m,p,h),bilangan_1,"*",bilangan_2, "=",bilangan_1-bilangan_2)	
			    		    
#---[SYSTEM]---#	
if __name__=='__main__':
	menu()
