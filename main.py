import os
import sys
import midi as midi

sys.stdout.reconfigure(encoding='utf-8')
directory = 'C:/Users/luciano.oliveira/Music/Separadas'

# Percorre o diretório principal e todas as subpastas
for root, dirs, files in os.walk(directory):
    for arquivo in files:
        if arquivo.endswith('(Vocals).mp3'):
            try:
                cleanName = arquivo.replace(' - (Vocals).mp3', '')
                cleanName = cleanName.encode('utf-8', errors='ignore').decode('utf-8')
                
                # Usa os.path.join para criar caminhos compatíveis com o sistema
                input_file = os.path.join(root, arquivo)
                output_dir = root  # Mantém o arquivo MIDI na mesma pasta do MP3
                
                # Verifica se o arquivo MIDI já existe na pasta atual
                midi_path = os.path.join(output_dir, f'{cleanName}.mid')
                if os.path.isfile(midi_path):
                    print(f"File {cleanName}.mid already exists in {output_dir}")
                    continue
                
                # Converte para MIDI usando o caminho completo
                midi.convert_to_midi(input_file, output_dir, cleanName)
                
            except Exception as e:
                print(f"Error processing file: {arquivo}")
                print(f"Error: {e}")
