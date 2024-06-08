// Inclusão das Bibliotecas
#include "SoftwareSerial.h"
#include "DFRobotDFPlayerMini.h"

//Inicia a serial para Módulo DFPlayer Mini e cria variável para controle do módulo
SoftwareSerial mySoftwareSerial(10, 11); // RX, TX
DFRobotDFPlayerMini myDFPlayer;

// Declaração de variáveis
int pin_botao1 = 0;
int pin_botao2 = 1;
int pin_botao3 = 2;
int pin_botao4 = 3;
int pin_botao5 = 4;
int pin_botao6 = 5;
int pin_botao7 = 6;
int pin_botao8 = 7;
int pin_botao9 = 8;
int pin_botao10 = 9;
int pin_botao11 = 12;
int pin_botao12 = 13;
int pin_botao13 = 14;
int pin_botao14 = 15;
int pin_botao15 = 16;
int pin_botao16 = 17;
int pin_botao17 = 18;
int pin_botao18 = 19;


int botao1 = 1;
int botao2 = 1;
int botao3 = 1;
int botao4 = 1;
int botao5 = 1;
int botao6 = 1;
int botao7 = 1;
int botao8 = 1;
int botao9 = 1;
int botao10 = 1;
int botao11 = 1;
int botao12 = 1;
int botao13 = 1;
int botao14 = 1;
int botao15 = 1;
int botao16 = 1;
int botao17 = 1;
int botao18 = 1;
int pausa = 0;
/* 
 * SETUP 
 */
 
void setup(){

 // Configura pinos dos botões    
  pinMode(pin_botao1, INPUT_PULLUP);
  pinMode(pin_botao2, INPUT_PULLUP);
  pinMode(pin_botao3, INPUT_PULLUP);
  pinMode(pin_botao4, INPUT_PULLUP);
  pinMode(pin_botao5, INPUT_PULLUP);
  pinMode(pin_botao6, INPUT_PULLUP);
  pinMode(pin_botao7, INPUT_PULLUP);
  pinMode(pin_botao8, INPUT_PULLUP);
  pinMode(pin_botao9, INPUT_PULLUP);
  pinMode(pin_botao10, INPUT_PULLUP);
  pinMode(pin_botao11, INPUT_PULLUP);
  pinMode(pin_botao12, INPUT_PULLUP);
  pinMode(pin_botao13, INPUT_PULLUP);
  pinMode(pin_botao14, INPUT_PULLUP);
  pinMode(pin_botao15, INPUT_PULLUP);
  pinMode(pin_botao16, INPUT_PULLUP);
  pinMode(pin_botao17, INPUT_PULLUP);
  pinMode(pin_botao18, INPUT_PULLUP);

  // Comunicacao serial com o módulo
  mySoftwareSerial.begin(9600);
  
  // Inicializa a serial do Arduino
  Serial.begin(115200);
  
  // Verifica se o módulo está conectado e se cartão SD foi inserido
  Serial.println();
  Serial.println(F("DFRobot DFPlayer Mini"));
  Serial.println(F("Inicializando módulo DFPlayer..."));
  if (!myDFPlayer.begin(mySoftwareSerial))
  {
    Serial.println(F("Não inicializado:"));
    Serial.println(F("- Verifique se módulo foi corretamente conectado ou"));
    Serial.println(F("- Insira um cartão SD"));
    while (true);
  }
  // Definições iniciais
  myDFPlayer.setTimeOut(500); //  Timeout serial 500ms
  myDFPlayer.volume(30);      //  Volume (de 0 até 30)
  myDFPlayer.EQ(DFPLAYER_EQ_NORMAL);           //  Equalização normal
  
  Serial.println();
  Serial.print("Número de arquivos no cartão: ");
  Serial.println(myDFPlayer.readFileCounts(DFPLAYER_DEVICE_SD)); 
  Serial.println();
  Serial.println(F("Módulo DFPlayer Mini inicializado corretamente!"));

  delay(2000);
  myDFPlayer.play(1); // Inicia módulo já tocando música 1

}

/* 
 * LOOP 
 */

void loop() {

  // Faz leitura dos botões
  botao1 = digitalRead(pin_botao1);
  botao2 = digitalRead(pin_botao2);
  botao3 = digitalRead(pin_botao3);
  botao4 = digitalRead(pin_botao4);
  botao5 = digitalRead(pin_botao5);
  botao6 = digitalRead(pin_botao6);
  botao7 = digitalRead(pin_botao7);
  botao8 = digitalRead(pin_botao8);
  botao9 = digitalRead(pin_botao9);
  botao10 = digitalRead(pin_botao10);
  botao11 = digitalRead(pin_botao11);
  botao12 = digitalRead(pin_botao12);
  botao13 = digitalRead(pin_botao13);
  botao14 = digitalRead(pin_botao14);
  botao15 = digitalRead(pin_botao15);
  botao16 = digitalRead(pin_botao16);

  botao17 = digitalRead(pin_botao17);
  botao18 = digitalRead(pin_botao18);

  // Se pressionou botão 1 uma vez reproduz grupo 1, se pressionar novamente para a reprodução
  if (botao1 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(1); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 2 uma vez reproduz grupo 2, se pressionar novamente para a reprodução
  if (botao2 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(2);
    delay(1000); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 3 uma vez reproduz grupo 3, se pressionar novamente para a reprodução
  if (botao3 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(3); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }
 
  // Se pressionou botão 4 uma vez reproduz grupo 4, se pressionar novamente para a reprodução
  if (botao4 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(4); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 5 uma vez reproduz grupo 5, se pressionar novamente para a reprodução
  if (botao5 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(5); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 1 uma vez reproduz grupo 6, se pressionar novamente para a reprodução
  if (botao6 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(6); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 7 uma vez reproduz grupo 7, se pressionar novamente para a reprodução
  if (botao7 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(7); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 1 uma vez reproduz grupo 8, se pressionar novamente para a reprodução
  if (botao8 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(8); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 9 uma vez reproduz grupo 9, se pressionar novamente para a reprodução
  if (botao9 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(9); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 10 uma vez reproduz grupo 10, se pressionar novamente para a reprodução
  if (botao10 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(10); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 11 uma vez reproduz grupo 11, se pressionar novamente para a reprodução
  if (botao11 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(11); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 12 uma vez reproduz grupo 12, se pressionar novamente para a reprodução
  if (botao12 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(12); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 13 uma vez reproduz, se pressionar novamente para a reprodução
  if (botao13 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(13); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 14 uma vez reproduz grupo 14, se pressionar novamente para a reprodução
  if (botao14 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(14); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 15 uma vez reproduz grupo 15, se pressionar novamente para a reprodução
  if (botao15 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(15); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 16 uma vez reproduz grupo 16, se pressionar novamente para a reprodução
  if (botao16 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(16); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 17 uma vez reproduz, se pressionar novamente para a reprodução
  if (botao17 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(17); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Se pressionou botão 18 uma vez reproduz, se pressionar novamente para a reprodução
  if (botao18 == LOW) {
    pausa = !pausa; 
    if (pausa == 0) { 
      myDFPlayer.loopFolder(18); 
    }
    if (pausa == 1) {
      myDFPlayer.pause();
    }
  }

  // Atraso
  delay(200);
}
