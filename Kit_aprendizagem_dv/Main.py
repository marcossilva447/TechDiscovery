import serial

# Defina a porta serial e a taxa de transmissão
porta_serial = '/dev/ttyACM0'  # Substitua pela porta correta do seu Arduino
taxa_transmissao = 9600  # Substitua pela taxa de transmissão correta do seu Arduino

# Inicialize a comunicação serial
arduino = serial.Serial(porta_serial, taxa_transmissao)

# Agora você pode enviar comandos para o Arduino
comando = 'L'  # Exemplo de comando para ligar um LED no Arduino
arduino.write(comando.encode())

# Leia a resposta do Arduino
resposta = arduino.readline().decode().strip()
print(f'Resposta do Arduino: {resposta}')

# Feche a comunicação serial quando terminar
arduino.close()