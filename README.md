# rasp-diaporama
Un simple diaporama plein écran pour Raspberry Pi. Le but était de projeter un diaporama composé de n images en fullscreen sur un écran dans une salle de classe, avec des infos pour les élèves sur chaque image (science, histoire, règles de grammaire, autre...), avec une série d'image différente pour chaque jour de la semaine.

## howto
1. télécharger le contenu de ce repo git dans le dossier de votre choix sur le Raspberry (par exemple /home/me/Apps/)
2. ajouter, dans le même dossier, un dossier pour chaque jour de la semaine (lundi, mardi, mercredi, ...) avec des images à l'intérieur
3. lancer le script pour le tester, dans un terminal :
```
python /home/me/Apps/Diaporama/diaporama.py
```
4. le script est réglé pour fonctionner 10 minutes (600 secondes). Chaque image sera affichée pendant n secondes, n étant les 600 secondes divisées par le nombre d'images. Puis le script va mettre en standby l'écran. Pour que le script puisse se lancer plusieurs fois, il faut créer une exécution automatique de tâche (tâche cron). Pour ce faire, dans un terminal, ouvrir la config 'crontab' :
```
crontab -e
```
Et ajouter au fond la ligne suivante :
```
*/11 13-17 * * * /usr/bin/python /home/me/Apps/Diaporama/diaporama.py
```
Il faudra ensuite redémarrer le Raspberry et le script va se lancer, dans cet exemple, toutes les 11 minutes (*/11) entre 13h et 17h (13-17). Si on voulait que le script se lance également tous les matins de 08h à 12h, il faudrait ajouter la ligne suivante :
```
*/11 08-12 * * * /usr/bin/python /home/me/Apps/Diaporama/diaporama.py
```
Ne pas hésiter à consulter le site [crontab.guru.com](https://crontab.guru/#*_*/6_*_*_*) pour lancer le script quand vous le souhaitez.
5. optionnel : il est possible de créer une synchronisation automatique des dossiers images avec Dropbox. Pour cela, il faut [créer une App](https://www.dropbox.com/developers/reference/getting-started) pour obtenir des informations de connexion. Puis, on peut synchroniser les dossiers nommés lundi, mardi, ... dans notre App Dropbox avec les dossiers présents sur notre Raspberry. Il suffit ensuite de changer les images dans les dossiers Dropbox pour qu'ils se mettent à jour sur le Raspberry. Pour cela, il faut appeler le script de synchronisation 1 fois par jour par exemple, toujours en éditant 'crontab' :
```
30 6 * * * bash /home/gabmichelet/Apps/sync_images.sh
```
Ici, tous les jours à 06h30, les images seront synchronisées entre Dropbox et le Raspberry.