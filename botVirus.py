#!/usr/bin/python
# -*- coding: utf-8 -*-
import time,os,sys
import telepot
from pexpect import pxssh
from pprint import pprint
from telepot.loop import MessageLoop


def Esegui(messaggio):
    pprint(messaggio)
    chatId=messaggio["chat"]["id"]
    

    if messaggio['from']['id'] == Id1 or messaggio['from']['id'] == Id2:
      
      
      
      
        if 'document' in messaggio.keys():
                  
            bot.download_file(messaggio['document']['file_id'],'Scaricati/' + str(messaggio['document']['file_name']))
            global lastFile
            lastFile = messaggio['document']['file_name']
            return
          
          
          
        if 'text' in messaggio.keys():
          
          
            if messaggio['text'].startswith('python3 scaricato'):   #Esegue ultimo file scaricato in python3
                try:
                    os.system('python3 Scaricati/' + str(lastFile) + ' > output.txt')
                    bot.sendDocument(messaggio['chat']['id'],document=open("output.txt"))
                    os.system("rm output.txt")
                    return
                    
                except Exception as e:
                    bot.sendMessage(chatId,'Errore: ' + str(e))
                    return
                    
                    
            if messaggio['text'].startswith('python scaricato'):    #Esegue ultimo file scaricato in python2
                try:
                    os.system('python Scaricati/' + str(lastFile) + ' > output.txt')
                    bot.sendDocument(messaggio['chat']['id'],document=open("output.txt"))
                    os.system("rm output.txt")
                    return
                    
                except Exception as e:
                    bot.sendMessage(chatId,'Errore: ' + str(e))
                    return
            
            
            if messaggio['text'].startswith('python'):    #Esegue file python2 specificato
                filename=messaggio["text"].split(" ")[1]
                try:
                    os.system('python Scaricati/' + str(filename) + ' > output.txt')
                    bot.sendDocument(chatId,document=open("output.txt"))
                    os.system("rm output.txt")
                    return
                    
                except Exception as e:
                    bot.sendMessage(chatId,'Errore: ' + str(e))
                    return
                  

            if messaggio['text'].startswith('python3'):   #Esegue file python3 specificato
                filename=messaggio["text"].split(" ")[1]
                try:
                    os.system('python3 Scaricati/' + str(filename) + ' > output.txt')
                    bot.sendDocument(chatId,document=open("output.txt"))
                    os.system("rm output.txt")
                    return
                  
                except Exception as e:
                    bot.sendMessage(chatId,'Errore: ' + str(e))
                    return
                  
                  
            if messaggio['text'].startswith('#'):   #Esegue comando specificato
                command=messaggio["text"].split("#")[1]
                try:
                    os.system(str(command) + " > output.txt")
                    outputFile=open("output.txt", "r")
                    output=outputFile.readlines()
                    outputFile.close()
                    output="".join(output)
                    if(len(output)==0):output="Eseguito"
                    bot.sendMessage(chatId,output)
                    os.system("rm output.txt")
                    return
                except Exception as e:
                    bot.sendMessage(chatId,'Errore: ' + str(e))
                    return
                  
                  
            if(messaggio["text"].startswith("&")):    #Esegue comando specificato senza output
                command=messaggio["text"].split("&")[1]
                try:
                    os.system(str(command)+" &")
                    bot.sendMessage(chatId,"Eseguito")
                    return
                except Exception as Err:
                    bot.sendMessage(chatId,"Errore: "+str(Err))
                    return
                  
                  
            if(messaggio["text"].startswith("/")):    #Manda il file contenuto nel path
                try:
                    bot.sendDocument(chatId,document=open(messaggio["text"]))
                    return
                except Exception as Err:
                    bot.sendMessage(chatId,"Errore: "+str(Err))
                    return
                  
            if(messaggio["text"].startswith("ssh")):    #Si connette a un host con un indirizzo un nome e una password
                username=messaggio["text"].split("@")[1]   #ssh@username@password@hostname
                password=messaggio["text"].split("@")[2]
                hostname=messaggio["text"].split("@")[3]
                try:
                    global s
                    s=pxssh.pxssh()
                    s.login(hostname,username,password)
                    bot.sendMessage(chatId,("Connesso a "+str(hostname)))
                    return
                except Exception as Err: 
                    bot.sendMessage(chatId,"Errore: "+str(Err))
                    return
                   
            if(messaggio["text"].startswith("ss#")):    #Esegue il comando sull' ssh connesso
                command=messaggio["text"].split("#")[1]
                try:               
                    s.sendline(command)
                    s.prompt()
                    output=s.before
                    bot.sendMessage(chatId,output.decode("utf-8") )
                    return
                except Exception as Err:
                    bot.sendMessage(chatId,"Errore: "+str(Err))
                    return
                                    
                                    
            if(messaggio["text"].lower()=="close ssh"):   #Chiude la connessione ssh
                try:
                    s.close()
                    bot.sendMessage(chatId,"Connessione chiusa")
                    return
                except Exception as Err:
                    bot.sendMessage(chatId,"Errore: "+str(Err))
                    return
                  
                  
            if(messaggio["text"].startswith("ss&")):    #Esegue il comando sull' ssh connesso
                command=messaggio["text"].split("&")[1]
                try:               
                    s.sendline(str(command)+" &")
                    s.prompt()
                    output=s.before
                    bot.sendMessage(chatId,output.decode("utf-8") )
                    return
                except Exception as Err:
                    bot.sendMessage(chatId,"Errore: "+str(Err))
                    return
                                    


    return


bot = telepot.Bot('1363795431:AAGGVwTqgfAreQIlmIJMgjtE9So9ZLjmCmc')

global Id1
global Id2


Id1 = 243898019
Id2 = 514341799

try:
  bot.sendDocument(Id1,document=open("output.txt"))
  bot.sendDocument(Id2,document=open("output.txt"))
  os.system("rm output.txt")
except:
    pass


MessageLoop(bot, Esegui).run_as_thread()

while 1:
    time.sleep(3600)
    sys.exit()

                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    
                                    