
Vending Machine Take Home
====================

In this exercise you will build the brains of a vending machine.  It will accept money, make change, maintain
inventory, and dispense products.  All the things that you might expect a vending machine to accomplish.

The point of this exercise is to provide a larger than trivial exercise that can be used to practice TDD.  A significant
portion of the effort will be in determining what tests should be written and, more importantly, written next.

Features
========

Select Product
--------------

_As a vendor_  
_I want customers to select products_  
_So that I can give them products_  

There are three products: cola, chips, and candy.  When the respective button is pressed, the product is dispensed and the machine displays THANK YOU.  

Accept Coins
------------

_As a vendor_  
_I want a vending machine that accepts coins_  
_So that I can collect money from the customer_  

The vending machine will accept valid coins (nickels, dimes, and quarters) and reject invalid ones (pennies).  When a
valid coin is inserted the amount of the coin will be added to the current amount and the display will be updated.
When there are no coins inserted, the machine displays INSERT COIN.  Rejected coins are placed in the coin return.

NOTE: The temptation here will be to create Coin objects that know their value.  However, this is not how a real
  vending machine works.  Instead, it identifies coins by their weight and size and then assigns a value to what
  was inserted.  You will need to do something similar.  This can be simulated using strings, constants, enums,
  symbols, or something of that nature.

  Pay for Product
  --------------

  _As a vendor_  
  _I want customers to pay for products_  
  _So that I can make money from giving them products_  

  There are three products: cola for $1.00, chips for $0.50, and candy for $0.65.  When the respective button is pressed
  and enough money has been inserted, the product is dispensed and the machine displays THANK YOU.  If the display is
  checked again, it will display INSERT COIN and the current amount will be set to $0.00.  If there is not enough money
  inserted then the machine displays PRICE and the price of the item and subsequent checks of the display will display
  either INSERT COIN or the current amount as appropriate.

Make Change
-----------

_As a vendor_  
_I want customers to receive correct change_  
_So that they will use the vending machine again_  

When a product is selected that costs less than the amount of money in the machine, then the remaining amount is placed
in the coin return.
====================



 

## Steps to run

#### 1. Clone the repository using below URL
```bash
git clone https://github.com/RajeevRanjan25/vmth_test.git
```
#### 2. Go inside repository
```bash
cd vmth_test
```
#### 1.  (recommended) create a conda env
```bash
conda create -n vmth python=3.8
```
#### Activate env
```bash
conda activate vmth
```

In case you don't have conda installed in your system try with virtualenv
```bash
python3 -m pip install --user virtualenv
```
```bash
python3 -m venv vmth
```
#### Activate env
In macOS/Unix
```bash
source vmth/bin/activate
```

In windows
```bash
.\vmth\Scripts\activate
```

#### 2. install requirements for development
```bash
pip install -r requirements.txt
```

#### 3. run unit tests
```bash
python -m unittest
```

#### 4 Run the file with desired input
```bash
python3 main.py <product_name> <product_count> <coin_type> <no_of_coin>
```

#### 5 Assumptions
* Vendor machine only have 3 products in it.
    * cola
    * chips
    * candy

* Vendor machine have sufficient coins available to return.
* Vendor machine have sufficient quantities of products.