# https://dodona.ugent.be/nl/courses/1523/series/16787/activities/761303597


gekochteStuks = int(input())
kostprijsPStuk = float(input())
barcodes = int(input())
mijlen = int(input())

totaalPrijs = gekochteStuks * kostprijsPStuk
aantalMijlen = (gekochteStuks - (gekochteStuks % barcodes)) / barcodes * mijlen

print(f'Phillips spendeerde ${totaalPrijs} voor {aantalMijlen} frequent flyer mijlen.')