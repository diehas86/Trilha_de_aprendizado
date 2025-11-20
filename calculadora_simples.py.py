while True:
   calculo = int(input ("DIGITE O PRIMEIRO NÚMERO: "))
   operadores = input("DIGITE A OPERAÇÃO MATEMÁTICA DESEJA FAZER  ")
   calculo2 = int(input ("DIGITE O SEGUNDO NÚMERO: "))
   if operadores == '+':
       print (f'O RESULTADO É : {calculo + calculo2}')
   elif operadores == '-':
       print (f'O RESULTADO É : {calculo - calculo2}')
   elif operadores == '*':                 
       print (f'O RESULTADO É : {calculo * calculo2}')
   elif operadores == '/':
       if calculo2 != 0 :        
         print (f'O RESULTADO É : {calculo / calculo2}')
       else:
        print ("NÃO É POSSÍVEL DIVIDIR POR ZERO")  
   else:
       print ("OPERADOR INVÁLIDO")   
       continue  

   sair= input("DESEJA SAIR? (S/N): ").upper()
   if sair == 'S':
         break          
   elif sair == 'N':
         continue   

      