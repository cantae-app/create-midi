import os
import sys
import midi as midi
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')
directory = 'C:/Users/luciano.oliveira/Music/Separadas'

for arquivo in os.listdir(directory):
    if arquivo.endswith('(Vocals).mp3'):
        try:
            cleanName = arquivo.replace(' - (Vocals).mp3', '')
            cleanName = cleanName.encode('utf-8', errors='ignore').decode('utf-8')
            filename = path = Path(f'{directory}/{arquivo}')
            midi.convert_to_midi(filename, directory, cleanName)
        except Exception as e:
            print(f"Erro to process file: {arquivo}")
            print(f"Erro: {e}")