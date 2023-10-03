import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, Callable

# Oppgaven er nederst!

# Gi noen typehinting for funksjonen, slik at du enklere kan se hva den returnerer
posisjon, fart, tid = np.ndarray, np.ndarray, np.ndarray 

def løsODE(tmax, x0: np.ndarray, v0: np.ndarray, dt, ODE: Callable, showPlot=True) -> Tuple[posisjon, fart, tid]:
    """
    Løser en andre ordens ODE med Eulers metode. 

    Parametere
    ----------
    tmax : float
        Tidslengden som skal løses over.
    x0 : np.ndarray
        Startposisjonen.
    v0 : np.ndarray
        Startfarten.
    dt : float
        Tidssteget.
    ODE : function
        Funksjonen som skal løses. Denne må ta inn x, v og t som parametere.
    showPlot : bool, optional
        Viser plottet av løsningen hvis True. Default er True.
    """

    ts = np.arange(0, tmax, dt)
    xs = np.zeros((len(ts), len(x0)))   
    vs = np.zeros((len(ts), len(v0)))

    xs[0] = x0
    vs[0] = v0

    for i in range(1, len(ts)):
        xs[i] = xs[i-1] + vs[i-1] * dt
        vs[i] = vs[i-1] + ODE(xs[i-1], vs[i-1], ts[i-1]) * dt
    
    if showPlot:
        plt.plot(xs[:, 0], xs[:, 1])
        plt.show()
    
    return xs, vs, ts


def plotXY(xy, vs, lagre=False):
    """
    Lager et plot av banen til et objekt i to dimensjoner.
    Fargen til banen i et punkt gir hastigheten til objektet!
    """

    # Denne bare plotter for special case 2 dimesnjoner, ikke tenk så mye på det!
    
    from matplotlib.collections import LineCollection
    
    points = np.array([xy[:,0], xy[:,1]]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)

    fig, axs = plt.subplots()

    # Create a continuous norm to map from data points to colors
    norm = plt.Normalize(np.linalg.norm(vs, axis = 1).min(), np.linalg.norm(vs, axis = 1).max())
    lc = LineCollection(segments, cmap='viridis', norm=norm)
    lc.set_array(np.linalg.norm(vs, axis = 1))
    lc.set_linewidth(2)
    line = axs.add_collection(lc)
    axs.plot(xy[:,0], xy[:,1])
    fig.colorbar(line, ax=axs, label="Hastighet")
    plt.show()
    if lagre:
        plt.savefig("oppgaveX.png")


def lagreLøsningIBilde(xs, vs, ts):
    fig, ax = plt.subplots(1,2)

    ax[0].set_title("Fart")
    ax[1].set_title("Posisjon")

    for dim in range(len(xs[0])):
        ax[1].plot(ts, xs[:, dim])
        ax[0].plot(ts, vs[:, dim])

    plt.savefig("oppgaveX.png")

def minDifferensialligning(x, v, t):
    # Dempet pendel i to dimensjoner! 
    return -x -0.1*v #+ #0.1*np.sin(t)


def dinDifferensialligning(x: np.ndarray, v, t):
    """
    Nå er det din tur, lag din egen differensialligning som tar inn x, v og t som parametere og returnerer en numpy-array med
    akselerasjonen. Denne arrayen må ha dimensjon lik v og x sin dimensjon, ie. hvis x = [x1, x2] må a = [a1, a2]
    """
    return x.copy()*0

# Skriv din kode under! 
# Du kan begynne med å kjøre
# --------
# position, velocity, times = løsODE(10, np.array([0, 0]), np.array([1, 1]), 0.01, minDifferensialligning)
# plotXY(position, velocity)
# --------
# ^ for å se hvordan løsODE fungerer.
# --------
# interessant = bool(input("Er dette interessant? (1 hvis ja, 0 hvis nei)"))
#
# if interessant:
#     plotXY(position, velocity, lagre=True)
# else:
#     print("Ok, ha en fin dag!")
#
# Se så på funksjonen LøsODE og se om du kan lage en egen differensialligning som gir et gøyt plot :)
# Last så opp KUN din funksjon på GitHub vha git med et passende navn under og send en pull request!
# Legg gjerne ved det lagrede bildet ditt i pull-requesten  under en mappe med navn "Bilder" =)
# -- Henrik, differensialligning-entusiast

