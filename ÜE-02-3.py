__author__= '7340644: Hassel'


import select
import sys
import time


def calculateNewInfected(rValue, totalInfected, i):
    """
        Eine Funktion, welche die Anzahl der neuen Infektionen berechnet.

        Attributes
        ----------
        rValue : int
            Berechneter R Wert.
        totalInfected : int
            Anzahl aller Infektionen.
        i : int
            Anzahl der Iterationen

    """
    return totalInfected * pow(rValue, i)


def calRValue(infected1, infected2):
    """
            Eine Funktion, welche den R Wert berechnet.

            Attributes
            ----------
            infected1 : int
                Infizierte zum Zeitpunkt T1.
            infected2 : int
                Infizierte zum Zeitpunkt T2.

    """
    return infected2 / infected1


def output(rValue, totalInfected):
    """
        Eine Funktion, welche den R Wert und die Anzahl der Infizierten in die Konsole ausgibt.

        Attributes
        ----------
        rValue : int
            Berechneter R Wert.
        totalInfected : int
            Anzahl aller Infizierten.

    """
    print("R Wert: " + str(rValue) + "  Anzahl Infizierte: " + str(totalInfected))


if __name__ == '__main__':
    """
        Die main Funktion, welche beim Start ausgeführt wird.
        Es wird über die Anzahl der Infizierten als Eingabe gefragt und
        berechnet pro iteration der while schleife die neuen Infizierten.
        
        Das Programm kann mit der Eingabe q in der Konsole beendet werden.
    
    """
    iterations = 1
    infected_1 = input("Infizierte Zum Zeitpunkt T1:")
    infected_2 = input("Infizierte Zum Zeitpunkt T1 + T:")

    if infected_1.isdigit() and infected_2.isdigit():
        infected_2 = int(infected_2)
        infected_1 = int(infected_1)

        total_infected = infected_1 + infected_2

        r_value = calRValue(infected_1, infected_2)

        output(r_value, total_infected)

        while True:
            total_infected = calculateNewInfected(r_value, total_infected, iterations)
            iterations += 1
            output(r_value, total_infected)
            time.sleep(1)
            if sys.stdin in select.select([sys.stdin], [], [], 0)[0]:
                line = input()
                if line == "q":
                    break
