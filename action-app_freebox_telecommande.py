#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import requests
import time
from snipsTools import SnipsConfigParser
from hermes_python.hermes import Hermes
from hermes_python.ontology import *
import io

CONFIG_INI = "config.ini"

# If this skill is supposed to run on the satellite,
# please get this mqtt connection info from <config.ini>
# Hint: MQTT server is always running on the master device
MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

#REMOTE_ADDR = 'http://hd1.freebox.fr/pub/remote_control?code='
#self.hdnumber = self.config.get("secret").get("hdnumber")
        #self.freeremotecode = self.config.get("secret").get("freeremotecode")
        #self.defaultchannel = self.config.get("secret").get("defaultchannel")
        #self.remoteaddr = 'http://hd'+self.hdnumber+'.freebox.fr/pub/remote_control?code='+self.freeremotecode

     #jeedomAPIKEY = self.config.get("secret").get("jeedomAPIKEY")
    jeedomIP = self.config.get("secret").get("jeedomIP")   
        
REMOTE_ADDR = 'http://'+jeedomIP+'/core/api/jeeApi.php?apikey='   #+jeedomAPIKEY+'&type=interact&query='        
        
class TelecommandeFreebox(object):
    """Class used to wrap action code with mqtt connection

        Please change the name refering to your application
    """

    def __init__(self):
        # get the configuration if needed
        try:
            self.config = SnipsConfigParser.read_configuration_file(CONFIG_INI)
        except :
            self.config = None


        # start listening to MQTT
        self.start_blocking()

    def askFreeboxCommand_callback(self, hermes, intent_message):
        # terminate the session first if not continue

        print "Lancement des commandes vocales de la maison"
        hermes.publish_end_session(intent_message.session_id, "")

        commandeFreebox = None
        subcommandeFreebox = None

        print '[Recep] intent value: {}'.format(intent_message.slots.TvCommand.first().value)

        #if intent_message.slots.TvChannel.first().value == 'oncle':
            #print '[Received] intent: {}'.format(intent_message.slots.TvChannel)
        commandeFreebox = intent_message.slots.TvCommand.first().value
        #subcommandeFreebox = intent_message.slots.TvSubCommand.first().value

        if commandeFreebox is None:
            telecommande_msg = "Je ne comprend pas ce que vous me demandez"
            quit()

        #else:

        #FREEREMOTECODE = self.config.get("secret").get("freeremotecode")
        jeedomAPIKEY = self.config.get("secret").get("jeedomAPIKEY")

        if commandeFreebox == 'onsalon
            self.onsalon(jeedomAPIKEY)
        elif commandeFreebox == 'offsalon
            self.offsalon(jeedomAPIKEY)
        elif commandeFreebox == 'onsejour
            self.onsejour(jeedomAPIKEY)
        elif commandeFreebox == 'offsejour
            self.offsejour(jeedomAPIKEY)
        
        
        #if commandeFreebox == 'power':
         #   self.powerFreebox(FREEREMOTECODE)
        #elif commandeFreebox == 'pip':
         #   self.pip(FREEREMOTECODE)
        #elif commandeFreebox == 'switchpip':
         #   self.switchPip(FREEREMOTECODE)
        #elif commandeFreebox == 'stopip':
         #   self.stopPip(FREEREMOTECODE)
        #elif commandeFreebox == 'direct':
         #   self.direct(FREEREMOTECODE)
        #elif commandeFreebox == 'rewind':
         #   self.rewind(FREEREMOTECODE)
        #elif commandeFreebox == 'forward':
         #   self.forward(FREEREMOTECODE)
        #elif (commandeFreebox == 'play') or (commandeFreebox == 'pause'):
         #   self.playPause(FREEREMOTECODE)
        #elif (commandeFreebox == 'mute') or (commandeFreebox =='unmute'):
         #   self.muteUnmute(FREEREMOTECODE)
        #elif commandeFreebox == 'volDown':
         #   self.volDown(FREEREMOTECODE)
        #elif commandeFreebox == 'volup':
         #   self.volUp(FREEREMOTECODE)
        #elif commandeFreebox == 'television' :
         #   self.television(FREEREMOTECODE)
        #elif commandeFreebox=='twitch':
         #   self.twitch(FREEREMOTECODE)
        #elif commandeFreebox == 'sortprogrammetv' :
         #   self.exitProgTv(FREEREMOTECODE)
        #elif commandeFreebox == 'programmetv':
         #   self.progTv(FREEREMOTECODE)
      
        #elif (subcommandeFreebox is not None) and (subcommandeFreebox == 'chaîne'):
        #    if (commandeFreebox == 'next') :
        #        self.nextChannel(FREEREMOTECODE)
        #    elif (commandeFreebox== 'previous'):
        #        self.previousChannel(FREEREMOTECODE)
       
        #elif (commandeFreebox == 'next'):
         #   self.right(FREEREMOTECODE)
        #elif (commandeFreebox == 'previous') :
         #   selft.left(FREEREMOTECODE)
        #else :
         #   self.channelChange(commandeFreebox,FREEREMOTECODE)

        quit()
            #telecommande_msg = 'J\'allume la télévision'
        # if need to speak the execution result by tts
        #    hermes.publish_start_session_notification(intent_message.site_id, telecommande_msg, "FreeboxTelecommande")
        #
    
    def onsalon(self,jeedomAPIKEY):
        requests.get(REMOTE_ADDR+jeedomAPIKEY+'&type=interact&query=allume la lumière du salon')
        quit()
    def offsalon(self,jeedomAPIKEY):
        requests.get(REMOTE_ADDR+jeedomAPIKEY+'&type=interact&query=éteind la lumière du salon')
        quit()
    def onsejour(self,jeedomAPIKEY):
        requests.get(REMOTE_ADDR+jeedomAPIKEY+'&type=interact&query=allume la lumière du séjour')
        quit()
    def offsejour(self,jeedomAPIKEY):
        requests.get(REMOTE_ADDR+jeedomAPIKEY+'&type=interact&query=éteind la lumière du séjour')
        quit()
    

    # --> Master callback function, triggered everytime an intent is recognized
    def FreeboxTelecommande_callback(self,hermes, intent_message):
        coming_intent = intent_message.intent.intent_name

        print '[Recept] intent {}'.format(coming_intent)
        if coming_intent == 'Tarlak:ChannelFreebox':
            self.askFreeboxCommand_callback(hermes, intent_message)
        # more callback and if condition goes here...

    # --> Register callback function and start MQTT
    def start_blocking(self):
        with Hermes(MQTT_ADDR) as h:
            h.subscribe_intents(self.FreeboxTelecommande_callback).start()

if __name__ == "__main__":
    TelecommandeFreebox()
