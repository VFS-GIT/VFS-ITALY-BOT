# -*- coding: utf-8 -*-
import os
import time
import requests
import telebot

# 1. Connexion sécurisée au bot avec ton TELEGRAM_TOKEN configuré sur Railway
TOKEN = os.environ.get("TELEGRAM_TOKEN")

if not TOKEN:
    print("ERREUR : La variable TELEGRAM_TOKEN est manquante sur Railway!")
    # Token de secours si tu as oublié de le mettre dans les paramètres Railway
    TOKEN = "METS_TON_TOKEN_ICI_SI_OUBLIE"

bot = telebot.TeleBot(TOKEN)

print("--- LE BOT TELEGRAM VFS ITALIE EST LANCE AVEC SUCCES ---")

# URL de test de la page VFS Global Italie en Algérie
URL_CIBLE = "https://visa.vfsglobal.com/algerie/fr/ita/"

def verifier_site():
    """Fonction simple qui vérifie si le site VFS répond"""
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        reponse = requests.get(URL_CIBLE, headers=headers, timeout=15)
        if reponse.status_code == 200:
            print("[INFO] Verification VFS : Le site repond parfaitement.")
            return True
        else:
            print(f" Code reponse anormal de VFS : {reponse.status_code}")
            return False
    except Exception as e:
        print(f" Impossible de joindre la plateforme VFS : {e}")
        return False

# Boucle infinie pour que ton bot tourne H24 sans s'arrêter sur Railway
while True:
    try:
        print("[CHECK] Verification des creneaux en cours...")
        verifier_site()
        
        # Le bot fait sa vérification puis attend 5 minutes (300 secondes) avant de recommencer
        time.sleep(300)
        
    except Exception as e:
        print(f" Probleme dans la boucle : {e}")
        time.sleep(60)
