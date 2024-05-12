from jiwer import wer 
from docx import Document

reference = """"Giroud André Vincent Lieutenant au 9e Rt d'artillerie Tunis ordre de Nichan 
Décoration de Officier portée sans rosette avec Croix Décret du 11 8bre 1883 
Enregé sous le N° 7 927"""
hypothesis = """Trorea André Vinceur e rienttenant au 9. D d'artilleri Ondre de Richan 
Decvration de Riciel  porlée dans rosette avec lean Decret du 11 E 1883 
Cureg^e sous le Si.J"""

# Calculer le WER
WER = wer(reference, hypothesis)
WAcc = 1 - WER

print(WAcc)