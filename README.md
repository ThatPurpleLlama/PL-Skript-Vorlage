Hallo, Liam hier

Dieses Skript ist auch auf Github https://github.com/ThatPurpleLlama/PL-Skript-Vorlage/

Dieses Skript ist ein Python Skript, welches zur Auswertung von je 2 Variablen aus 2 Messreihen (2 csv dateien) verwendet werden kann  
Dabei werden, wie gesagt, 2 csv Dateien (welche üblich von digitalen messgeräten ist) eingelesen welche auf dem selben Graphen geplottet werden.
Falls dies unerwünscht ist wird im Skript beschrieben, wie man nur eine Datei einliest.
Vorab. Dieses Skript wurde manuell von Liam Larisch aus der PG521 an der TU-Berlin geschrieben. 
Bei anwendungsfragen könnt ihr mir gerne per e-mail schreiben ( liamlarisch9@gmail.com ). Bitte gebt aber bescheid, dass ich nicht verwirrt bin, falls einfach eine
random code frage kommt hahaha. Ansonsten denke ich habe ich dieses Skript vollständig Kommentiert und mit plausiblen erklärungen versehen.

viel Spaß beim experimentieren und viel Glück!! <3  

Dieses Skript darf und soll gerne an ALLE PL- und PG-Gruppen weitergegeben werden! Es gibt keinerlei
Einschränkung bei der Nutzung oder Weitergabe – im Gegenteil, ich freue mich, wenn möglichst viele
Gruppen davon profitieren und sich die Auswertung damit erleichtern können. Verändert, kürzt oder
erweitert es gerne nach eurem Bedarf, und gebt es ruhig an eure Nachfolger-Gruppen oder andere
Projektlabore/Projektgruppen weiter, damit möglichst wenig Leute das Rad neu erfinden müssen :)

Dieses Skript basiert auf das Experiment des Schwingkreises. weswegen dessen Einheiten und rechnungen beispielhaft verwendet werden.

Wenn ich ein lernender Student bin und es erlaubt WÄRE. würde ich zum anpassen des Skripts Claude, ChatGPT oder Gemini nutzen und folgenden Prompt geben,
Beschreibt einfach das Experiment und was ihr braucht und fügt folgenden Absatz ein; ändert aber den Namen und die Variable im letzten Satz!!! Und schreibt auch
ob ihr nur eine Messreihe oder 2 Messreiehn verwendet und, dass die AI euch die variablen für die zweite Messreiehe rausnimmt. Falls ihr Messfehler habt
dann schreibt das auch in den Prompt und sagt, dass die bestehende Fehlerrechnung angepasst werden müssen:

"Im Anhang befindet sich eine Vorlage zum erstellen einer Abbildung anhand von Messdaten, diese Vorlage wurde anhand des elektrischen Schwingkreises erstellt 
und dessen Variablen stehen noch drinne. Kannst du mir bitte das Skript so umschreiben, dass die gesamten verwendeten Variablen und rechnungen für die anwendunge
meines Experiments, das <Experiment hier>. Anhang befindet sich zusätzlich eine Beispielhafte messung. Und wir möchten die Variable <variable hier> fitten."

Falls ihr nur EINE Messreihe auswerten wollt (also nur eine csv Datei), müsst ihr NICHTS am Code löschen!
Sucht einfach den Abschnitt "zweite Datei und die Variablen" und setzt jeweils DREI Anführungszeichen
( 3x ' ) direkt VOR die Zeile "data2 = pd.read_csv(...)" und DREI Anführungszeichen ( 3x ' ) direkt NACH der
letzten Zeile dieses Abschnitts (also nach "anzeige_stop_2 = 6"). Damit wird der komplette Block zu einem
reinen Kommentar und Python überspringt ihn beim Ausführen.

WICHTIG: Wenn ihr die zweite Messreihe so ausblendet, müsst ihr zusätzlich weiter unten JEDE Stelle
auskommentieren oder löschen, die "data2", "U_2", "t_2" oder die Werte mit der Endung "_2" verwendet
(z. B. im Fit-Abschnitt für die zweite Datei, sowie beim Plotten von "t_2, U_2" und den zugehörigen
Fehlerbalken/Fit-Kurven/Infotexten in Abbildung 1 und 2). Sonst wirft Python einen Fehler, weil diese
Variablen dann nicht mehr existieren.

Das Skript wird, so wie es gerade ist, nicht mit den messdaten vom Schwingkreis aus unserem Experiment Funktionieren (ironisch ich weiß)
Liegt aber daran, dass das Skript für eine allgemeine Anwendung umgeschrieben wurde. Ich könnt das Originale Skript im Protokoll auf dem PL-Wiki finden.
(WIe gesagt. PL-Wiki -> Experimente -> (Elektrischer) Schwingkreis -> PG521 Protokoll) falls es schon hochgeladen wurde

Typische Fehle:
modules sind nicht runtergeladen. bswp muss numpy als module runtergeladen werden um es dann erst importieren zu können. Falls in der Konsole solche Fehler auftreten
googled einfach kurz wie ihr es runterladet!

Falsche benennung des Dokuments. Es muss wirklich mit Groß und Klein schreibung alles gleich sein wie der Name also bei Mappe1.csv darf es nicht mappe1.csv oder mapPe1.csv oderso sein
