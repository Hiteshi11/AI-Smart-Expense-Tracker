import easyocr

reader = easyocr.Reader(['en'])

results = reader.readtext('receipts/r1.webp')

text_list = []

print("Detected Text:\n")

for detection in results:
    text = detection[1]
    text_list.append(text)
    print(text)

print("\nSearching for TOTAL...\n")

total_amount = None

for i in range(len(text_list)):
    
    word = text_list[i].upper()

    if "TOTAL" in word:
        
        # check next element for amount
        if i + 1 < len(text_list):
            total_amount = text_list[i + 1]
            break

if total_amount:
    print("Total Expense Found:", total_amount)
else:
    print("Total not detected")
