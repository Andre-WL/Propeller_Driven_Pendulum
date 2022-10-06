import csv
import matplotlib.pyplot as plt
import numpy as np

def find_peak(t,theta):
    peak_val = 0
    peak_index = 0
    for i in range(len(theta)-1):
        if theta[i] > peak_val:
            peak_val = thet[i]
            peak_index = i
    return [t[i],peak_val]

def find_freq(t,theta):
    r = 0.165 #distance from axis to applied torque from prop
    d = 0.14 #distance form axis to centre of mass
    m = 0.168 #mass of pendulum
    g = 9.81 #graviational constant
    max_val = 0
    max_time = 0
    peak_times = []
    impulse = []
    for i in range(len(theta)):
        if i < len(theta)-1 and i > 0:
            if theta[i]>theta[i-1] and theta[i]>theta[i+1]:
                peak_times.append(t[i])
        if theta[i]>max_val:
            max_val = theta[i]
            max_time = t[i]
    periods = []
    for i in range(len(peak_times)-1):
        periods.append(peak_times[i+1]-peak_times[i])
    period = np.mean(periods)
    freq = 1/period
    omega = freq*2*np.pi
    overshoot = max_val/255
    ln_overshoot = np.log(overshoot)
    zeta = (-1*ln_overshoot)/(np.sqrt(((np.pi)**2)+(ln_overshoot**2)))
    theta = np.arccos(zeta)
    omega_n = omega/np.sin(theta)
    sigma = zeta*omega_n
    Jp = m*g*d/(omega**2+sigma**2)
    c = sigma*2*Jp
    settle = np.arcsin(g*m*d)
    for i in range(len(t)):
        impulse.append(-255*np.exp(-1*sigma*t[i])*np.cos(omega*t[i])+1)
    print('omega = ',omega,'rads^-1    (found by taking inverse of average peak to peak time, then multiplying by 2pi)')
    print('Time to peak = ',max_time,'s')
    print('Overshoot = ',overshoot)
    print('damping ratio =',zeta)
    print('Theta = ', theta)
    print('omega_n = ',omega_n)
    print('sigma = ',sigma)
    print('Jp =',Jp)
    print('c =',c)
    print('Settled angle at 1Nm = ',settle)
    return impulse

def graph_data(t,theta,impulse):
    plt.plot(t,theta,label = 'data')
    plt.plot(t,impulse,label='-255*e^(-0.6689*t)cos(6.5*t)')
    #plt.ylim([-100,100])
    plt.legend()
    plt.title('Angular displacement vs Time')
    plt.xlabel('Time (s)')
    plt.ylabel('Angular displacement')
    plt.grid()
    plt.show()

def load_data():
    t = []
    theta = []
    with open('Lab3_Data.csv','r') as input_csv:
        reader = csv.reader(input_csv, delimiter='\t')
        for row in reader:
            t.append(float(row[0]))
            theta.append(float(row[1]))
    impulse = find_freq(t,theta)
    graph_data(t,theta,impulse)

def main():
    load_data()
    #graph_data(t,theta)

if __name__ == "__main__":
    main()
