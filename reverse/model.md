[TOC]

# Z3
```python
from z3 import *  // import z3 model 
s=Solver()  //create a solver named s
x=Int('x')  //define a valuable named x
s.add( )  //add some restrictions to s
s.check()  //check if the restrictions is right. if the return value is sat 
s.model()  //the return value is the answer
y=[IntVal(i)]  //give y a value that is I
flag=[Int('a%i' %i) for I in range()]  //give an array named flag some value-- a1,a2….. means to initialize an array  

How to print all eligble answer:
	while(s.check()==sat):
		print(s.model())
s.add(s.model[x]!=x)
```

# GMP
Gramma:
	mpz_t $int  // define a integer
	mpz_init($int)  //initalize a integer
	void mpz_set (mpz_t rop, mpz_t op) 
	void mpz_set_ui (mpz_t rop, unsigned long int op)
	void mpz_set_si (mpz_t rop, signed long int op)
	void mpz_set_d (mpz_t rop, double op)
	// rop = op1 + op2
	void mpz_add (mpz_t rop, mpz_t op1, mpz_t op2)
	void mpz_add_ui (mpz_t rop, mpz_t op1, unsigned long int op2)
	// rop = op1 - op2
	void mpz_sub (mpz_t rop, mpz_t op1, mpz_t op2)
	void mpz_sub_ui (mpz_t rop, mpz_t op1, unsigned long int op2)
	void mpz_ui_sub (mpz_t rop, unsigned long int op1, mpz_t op2)
	// rop = op1 * op2
	void mpz_mul (mpz_t rop, mpz_t op1, mpz_t op2)
	void mpz_mul_si (mpz_t rop, mpz_t op1, long int op2)
	void mpz_mul_ui (mpz_t rop, mpz_t op1, unsigned long int op2)
	// q = n / d + r
	void mpz_cdiv_q (mpz_t q, mpz_t n, mpz_t d)
	void mpz_cdiv_r (mpz_t r, mpz_t n, mpz_t d)
	void mpz_cdiv_qr (mpz_t q, mpz_t r, mpz_t n, mpz_t d)
	// rop = base ^ exp
	void mpz_pow_ui (mpz_t rop, mpz_t base, unsigned long int exp)
	void mpz_ui_pow_ui (mpz_t rop, unsigned long int base,
	unsigned long int exp)
	
	
