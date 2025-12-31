# 📘 Transaction Rules – Accounting Equation Engine

This file defines accounting transaction rules using keywords and accounting logic.
The system matches user questions with keywords and applies the corresponding rule.

---

## FORMAT
- **Keywords**: words used to detect transaction
- **Transaction Type**
- **Accounting Effect**
- **Accounting Equation Impact**
- **Journal Entry Template**

---

## 1. Capital Introduced
**Keywords:** capital, introduced, owner invested  
**Effect:** Cash ↑, Capital ↑  
**Equation:** Assets ↑ = Capital ↑  
**Journal:**  
Cash A/c Dr  
To Capital A/c  

---

## 2. Cash Withdrawn (Drawings)
**Keywords:** withdrawn, drawings, personal use  
**Effect:** Cash ↓, Capital ↓  
**Equation:** Assets ↓ = Capital ↓  
**Journal:**  
Drawings A/c Dr  
To Cash A/c  

---

## 3. Cash Purchase of Goods
**Keywords:** goods purchased, cash purchase  
**Effect:** Inventory ↑, Cash ↓  
**Equation:** Assets ↑ = Assets ↓  
**Journal:**  
Purchases A/c Dr  
To Cash A/c  

---

## 4. Credit Purchase of Goods
**Keywords:** credit purchase, goods on credit  
**Effect:** Inventory ↑, Creditors ↑  
**Equation:** Assets ↑ = Liabilities ↑  
**Journal:**  
Purchases A/c Dr  
To Creditors A/c  

---

## 5. Cash Sales
**Keywords:** cash sales, sold for cash  
**Effect:** Cash ↑, Capital ↑  
**Equation:** Assets ↑ = Capital ↑  
**Journal:**  
Cash A/c Dr  
To Sales A/c  

---

## 6. Credit Sales
**Keywords:** credit sales, sold on credit  
**Effect:** Debtors ↑, Capital ↑  
**Equation:** Assets ↑ = Capital ↑  
**Journal:**  
Debtors A/c Dr  
To Sales A/c  

---

## 7. Rent Paid
**Keywords:** rent paid  
**Effect:** Cash ↓, Capital ↓  
**Equation:** Assets ↓ = Capital ↓  
**Journal:**  
Rent A/c Dr  
To Cash A/c  

---

## 8. Salary Paid
**Keywords:** salary paid, wages paid  
**Effect:** Cash ↓, Capital ↓  
**Equation:** Assets ↓ = Capital ↓  
**Journal:**  
Salary A/c Dr  
To Cash A/c  

---

## 9. Electricity Bill Paid
**Keywords:** electricity, power bill  
**Effect:** Cash ↓, Capital ↓  
**Equation:** Assets ↓ = Capital ↓  
**Journal:**  
Electricity A/c Dr  
To Cash A/c  

---

## 10. Water Bill Paid
**Keywords:** water bill  
**Effect:** Cash ↓, Capital ↓  
**Equation:** Assets ↓ = Capital ↓  
**Journal:**  
Water Charges A/c Dr  
To Cash A/c  

---

## 11. Telephone Bill Paid
**Keywords:** telephone bill, phone expense  
**Effect:** Cash ↓, Capital ↓  
**Journal:**  
Telephone A/c Dr  
To Cash A/c  

---

## 12. Internet Charges Paid
**Keywords:** internet, broadband  
**Effect:** Cash ↓, Capital ↓  
**Journal:**  
Internet Charges A/c Dr  
To Cash A/c  

---

## 13. Purchase of Furniture (Cash)
**Keywords:** furniture purchased  
**Effect:** Furniture ↑, Cash ↓  
**Equation:** Assets ↑ = Assets ↓  
**Journal:**  
Furniture A/c Dr  
To Cash A/c  

---

## 14. Purchase of Furniture (Credit)
**Keywords:** furniture on credit  
**Effect:** Furniture ↑, Creditors ↑  
**Journal:**  
Furniture A/c Dr  
To Creditors A/c  

---

## 15. Purchase of Machinery
**Keywords:** machinery purchased  
**Effect:** Machinery ↑, Cash ↓  
**Journal:**  
Machinery A/c Dr  
To Cash A/c  

---

## 16. Purchase of Building
**Keywords:** building purchased  
**Effect:** Building ↑, Cash ↓  
**Journal:**  
Building A/c Dr  
To Cash A/c  

---

## 17. Purchase of Land
**Keywords:** land purchased  
**Effect:** Land ↑, Cash ↓  
**Journal:**  
Land A/c Dr  
To Cash A/c  

---

## 18. Purchase of Land and Building
**Keywords:** land and building purchased  
**Effect:** Land ↑, Building ↑, Cash ↓  
**Journal:**  
Land & Building A/c Dr  
To Cash A/c  

---

## 19. Loan Taken
**Keywords:** loan taken, borrowed  
**Effect:** Cash ↑, Loan ↑  
**Equation:** Assets ↑ = Liabilities ↑  
**Journal:**  
Cash A/c Dr  
To Loan A/c  

---

## 20. Loan Repaid
**Keywords:** loan repaid  
**Effect:** Cash ↓, Loan ↓  
**Journal:**  
Loan A/c Dr  
To Cash A/c  

---

## 21. Interest Paid
**Keywords:** interest paid  
**Effect:** Cash ↓, Capital ↓  
**Journal:**  
Interest A/c Dr  
To Cash A/c  

---

## 22. Commission Received
**Keywords:** commission received  
**Effect:** Cash ↑, Capital ↑  
**Journal:**  
Cash A/c Dr  
To Commission A/c  

---

## 23. Discount Allowed
**Keywords:** discount allowed  
**Effect:** Capital ↓  
**Journal:**  
Discount A/c Dr  

---

## 24. Discount Received
**Keywords:** discount received  
**Effect:** Capital ↑  
**Journal:**  
Discount A/c Cr  

---

## 25. Depreciation Charged
**Keywords:** depreciation  
**Effect:** Asset ↓, Capital ↓  
**Journal:**  
Depreciation A/c Dr  
To Asset A/c  

---

## 26. Bad Debts
**Keywords:** bad debts  
**Effect:** Debtors ↓, Capital ↓  
**Journal:**  
Bad Debts A/c Dr  
To Debtors A/c  

---

## 27. Insurance Paid
**Keywords:** insurance paid  
**Effect:** Cash ↓, Capital ↓  
**Journal:**  
Insurance A/c Dr  
To Cash A/c  

---

## 28. Advertising Expense
**Keywords:** advertisement  
**Effect:** Cash ↓, Capital ↓  
**Journal:**  
Advertisement A/c Dr  
To Cash A/c  

---

## 29. Repair Expense
**Keywords:** repair, maintenance  
**Effect:** Cash ↓, Capital ↓  
**Journal:**  
Repairs A/c Dr  
To Cash A/c  

---

## 30. Owner’s Salary
**Keywords:** owner salary  
**Effect:** Capital ↓  
**Journal:**  
Capital A/c Dr  

---

(… continues with **utilities, office expenses, prepaid expenses, outstanding expenses, accrued income, advance income, depreciation on machinery, depreciation on furniture, GST paid, GST collected, stock withdrawn, goods destroyed, charity, donation, bank charges, interest received, closing stock, opening stock, provision for doubtful debts, commission paid, audit fees, carriage inward, carriage outward, brokerage, freight, printing, stationery, postage, travelling expenses, legal charges, professional fees, income tax paid, drawings in goods, sales return, purchase return, cash deposited in bank, cash withdrawn from bank, bank overdraft, petty cash expense, suspense adjustment, capital reserve, general reserve, revaluation profit, revaluation loss)

---

## NOTE
This rule file is **extensible**.  
New transactions can be added without modifying application code.

---
