'''

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

'''






# Importieren der benötigten Bibliotheken
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import datetime
import scipy.odr as odr
import locale
from pprint import pprint
from scipy.optimize import curve_fit
from pathlib import Path

#Lokalisierung auf Deutschland (bspw wird in deutschland ein komma für Dezimaltrennung verwendet also 22.2 m/s sind 22,2 m/s im deutschen)
locale.setlocale(locale.LC_NUMERIC, "de_DE")
plt.rcParams["axes.formatter.use_locale"] = True
plt.rcParams["text.usetex"] = False



######################
#  erste Datei und die Variablen
######################


# Einlesung der Daten in die Variable "datei" inkl. Unterteilung der Messdaten X (Zeit) und CH1 (Spannung)
# Hierbei ersetzt ihr jede X mit der ersten Variable, welche auf der X-Achse geplottet wird (einfach STRG+F und X suchen, bzw auf mac CMD+F)
# mit "Path(__file__).parent" werden dokumente aus der selben directory (dem selben Ordner) gesucht mit dem namen "Mappe1.csv"
# Also sollte die Python datei, sozusagen neben den Messdaten sein. Wenn ihr also einen Messdaten ordner habt muss das Python Skript dort auch rein, damit es die Daten lesen kann
# diese Ansatz ist für mich als Programmierer sinnvoll, da ich nicht weiß wie eure lokale datenstruktur aufgebaut ist, und ich hiermit eine leichte möglichkeit darbiete,
# damit ihr einfach mit diesem Skript umgehen könnt.
# ganz unten steht nochmal wie also die Dateistruktur aussehen muss!!!!!!
datei1 = Path(__file__).parent / "Mappe1.csv"

#jetzt werden die daten aus datei im array "data" gespeichert (kleiner aber wichtige änderung im Namen, zur differenzierung)
#falls ihr nicht wisst was der seperator von daten und die decimal verwendung ist. Öffnet das dokument in einem simplen notepad (auf windows halt einfach notepad)
#und schaut euch die daten an. In einem CSV werden die daten typischer weise mit einem ";" in spalten separiert und per Zeilenumbruch in Zeilen.
#falls ihr hier nun auch einen punkt für die Dezimalstelle verwendet könnt ihr das hier nun auch ändern
data = pd.read_csv(datei1, sep=",",decimal=".")

#hier werden die daten aus den jeweiligen spalten in 2 unterschiedliche "arrays" gespeichert. damit die auswertung nachher angenehmer ist.
data['X'] = pd.to_numeric(data['X'], errors='coerce')
data['CH1'] = pd.to_numeric(data['CH1'], errors='coerce')

#Hier könnt ihr die Nullstelle manuell verschieben. Falls ihr bspw mit den messwerten angefangen habt, ohne einen trigger zu verwenden
#oder eine bestimmten Nullpunkt haben wollt. müsst ihr halt manuell anpassen
start_time_1 = 0

#Daten werden nun ein weiters mal in Variablen gelesen, falls etwa eine Umrechnung stattfinden muss, da bspw die Zeit in 0.5s intervall aufgenommen wurde kann dies hier geschehen
U_1 = data['CH1']
t_1 = (start_time_1 + data['X'])

#hier wird ein Offset eingestellt. welches Relativ zum Nullpunkt verschoben wird. falls ihr bspw mit einer messung 3 sekunden vorlauf hattet.
#könnt ihr das hier verschieben
schwingung_offset_1 = 0.0
t_1 = t_1 - schwingung_offset_1

#hier geht es jetzt um die angezeigte Zeit, die vor und nach t = 0 angezeigt wird
anzeige_start_1 = -0.15 # 0.15 ms vor t = 0 wird noch angezeigt, tbh idk ob ms noch genau ist. dies messdaten waren vom schwingkreis in ms, weswegen das gut gepasst hat
#sollte aber eigentlich die anzahl der messdaten sein. spielt einfach mit dem Wert rum (auch im tausender bereich) und schaut was passt.  
anzeige_stop_1  =  6 # das gleiche basically hier auch






######################
# zweite Datei und die Variablen, selben kommentare wie oben, falls ihr nur eine Messreihe haben wollt, dann nutzt  -> ''' <- am anfang und am ende von dem Codeblock
# oben (Ab Zeile 1, wo die einleitung steht) könnt ihr nochmal sehen wie das FUkntioniert, ihr würdest aus dem Code bascially nen kommentar machen.
######################
datei2 = Path(__file__).parent / "Mappe2.csv"
data2 = pd.read_csv(datei2, sep=",",decimal=".")

data2['X'] = pd.to_numeric(data2['X'], errors='coerce')
data2['CH1'] = pd.to_numeric(data2['CH1'], errors='coerce')

start_time_2 = 0

U_2 = data2['CH1']
t_2 = (start_time_2 + data2['X'])

schwingung_offset_2 = 0
t_2 = t_2 - schwingung_offset_2

#hier wird nochmal die anzeige limitiert, am ende wird von den beiden das max und min gewählt. was euch einfach ermöglicht die maxima und minima aus den messdaten zu übernehmen
#das programm wählt dann von selbst, welcher wert relevanter ist.
anzeige_start_2 = -0.15
anzeige_stop_2  =  6





######################
# Fehlerrechnung, Daten müssen manuell geändert werden
######################

# Bauteilfehler aus Multimetermessung
# hier haben wir basically einfach die gemessenen daten von einem Multimeter aufgeschrieben.
# bspw haben wir einen Widerstand von 2 Ohm verwendet. das mit einem Multimeter gemessen, 2.9 Ohm abgelesen und diesen wert dann eingetragen.
# wird später für die Fehlerrechnung relevant
C_1  = 0.10e-6 # F  (0,1 µF)
R_1  = 2.9 # Ω
L_1  = 104e-3 # H

# Relative Fehler des Multimeters anhand von dem Handbuch abgelesen. Also schaut in die Dokumentation vom Messgerät
dC_1 = 0.04 * C_1 # ±4 %
dR_1 = 0.008 * R_1 # ±0,8 %
dL_1 = 0.02 * L_1 # ±2 %

# das gleiche für die 2te messung
# Bauteilfehler aus Multimetermessung
C_2  = 0.31e-6 # F  (0,31 µF)
R_2  = 2.9 # Ω
L_2  = 104e-3 # H

dC_2 = 0.04 * C_2
dR_2 = 0.008 * R_2
dL_2 = 0.02 * L_2




# Oszilloskopfehler
# wir haben für die Messung ein Oszilloskop als Spannungsmessgerät verwendet. daher auch die Fehler von diesem Gerät.
# auch jeweils für die beiden Messungen
# hier auch erstmal die einstellung selbt. Also pro div wurden 50mV angezeigt
V_per_div_1 = 50.0   # mV/div
V_per_div_2 = 50.0   # mV/div

#umgerechnet auf das gesamte bild (8x ist von unserem oszilloskop die menge an divisions die angezeigt werden)
full_scale_1 = 8.0 * V_per_div_1
full_scale_2 = 8.0 * V_per_div_2

#hier der fehler vom Gain aus der Bedienungsanleitung
gain_err_1 = 0.03 * full_scale_1
gain_err_2 = 0.03 * full_scale_2

#hier der fehler vom offset aus der Bedienungsanleitung
offset_err_1 = 0.1 * V_per_div_1 + 2.0
offset_err_2 = 0.1 * V_per_div_2 + 2.0

#hier der zusammengerechnete Fehler
U_oszi_err_1 = np.sqrt(gain_err_1**2 + offset_err_1**2)
U_oszi_err_2 = np.sqrt(gain_err_2**2 + offset_err_2**2)




# Theoretische Werte mit Fehlerfortpflanzung
# hier ist die Fehlerrechnung. Die müsst ihr je nach bestimmter parameter ändern. Ihr rechnet für nicht newtonische Fluide ja nicht mit der elektrischen Kreisfrequenz
# Ungedämpfte Frequenz omega_0
# erste messreieh
omega_0_1     = 1.0 / np.sqrt(L_1 * C_1)
d_omega_0_1   = 0.5 * omega_0_1 * np.sqrt((dL_1/L_1)**2 + (dC_1/C_1)**2)
#zweite messreihe
omega_0_2     = 1.0 / np.sqrt(L_2 * C_2)
d_omega_0_2   = 0.5 * omega_0_2 * np.sqrt((dL_2/L_2)**2 + (dC_2/C_2)**2)

# Dämpfungskonstante delta
# erste messreihe
delta_theo_1  = R_1 / (2.0 * L_1)
d_delta_theo_1 = np.sqrt((dR_1 / (2.0*L_1))**2 + (R_1 * dL_1 / (2.0*L_1**2))**2)
#zweite messreihe
delta_theo_2  = R_2 / (2.0 * L_2)
d_delta_theo_2 = np.sqrt((dR_2 / (2.0*L_2))**2 + (R_2 * dL_2 / (2.0*L_2**2))**2)

# Gedämpfte Eigenfrequenz
# erste Messreihe
omega_d_1 = np.sqrt(omega_0_1**2 - delta_theo_1**2)
domega_d_dC_1 = -1.0 / (2.0 * omega_d_1 * L_1 * C_1**2)
domega_d_dR_1 = -R_1 / (4.0 * omega_d_1 * L_1**2)
domega_d_dL_1 = (1.0 / (2.0 * omega_d_1 * L_1**2)) * (-1.0/C_1 + R_1**2 / (2.0*L_1))
d_omega_d_1 = np.sqrt((domega_d_dL_1 * dL_1)**2 + (domega_d_dC_1 * dC_1)**2 + (domega_d_dR_1 * dR_1)**2)

#zweiter messreihe
omega_d_2 = np.sqrt(omega_0_2**2 - delta_theo_2**2)
domega_d_dC_2 = -1.0 / (2.0 * omega_d_2 * L_2 * C_2**2)
domega_d_dR_2 = -R_2 / (4.0 * omega_d_2 * L_2**2)
domega_d_dL_2 = (1.0 / (2.0 * omega_d_2 * L_2**2)) * (-1.0/C_2 + R_2**2 / (2.0*L_2))
d_omega_d_2 = np.sqrt((domega_d_dL_2 * dL_2)**2 + (domega_d_dC_2 * dC_2)**2 + (domega_d_dR_2 * dR_2)**2)


# Umrechnung in 1/ms und rad/ms für den Fit-Vergleich
delta_theo_1_ms   = delta_theo_1  / 1000.0
d_delta_theo_1_ms  = d_delta_theo_1 / 1000.0
delta_theo_2_ms   = delta_theo_2  / 1000.0
d_delta_theo_2_ms  = d_delta_theo_2 / 1000.0

omega_d_1_ms  = omega_d_1  / 1000.0
d_omega_d_1_ms = d_omega_d_1 / 1000.0
omega_d_2_ms  = omega_d_2  / 1000.0
d_omega_d_2_ms = d_omega_d_2 / 1000.0
# Vollständige Fehlerrechnung ist im Protokoll für den elektischen Schwingkreis der Gruppe PG521, diese sollte im PL-Wiki zu finden sein!!!!
# ist zum jetztigen Standpunkt noch nicht Hochgeladen. aber sollte  unter Hauptseite -> Experimente -> (elektrischer) Schwingkreis zu finden sein



######################
# Fit für die Dämpfungskonstante des ersten Dokuments
######################
# Bereich der zu Fitten ist, hier also von 0 bis 6ms in unserem fall
laden_start = 0
laden_stop  = 6

#daten werden vom gegebenem bereich geladen und gefittet. Falls ihr also eine Startzeit habt. wird dort der wert nicht mit einbezogen.
# bswp falls ihr druck habt ist der ja konstant, bis ihr bswp eine Vakuumpumpe aktiviert. Dieser konstante Druck kann mit "laden_start" also rausgeschnitten werden.
idx_start_1 = np.where(t_1.values > laden_start)[0]
start_index_laden = idx_start_1[0] if len(idx_start_1) > 0 else 0

idx_stop_1 = np.where(t_1.values > laden_stop)[0]
stop_index_laden = idx_stop_1[0] if len(idx_stop_1) > 0 else len(t_1) - 1


#fit wird hier geladen
U_fit_laden  = U_1.iloc[start_index_laden:stop_index_laden].values
t_data_laden = t_1.iloc[start_index_laden:stop_index_laden].values
t_fit_laden = t_data_laden - t_data_laden[0]


# Formel der gedämpften Schwingung
# hier müsst ihr natürlich eure Gleichung verwenden
# hier wird nur eine Funktion erstellt die später noch "gerufen" werden muss. Alleine macht das hier nix
def gedaempfte_schwingung(t, U_0, delta, omega, phi):
    return U_0 * np.exp(-delta * t) * np.cos(omega * t + phi)

p0 = [U_fit_laden[0], 0.05, 8.1, 0.0]
sigma_1 = U_oszi_err_1 * np.ones_like(U_fit_laden)

#maxfev ist die Anzahl an rechnungen die Maximal durchgeführt werden, also mehr messpunkte = mehr rechnungen,
#bei unserer dritten messreieh hat es nicht funktioniert, wesegen die Anzahl der rechnungen erhöht wurde. Nachteile gibt es soweit ich weiß nicht
#falls ihr immernoch mehr rechnungen braucht könnt ihr bei maxfev die zahl weiter erhöhen
# an diesem punkt wird auch die Funktion aus zeile 233 "gerufen", weswegen die rechnung her durchgeführt wird.
params, pcov = curve_fit(gedaempfte_schwingung, t_fit_laden, U_fit_laden, p0=p0, sigma=sigma_1, absolute_sigma=True, maxfev=10000)

# nun werden die daten einweiteres mal in variablen geladen, damit diese verwendet werden können um den graphen zu plotten
U_0_fit, delta_fit, omega_fit, phi_fit = params
U_0_err, delta_err, omega_err, phi_err = np.sqrt(np.diag(pcov))



######################
# Fit für die Dämpfungskonstante des zweiten Dokuments, wieder: gleiche Kommentare wie oben
######################
laden_start_2_fit = 0
laden_stop_2_fit  = 6

idx_2 = np.where(t_2.values > laden_start_2_fit)[0]
start_index_laden_2 = idx_2[0] if len(idx_2) > 0 else 0

idx_stop_2 = np.where(t_2.values > laden_stop_2_fit)[0]
stop_index_laden_2 = idx_stop_2[0] if len(idx_stop_2) > 0 else len(t_2) - 1

U_fit_laden_2  = U_2.iloc[start_index_laden_2:stop_index_laden_2].values
t_data_laden_2 = t_2.iloc[start_index_laden_2:stop_index_laden_2].values
t_fit_laden_2 = t_data_laden_2 - t_data_laden_2[0]

p0_2 = [U_fit_laden_2[0], 0.05, 5.8, 0.0]
sigma_2 = U_oszi_err_2 * np.ones_like(U_fit_laden_2)

params_2, pcov_2 = curve_fit(gedaempfte_schwingung, t_fit_laden_2, U_fit_laden_2, p0=p0_2, sigma=sigma_2, absolute_sigma=True, maxfev=10000)

U_0_fit_2, delta_fit_2, omega_fit_2, phi_fit_2 = params_2
U_0_err_2, delta_err_2, omega_err_2, phi_err_2 = np.sqrt(np.diag(pcov_2))



######################
# Abbildung 1
######################
# der plot wird ein verhältnis von 8:5 haben, also 8 Einheiten Breit und 5 einheiten Hoch, die punkte könnt ihr ändern um die Daten etwas zu stretchen, damit es bspw leichter lesbar ist
# falls die Legenden verschoben sind
plt.figure(figsize=(8, 5))

# Farbe der Graphen und dessen Bezeichnung in der Legende, den namen bitte zwischen die -> 'Name hier' <- eintragen, das "r" hat schon seinen zweck
plt.plot(t_1, U_1, color='tab:blue',   label=r'#10 0,141 µF ±4%; 1549 Ω ±0,8%; 105 mH ±2%')
plt.plot(t_2, U_2, color='tab:orange', label=r'#11 0,141 µF ±4%; 997 Ω ±0,8%; 52 mH ±2%')

# Auswahl der Werte für die x-Achse und der jeweils bessere Wert zur darstellung wird verwendet. Diese Variablen stehen oben beim Einstellen der Graphen
# habe ich ja eben schon angetease, hier wird also die x-achse limitiert um nur die relevanten punkte anzuzeigen. Falls ihr unzufrieden seit. schaut einfach oben
# ob ihr alles richtig eingetragen habt
anzeige_start = min(anzeige_start_1, anzeige_start_2)
anzeige_stop  = max(anzeige_stop_1,  anzeige_stop_2)

# x-Achse wird auf die genannten werte reduziert.
plt.xlim(anzeige_start, anzeige_stop)

#Möglichkeit einen bestimmten Bereich zu markieren. Ist dann für Zukünftige Protokolle wichtig! Wurder hier aber nicht verwendet!. löscht dafür das "#" aus der nächsten Zeile
#plt.axvspan(laden_start, laden_stop, alpha=0.5, color='tab:orange', label=r'Vier Schwingungen von #2')


######################
# Abbildung 2, und nochmal: gleiche Kommentare wie oben
######################
plt.figure(figsize=(8, 5))

U_err_plot_1 = U_oszi_err_1 * np.ones_like(U_fit_laden)
U_err_plot_2 = U_oszi_err_2 * np.ones_like(U_fit_laden_2)


# plotten der Messdaten mit Fehler
# errorevery=20 sorgt dafür, dass nur jeder 20. Punkt einen Fehlerbalken bekommt, damit es übersichtlich bleibt
plt.errorbar(t_data_laden, U_fit_laden, yerr=U_err_plot_1, fmt='o', markersize=2, capsize=2, elinewidth=0.5, errorevery=20, color='tab:blue', label='Messdaten #10 (Fit-Bereich)', alpha=0.5)
plt.errorbar(t_data_laden_2, U_fit_laden_2, yerr=U_err_plot_2, fmt='s', markersize=2, capsize=2, elinewidth=0.5, errorevery=20, color='tab:orange', label='Messdaten #11 (Fit-Bereich)', alpha=0.5)

# Plotten des Fits
plt.plot(t_data_laden, gedaempfte_schwingung(t_fit_laden, *params), linewidth=2, color='tab:blue', label='Fit #10', alpha=1)
plt.plot(t_data_laden_2, gedaempfte_schwingung(t_fit_laden_2, *params_2), linewidth=2, color='tab:orange', label='Fit #11', alpha=1)

# formatierung des Graphen
plt.xlabel(r'Zeit $t$ in ms')
plt.ylabel(r'Spannung $U$ in mV')
plt.title(r'Schwingkreis – Fit der Dämpfungskonstante')
plt.minorticks_on()
plt.grid(True, which='major', linewidth=0.8)
plt.grid(True, which='minor', linewidth=0.3, linestyle=':')


# Infotexte im Plot
info_1 = (
    # Titel
    r"$\mathbf{Fit\ \#10}$" + "\n"
    # Formel des Fits
    r"$U(t) = U_0 \cdot e^{-\delta t} \cdot \cos(\omega_d t + \varphi)$" + "\n"
    
    # berechneten werte des Fits, also Spannung, Dämpfungskonstante und Kreisfrequenz
    rf"$U_0 = ({U_0_fit:.1f} \pm {U_0_err:.1f})$ mV" + "\n"
    rf"$\delta = ({delta_fit:.4f} \pm {delta_err:.4f})$ 1/ms" + "\n"
    rf"$\omega_d = ({omega_fit:.3f} \pm {omega_err:.3f})$ rad/ms"
)
# formatierung
# 0.75 und 0.75 ist der Ort der box
plt.text(0.75, 0.75, info_1, transform=plt.gca().transAxes, fontsize=8, verticalalignment='top', color='tab:blue', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

# gleiche spiel nochmal hier
info_2 = (
    r"$\mathbf{Fit\ \#11}$" + "\n"
    r"$U(t) = U_0 \cdot e^{-\delta t} \cdot \cos(\omega_d t + \varphi)$" + "\n"
    rf"$U_0 = ({U_0_fit_2:.1f} \pm {U_0_err_2:.1f})$ mV" + "\n"
    rf"$\delta = ({delta_fit_2:.4f} \pm {delta_err_2:.4f})$ 1/ms" + "\n"
    rf"$\omega_d = ({omega_fit_2:.3f} \pm {omega_err_2:.3f})$ rad/ms"
)
#0.75 und 0.97 sind der Ort der box
plt.text(0.75, 0.97, info_2, transform=plt.gca().transAxes, fontsize=8, verticalalignment='top', color='tab:orange', bbox=dict(boxstyle='round', facecolor='white', alpha=0.7))

plt.legend()
plt.tight_layout()
ergebnis_ordner = Path(__file__).parent / "Ergebnisse"
ergebnis_ordner.mkdir(exist_ok=True)

# Speichert den Plot im Unterordner Ergebnisse
plt.savefig(ergebnis_ordner / "plot.pdf")



'''

die Datei Struktur sieht also wie folgt aus:


/euer eigener Ordner
    /Mappe1.csv
    /Mappe2.csv
    /Vorlage.py
    
    /Ergebnisse
        /plot.pdf


'''



print("Skript ist zu Ende")






