UNDERSTANDING THE ABS () METHOD IN PYTHON AND ITS APPLICATIONS

In python we can encounter complex numbers such as z = 3 + 2j

             3   =  real number
             2j  =  imaginary number 

j in python simply a special number that represents the imaginary unit in which it translates to a complex number (2j) in this case. However, in fields of physics and engineering, j is represented as i , we use j in python since many programmers use it when iterating for loops or even declaring varibles ,hence ,to avoid confusion python uses j since it's not regulary used to declare varibles.

                            

                                  
                         (in Math/Physics/Engineering)


How to solve it : 

     j is simply originated from this:
           
Normal negative real/normal numbers cannot give you a square root hence its not a real number:

           √ –1  is not real number hence it becomes negative 
                 real number which now is expressed as
                 Imaginary number    

Hence mathematicians  invented the imaginary number using i (or j in python)
      
          √ –1 = j

So if you print in python  :

          j = 1j

          print( j  *  j ) 

          Result : (-1+0j)
      
      Why is this : 
           
           j × j = j²
           
           While : 
         
           J² = – 1

      Example : 
           
           No real number works, because:
                
                √– 9 ?
3 × 3 = 9 


(−3) × (−3) = 9 


      Neither gives –9 hence they introduced the j (in python)
      So result should be : 3j

  Run this in python3 :
  import cmath
  print(cmath.sqrt(-9))  # (0+3j)
  While 
  Run this in python3 :
  j = 3j
  print( j * j )       # (-9+0j)
  this means
Real part = –9


Imaginary part = 0


That is just the same as the real number –9.
Python is showing it in complex form, but it’s not imaginary — it’s just a negative real number written inside the complex system.
Where abs() comes into the picture : 
abs() simply means absolute value hence or “How far is this number from zero?”
If the number is positive → abs() gives it back.


If the number is negative → abs() flips it to positive.
Run this in python3 : 
   number = -9
   print(abs(number ** 0.5))  # 3.0

Now why should i use abs() 
Use abs() in instances where you care about magnitude and not the direction in this case negative values
Example : 
Run this in python3 : 
   #1
   number = -9
   print(abs(number ** 0.5))  # 3.0
   #2
   steps = -120
   print(abs(steps))  # 120 (distance is always positive)
   #3
   ## our example
   z = 3 + 2j
   print(abs(z)) # 3.6
   # compare 
   print(z)      #(3+2j)
(ss3+2j)

(3+2j)




   



  

  



           
           














      
     


